#!/usr/bin/env python3
"""
Anticloud Tier-Agent Benchmark Engine
Real static analysis over cloned source. No AI/LLM-latency checks.
Stdlib only. Emits CycloneDX SBOM + per-check evidence.
"""
from __future__ import annotations
import os, re, json, sys, hashlib, subprocess, time, argparse, datetime, fnmatch, stat
from pathlib import Path

# ---------------------------------------------------------------- constants
VENDOR_DIRS = {'.git', 'node_modules', 'vendor', 'third_party', '3rdparty',
               '.venv', 'venv', 'build', 'dist', '__pycache__', '.mypy_cache',
               '.pytest_cache', '.tox', 'target', 'deps', 'external', 'subprojects',
               'cmake', 'extern', '.yarn', '.turbo', '.next', 'coverage',
               '.serverless', '.parcel-cache', '.nuxt', 'out', 'storybook-static'}
MINIFIED_SUFFIXES = ('.min.js', '.min.css', '.bundle.js', '.bundle.css')
SKIP_SCAN_FILES = {'yarn.lock', 'package-lock.json', 'pnpm-lock.yaml',
                   'Cargo.lock', 'poetry.lock', 'composer.lock'}
MAX_SCAN_BYTES = 500_000
MAX_SINGLE_LINE = 200_000
# NOTE: 'contrib', 'tests'/'test', 'docs'/'doc', '.github', 'examples' and
# 'benchmarks' were previously in this skip set.  They are NOT vendor code —
# in Django/Python and many C/C++ projects `contrib/` and `tests/` hold real
# source.  Skipping them made files_total and lines_of_code understate every
# project (DJANGO_HEALTH read 20 files / 940 LOC when the tree holds 68 files
# and its `health_check/contrib/*.py` modules are part of the shipped
# architecture).  A skip list is only correct for directories that genuinely
# hold third-party or generated content.
CODE_EXT = {'.py','.c','.h','.cpp','.hpp','.cc','.cxx','.java','.js','.ts','.tsx',
            '.jsx','.go','.rs','.rb','.php','.cs','.swift','.kt','.scala','.m','.mm',
            '.sh','.bash','.pl','.lua','.jl','.r','.f90','.f','.cu','.cl',
            '.ex','.exs','.erl','.hrl','.'}
CODE_EXT.discard('.')
SRC_EXT = {'.py','.c','.h','.cpp','.hpp','.cc','.cxx','.js','.ts','.tsx','.jsx','.go',
           '.rs','.java','.sh','.bash','.rb','.php','.cs','.swift','.kt','.lua','.pl',
           '.m','.mm','.cu','.cl','.ex','.exs','.erl'}
BIN_EXT = {'.png','.jpg','.jpeg','.gif','.bmp','.ico','.svg','.webp','.pdf','.zip',
           '.gz','.bz2','.xz','.7z','.tar','.exe','.dll','.so','.dylib','.a','.o',
           '.pyc','.pyo','.woff','.woff2','.ttf','.eot','.mp3','.mp4','.wav','.ogg',
           '.mo','.jar','.class','.bin','.dat','.onnx','.pt','.pth','.safetensors'}

# ---------------------------------------------------------------- licences
LIC_CLASS_A = {'MIT','Apache-2.0','BSD-2-Clause','BSD-3-Clause','ISC','MPL-2.0',
               '0BSD','Unlicense','Apache-2.0-with-LLVM-exception','BSD-3-Clause-Clear'}
LIC_CLASS_B = {'GPL-1.0','GPL-2.0','GPL-3.0','AGPL-1.0','AGPL-3.0','LGPL-2.0',
               'LGPL-2.1','LGPL-3.0','SSPL-1.0','Commons-Clause','GPL-2.0-only',
               'GPL-3.0-only','GPL-3.0-or-later','AGPL-3.0-only','MPL-2.0-no-copyleft-exception'}
LIC_NONCOMMERCIAL_HINT = re.compile(
    r'non[- ]?commercial|not (?:be )?used for commercial|educational (?:and|or) research only'
    r'|free for personal use|academic use only|cc[- ]by[- ]nc', re.I)

LIC_PATTERNS = [
    ('AGPL-3.0', re.compile(r'Affero General Public License.*?Version 3', re.I|re.S)),
    ('AGPL-3.0', re.compile(r'\bAGPL\b|GNU AFFERO', re.I)),
    ('LGPL-3.0', re.compile(r'GNU Lesser General Public License.*?Version 3', re.I|re.S)),
    ('LGPL-2.1', re.compile(r'GNU Lesser General Public License.*?Version 2\.1', re.I|re.S)),
    ('GPL-3.0',  re.compile(r'GNU GENERAL PUBLIC LICENSE\s+Version 3', re.I)),
    ('GPL-2.0',  re.compile(r'GNU GENERAL PUBLIC LICENSE\s+Version 2', re.I)),
    ('MPL-2.0',  re.compile(r'Mozilla Public License Version 2\.0', re.I)),
    ('Apache-2.0',re.compile(r'Apache License\s+.*?Version 2\.0', re.I|re.S)),
    ('MIT',      re.compile(r'\bMIT License\b|Permission is hereby granted, free of charge', re.I)),
    ('ISC',      re.compile(r'Permission to use, copy, modify,? and/or distribute this software', re.I)),
    ('BSD-3-Clause', re.compile(r'Neither the name of|3\. Neither the name', re.I)),
    ('BSD-2-Clause', re.compile(r'This source code form subject to the terms of the BSD', re.I)),
    ('SSPL-1.0', re.compile(r'Server Side Public License', re.I)),
    ('Commons-Clause', re.compile(r'"Commons Clause"|Commons Clause condition', re.I)),
    ('BSL-1.0', re.compile(r'Boost Software License', re.I)),
    ('Unlicense', re.compile(r'This is free and unencumbered software released into the public domain', re.I)),
    ('CDDL-1.0', re.compile(r'COMMON DEVELOPMENT AND DISTRIBUTION LICENSE', re.I)),
    ('EPL-2.0', re.compile(r'Eclipse Public License.*?2\.0', re.I|re.S)),
]

# ---------------------------------------------------------------- scanners
class Finding:
    __slots__=('rule','severity','file','line','snippet','cwe')
    def __init__(s,r,sev,f,l,sn,cwe=''):
        s.rule,s.severity,s.file,s.line,s.snippet,s.cwe=r,sev,f,l,sn,cwe
    def d(s):
        return {'rule':s.rule,'severity':s.severity,'file':s.file,'line':s.line,
                'cwe':s.cwe,'snippet':(s.snippet or '')[:180]}

OWASP_TOP10 = {
 'A01-BrokenAccessControl': [
   (re.compile(r'\b(verify\s*=\s*False|rejectUnauthorized\s*:\s*false|CURLOPT_SSL_VERIFYPEER\s*,\s*0|CURLOPT_SSL_VERIFYHOST\s*,\s*0)',re.I),'high','CWE-295'),
   (re.compile(r'os\.chmod\([^)]*0o?777'),'high','CWE-732'),
   (re.compile(r'\bchmod\s+777\b'),'high','CWE-732'),
 ],
 'A02-CryptographicFailures': [
   (re.compile(r'\b(md5|sha1)\s*\(',re.I),'medium','CWE-327'),
   (re.compile(r'\bMD5\b'),'medium','CWE-327'),
   (re.compile(r'\bDES\b|RC4|ECB'),'high','CWE-327'),
   (re.compile(r'random\.(random|randint|choice)\([^)]*\)\s*.*(token|secret|password|nonce|salt|key)',re.I),'high','CWE-338'),
   (re.compile(r'SecRandomCopyBytes|arc4random|Mersenne|mt19937',re.I),'medium','CWE-338'),
 ],
 'A03-Injection': [
   (re.compile(r'\beval\s*\('),'high','CWE-95'),
   (re.compile(r'\bexec\s*\(\s*[a-zA-Z_]'),'high','CWE-95'),
   (re.compile(r'shell\s*=\s*True'),'high','CWE-78'),
   (re.compile(r'os\.system\s*\('),'high','CWE-78'),
   (re.compile(r'popen\s*\('),'high','CWE-78'),
   (re.compile(r'sprintf\s*\('),'high','CWE-120'),
   (re.compile(r'\bstrcpy\s*\(|\bstrcat\s*\(|\bgets\s*\('),'high','CWE-120'),
   (re.compile(r'\$\(\s*[a-z_]+\s*\)'),'high','CWE-78'),
   (re.compile(r'system\s*\(\s*argv'),'medium','CWE-78'),
   (re.compile(r'yaml\.load\s*\((?![^)]*Safe)',),'high','CWE-502'),
   (re.compile(r'pickle\.loads?\s*\(|cPickle\.loads?\s*\('),'high','CWE-502'),
   (re.compile(r'marshal\.loads?\s*\('),'medium','CWE-502'),
   (re.compile(r'(SELECT|INSERT|UPDATE|DELETE)\s+.*(\+|%s|\{).*FROM',re.I),'high','CWE-89'),
   (re.compile(r'\.\s*format\s*\(.*\)\s*["\']?\s*\+'),'medium','CWE-89'),
 ],
 'A04-InsecureDesign': [
   (re.compile(r'TODO|FIXME|XXX|HACK',re.I),'low','CWE-'),
 ],
 'A05-SecurityMisconfiguration': [
   (re.compile(r'default\s*=\s*True'),'medium','CWE-1188'),
   (re.compile(r'--insecure|-k\s*--insecure|verify=False'),'medium','CWE-1188'),
   (re.compile(r'\bDEBUG\s*=\s*True\b'),'medium','CWE-489'),
   (re.compile(r'\bAllowAll\b|PermitAll|trust\s+all',re.I),'high','CWE-1188'),
   (re.compile(r'cors\(\)|Access-Control-Allow-Origin.*\*',re.I),'high','CWE-942'),
 ],
 'A06-VulnerableComponents': [
   (re.compile(r'==\s*\d+\.\d+\.\d+'),'low','CWE-1104'),
 ],
 'A07-AuthFailures': [
   (re.compile(r'password\s*=\s*["\'][^"\']{3,}["\']',re.I),'high','CWE-798'),
   (re.compile(r'(api[_-]?key|secret|token|passwd)\s*=\s*["\'][A-Za-z0-9_\-]{12,}["\']',re.I),'high','CWE-798'),
   (re.compile(r'(?i)(default|admin|guest|test)\s*/\s*(admin|password|pass|root|12345)'),'high','CWE-798'),
   (re.compile(r'Authorization:\s*(Bearer|Basic)\s+[A-Za-z0-9_\-\.=]{20,}'),'high','CWE-798'),
   (re.compile(r'AKIA[0-9A-Z]{16}'),'high','CWE-798'),
   (re.compile(r'-----BEGIN (RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----'),'high','CWE-798'),
 ],
 'A08-SoftwareDataIntegrity': [
   (re.compile(r'http://[^\s"\']+'),'low','CWE-319'),
   (re.compile(r'curl[^\n]*\|\s*(ba)?sh|wget[^\n]*\|\s*(ba)?sh'),'high','CWE-494'),
   (re.compile(r'--allow-untrusted-root|--no-check-certificate|-k\s+https?://'),'high','CWE-494'),
   (re.compile(r'ETag\s*\)?\s*:',re.I),'low','CWE-'),
 ],
 'A09-LoggingMonitoringFailures': [
   (re.compile(r'sys\.excepthook\s*=\s*None'),'medium','CWE-778'),
   (re.compile(r'except[^\n]*:\s*(#.*)?$'),'low','CWE-390'),
 ],
 'A10-SSRF': [
   (re.compile(r'(requests|urlopen|curl|fetch)\s*\(\s*[a-z_]*url\b'),'medium','CWE-918'),
   (re.compile(r'redirect\s*\(', ),'low','CWE-601'),
 ],
}

OWASP_LLM10 = {
 'LLM01-PromptInjection': [
   (re.compile(r'(system_prompt|SYSTEM_PROMPT|systemPrompt)\s*[:=]',re.I),'low','CWE-1427'),
   (re.compile(r'jinja2\.Template\(|Template\(',),'medium','CWE-1336'),
   (re.compile(r'eval\(.*prompt',re.I),'high','CWE-95'),
 ],
 'LLM02-SensitiveInfoDisclosure': [
   (re.compile(r'(os\.environ|getenv)\s*\(\s*["\'](API_KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL)',re.I),'high','CWE-798'),
   (re.compile(r'\bOPENAI_API_KEY\b|\bHF_TOKEN\b|\bAWS_SECRET\b',),'high','CWE-798'),
 ],
 'LLM03-SupplyChain': [
   (re.compile(r'pip install\s+[^\n]*(http://|-e\s+git)'),'high','CWE-494'),
   (re.compile(r'requests\.get\(["\']https?://[^\s"\']+/download'),'high','CWE-494'),
   (re.compile(r'from_pretrained\(|hf_hub_download\(',),'medium','CWE-494'),
 ],
 'LLM04-DataPoisoning': [
   (re.compile(r'json\.loads?\([^)]*(request|input|user)',re.I),'medium','CWE-20'),
 ],
 'LLM05-ImproperOutputHandling': [
   (re.compile(r'\b(eval|exec)\(\s*(completion|response|output|result)',re.I),'high','CWE-95'),
   (re.compile(r'subprocess[^\n]*\+\s*(completion|response|output)',re.I),'high','CWE-78'),
 ],
 'LLM06-ExcessiveAgency': [
   (re.compile(r'\bos\.system\s*\(.*(llm|agent|completion|response)',re.I),'high','CWE-78'),
   (re.compile(r'(auto_?approve|skip_?confirm|confirm\s*=\s*False)',re.I),'high','CWE-862'),
 ],
 'LLM07-SystemPromptLeak': [
   (re.compile(r'(reveal|print|log|expose).{0,20}(system prompt|instructions)',re.I),'medium','CWE-200'),
 ],
 'LLM08-VectorEmbeddingWeaknesses': [
   (re.compile(r'(chroma|faiss|weaviate|pinecone|milvus)',re.I),'low','CWE-'),
 ],
 'LLM09-Misinformation': [
   (re.compile(r'assert.{0,30}(ground.?truth|verif)',re.I),'low','CWE-'),
 ],
 'LLM10-UnboundedConsumption': [
   (re.compile(r'(max_tokens|num_predict)\s*=\s*-1'),'medium','CWE-400'),
   (re.compile(r'while\s+True\s*:\s*\n\s+(recv|read|input)\(',re.I),'high','CWE-400'),
 ],
}

# ---------------------------------------------------------------- utilities
def run_git(repo, *a):
    try:
        p = subprocess.run(['git','-C',str(repo)]+list(a), capture_output=True,
                           text=True, timeout=30)
        return p.stdout.strip() if p.returncode==0 else ''
    except Exception:
        return ''

def _is_reparse_point(path):
    """True for a Windows junction / symlink / mount point.

    ``os.walk(followlinks=False)`` only refuses *symlinks*; on Windows a
    directory junction is a reparse point that walk follows anyway.  A
    junction pointing at an ancestor therefore makes the walk recurse
    forever.  This is what hung the NEQSIM run: the process sat inside
    os.walk for over an hour and never reached the analysis stage.
    """
    try:
        st = os.lstat(path)
    except OSError:
        return True
    if stat.S_ISLNK(st.st_mode):
        return True
    attrs = getattr(st, 'st_file_attributes', 0)
    return bool(attrs & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400))


def walk_files(root, limit_bytes=6_000_000, max_files=250_000, max_depth=20,
               time_budget=900.0):
    """Collect files under ``root`` with hard bounds.

    Bounds exist so a pathological tree cannot hang a run forever, but they
    are deliberately generous: an earlier 45s/25k budget silently truncated
    real projects and wrote a low file count as though it were complete
    (DJANGO_HEALTH read as 13 files when the full tree is 26).  A truncated
    walk is now marked in the report and must never be presented as a
    complete scan.
    """
    out = []
    root = Path(root)
    deadline = time.monotonic() + time_budget
    truncated = False

    stack = [(str(root), 0)]
    seen_dirs = set()

    while stack:
        if time.monotonic() > deadline or len(out) >= max_files:
            truncated = True
            break
        cur, depth = stack.pop()
        if depth > max_depth:
            continue
        try:
            real = os.path.realpath(cur)
        except OSError:
            continue
        # A cycle shows up as a directory whose real path we already entered.
        if real in seen_dirs:
            continue
        seen_dirs.add(real)

        try:
            entries = list(os.scandir(cur))
        except OSError:
            continue

        for ent in entries:
            if len(out) >= max_files or time.monotonic() > deadline:
                truncated = True
                break
            try:
                if ent.is_dir(follow_symlinks=False):
                    name = ent.name
                    if name in VENDOR_DIRS or name == '.git':
                        continue
                    if name.startswith('.'):
                        continue
                    if _is_reparse_point(ent.path):
                        continue
                    stack.append((ent.path, depth + 1))
                    continue
                if not ent.is_file(follow_symlinks=False):
                    continue
            except OSError:
                continue

            p = Path(ent.path)
            try:
                st = p.lstat()
            except OSError:
                continue
            ext = p.suffix.lower()
            lname = p.name.lower()
            if lname.endswith(MINIFIED_SUFFIXES) or lname in SKIP_SCAN_FILES:
                out.append({'path': str(p.relative_to(root)).replace('\\', '/'),
                            'ext': ext, 'size': st.st_size,
                            'skipped_scan': 'minified-or-lockfile'})
                continue
            if st.st_size > MAX_SCAN_BYTES:
                out.append({'path': str(p.relative_to(root)).replace('\\', '/'),
                            'ext': ext, 'size': st.st_size,
                            'skipped_scan': 'over-size-cap'})
                continue
            rec = {'path': str(p.relative_to(root)).replace('\\', '/'),
                   'ext': ext, 'size': st.st_size}
            if ext in SRC_EXT and st.st_size <= limit_bytes:
                try:
                    b = p.read_bytes()
                    if b.find(b'\n', 0, MAX_SINGLE_LINE) == -1 and len(b) > 100_000:
                        rec['sha256'] = hashlib.sha256(b).hexdigest()
                        rec['skipped_scan'] = 'single-line-minified'
                        out.append(rec)
                        continue
                    rec['sha256'] = hashlib.sha256(b).hexdigest()
                    rec['raw'] = b
                except OSError:
                    rec['sha256'] = None
            out.append(rec)

    if truncated:
        # Recorded in the report so a partial scan is never mistaken for a
        # complete one.
        out.append({'path': '<WALK-TRUNCATED>', 'ext': '', 'size': 0,
                    'truncated': True,
                    'reason': f'budget {time_budget}s or {max_files} files'})
    return out

def count_lines(b):
    if not b: return 0
    return b.count(b'\n') + (0 if b.endswith(b'\n') else 1)

def decode(b):
    if b is None: return ''
    try: return b.decode('utf-8')
    except UnicodeDecodeError:
        try: return b.decode('latin-1')
        except Exception: return ''

# ---------------------------------------------------------------- dep parsing
DEP_FILES = {
 'requirements.txt': 'pypi', 'requirements-dev.txt':'pypi', 'requirements/*.txt':'pypi',
 'package.json':'npm', 'Cargo.toml':'cargo', 'pyproject.toml':'pypi',
 'setup.py':'pypi', 'setup.cfg':'pypi', 'Pipfile':'pypi', 'environment.yml':'conda',
 'CMakeLists.txt':'cmake', 'configure.ac':'m4', 'Makefile.am':'m4',
 'go.mod':'go', 'Gemfile':'rubygems', 'pom.xml':'maven', 'build.gradle':'maven',
 'meson.build':'meson', 'vcpkg.json':'vcpkg', 'conanfile.txt':'conan',
 'Dockerfile':'docker', '*.spec':'rpm', 'debian/control':'deb',
}

def parse_deps(root, files):
    deps=[]
    def add(ecosystem,name,ver,src,raw=''):
        name=(name or '').strip()
        if name and len(name)<200:
            deps.append({'ecosystem':ecosystem,'name':name,'version':ver or '',
                         'source_file':src,'raw':raw.strip()[:200]})
    for rec in files:
        p=rec['path']; name=p.split('/')[-1]; base=name
        txt=decode(rec.get('raw'))
        if not txt and base in ('pyproject.toml','package.json','Cargo.toml','go.mod',
                                'CMakeLists.txt','setup.py','Pipfile','meson.build',
                                'environment.yml','setup.cfg','conanfile.txt','vcpkg.json'):
            try: txt=Path(root,p).read_text(encoding='utf-8',errors='replace')
            except OSError: continue
        if base.startswith('requirements') and base.endswith('.txt'):
            for ln in txt.splitlines():
                ln=ln.split('#')[0].strip()
                if not ln or ln.startswith('-'): continue
                m=re.match(r'^([A-Za-z0-9._\-\[\]]+)\s*(?:\[[^\]]*\])?\s*(?:([=<>!~]=|[<>])\s*([^\s;]+))?',ln)
                if m: add('pypi',m.group(1),(m.group(2) or '')+ (m.group(3) or ''),p,m.group(0))
        elif base=='package.json':
            try: j=json.loads(txt)
            except Exception: j={}
            if not isinstance(j, dict): j={}
            for sect in ('dependencies','devDependencies','peerDependencies','optionalDependencies'):
                for k,v in (j.get(sect) or {}).items(): add('npm',k,str(v),p)
        elif base=='pyproject.toml' and '[project]' in txt:
            blk=re.search(r'\[project\](.*?)(?=\n\[|\Z)',txt,re.S)
            if blk:
                d=re.search(r'dependencies\s*=\s*\[(.*?)\]',blk.group(1),re.S)
                if d:
                    for it in re.findall(r'["\']([^"\']+)["\']',d.group(1)):
                        m=re.match(r'^([A-Za-z0-9._\-]+)\s*([^\s,;]*)',it)
                        if m: add('pypi',m.group(1),m.group(2),p,m.group(0))
        elif base=='Cargo.toml':
            for m in re.finditer(r'^\s*([A-Za-z0-9_\-]+)\s*=\s*(?:\{[^}]*version\s*=\s*"([^"]+)"[^}]*\}|"([^"]+)")',txt,re.M):
                add('cargo',m.group(1),m.group(2) or m.group(3) or '',p)
        elif base=='go.mod':
            for m in re.finditer(r'^\s*(?:require\s+)?([a-z0-9\./\-]+)\s+(v[^\s]+)',txt,re.M):
                add('go',m.group(1),m.group(2),p)
        elif base=='environment.yml':
            for m in re.finditer(r'-\s*([A-Za-z0-9_\-\.]+)[\s=]*([0-9][^\s#]*)?',txt):
                add('conda',m.group(1),m.group(2) or '',p,m.group(0))
        elif base=='Pipfile':
            for m in re.finditer(r'^"?([A-Za-z0-9._\-]+)"?\s*=\s*"?([^"\n]*)',txt,re.M):
                add('pypi',m.group(1),m.group(2),p)
        elif base=='setup.py':
            for m in re.finditer(r'["\']([A-Za-z0-9._\-]+[=<>!~ ][^"\']*)["\']',txt):
                s=m.group(1)
                if '://' in s: continue
                mm=re.match(r'^([A-Za-z0-9._\-]+)\s*([=<>!~].*)?$',s)
                if mm: add('pypi',mm.group(1),mm.group(2) or '',p,s)
        elif base in ('CMakeLists.txt','meson.build'):
            for m in re.finditer(r'(?:find_package|pkg_check_modules|dependency|requires)\s*\(\s*([A-Za-z0-9_.\-]+)',txt):
                add('native',m.group(1),'',p,m.group(0))
        elif base=='conanfile.txt':
            for m in re.finditer(r'^\s*([A-Za-z0-9_.\-]+)/([0-9][^\s#]*)',txt,re.M):
                add('conan',m.group(1),m.group(2),p)
        elif base=='vcpkg.json':
            try:
                for d in (json.loads(txt).get('dependencies') or []):
                    add('vcpkg',d if isinstance(d,str) else d.get('name',''),'' ,p)
            except Exception: pass
        elif base=='Dockerfile':
            for m in re.finditer(r'^\s*(?:FROM)\s+([^\s]+)',txt,re.M):
                add('container',m.group(1),'',p,m.group(0))
            for m in re.finditer(r'(apt-get install|apk add)[^\n]*',txt):
                for tok in re.findall(r'(?:^|\s)([a-z0-9][a-z0-9\-\.]{2,})',m.group(0)):
                    add('apt',tok,'',p,m.group(0)[:200])
    return deps

# ---------------------------------------------------------------- SBOM
def make_sbom(repo_name, version, files, deps):
    comps=[]
    seen=set()
    for d in deps:
        k=(d['ecosystem'],d['name'])
        if k in seen: continue
        seen.add(k)
        comps.append({'type':'library','name':d['name'],
                      'version':d['version'] or 'unspecified',
                      'purl':purl(d['ecosystem'],d['name'],d['version']),
                      'bom-ref':f"{d['ecosystem']}/{d['name']}@{d['version'] or 'unspecified'}"})
    lic = LICENSE_INFO['spdx']
    ts = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    return {
      'bomFormat':'CycloneDX','specVersion':'1.5','serialNumber':
        'urn:uuid:'+str(__import__('uuid').uuid5(__import__('uuid').NAMESPACE_URL,
                                                f'{repo_name}@{version}')),
        'version':1,'metadata':{'timestamp':ts,
          'component':{'type':'application','name':repo_name,'version':version,
                       'bom-ref':f'pkg:generic/anticloud/{repo_name}@{version}',
                       'purl':f'pkg:generic/anticloud/{repo_name}@{version}',
                       'licenses':[{'license':{'id':lic}}] if lic else []},
          'properties':[{'name':'anticloud:source-commit','value':GIT['head']},
                        {'name':'anticloud:source-url','value':GIT['url']},
                        {'name':'anticloud:tier','value':'tier-agent'}]},
      'components':comps}

def purl(eco,name,ver):
    v=ver or ''
    if eco=='pypi': return f'pkg:pypi/{name.lower().replace("_","-")}@{v.lstrip("=<>~! ")}' if v else f'pkg:pypi/{name.lower()}'
    if eco=='npm': return f'pkg:npm/{name}@{v}'
    if eco=='cargo': return f'pkg:cargo/{name}@{v}'
    if eco=='go': return f'pkg:golang/{name}@{v}'
    if eco=='container': return f'pkg:docker/{name}'
    if eco=='maven': return f'pkg:maven/{name}@{v}'
    if eco=='gem' or eco=='rubygems': return f'pkg:gem/{name}@{v}'
    return f'pkg:generic/{name}@{v}' if v else f'pkg:generic/{name}'

LICENSE_INFO={}
GIT={}

# ---------------------------------------------------------------- rule engine
RULE_KEYWORDS = {
    'A01-BrokenAccessControl': ('verify', 'chmod', 'rejectunauthorized', 'curlopt'),
    'A02-CryptographicFailures': ('md5', 'sha1', 'des', 'rc4', 'ecb', 'random', 'mersenne'),
    'A03-Injection': ('eval', 'exec', 'shell', 'system', 'popen', 'sprintf', 'strcpy', 'yaml', 'pickle', 'marshal', 'select', 'format'),
    'A04-InsecureDesign': ('todo', 'fixme', 'xxx', 'hack'),
    'A05-SecurityMisconfiguration': ('default', 'insecure', 'debug', 'allowall', 'cors', 'access-control'),
    'A06-VulnerableComponents': ('==',),
    'A07-AuthFailures': ('password', 'api_key', 'apikey', 'secret', 'token', 'authorization', 'akia', 'private key'),
    'A08-SoftwareDataIntegrity': ('http://', 'curl', 'wget', 'etag'),
    'A09-LoggingMonitoringFailures': ('excepthook', 'except'),
    'A10-SSRF': ('requests', 'urlopen', 'curl', 'fetch', 'redirect'),
    'LLM01-PromptInjection': ('system_prompt', 'systemprompt', 'jinja', 'template', 'prompt'),
    'LLM02-SensitiveInfoDisclosure': ('environ', 'getenv', 'api_key', 'hf_token', 'aws_secret', 'openai_api_key'),
    'LLM03-SupplyChain': ('pip install', 'requests.get', 'from_pretrained', 'hf_hub_download'),
    'LLM04-DataPoisoning': ('json.load',),
    'LLM05-ImproperOutputHandling': ('eval', 'exec', 'subprocess', 'completion', 'response'),
    'LLM06-ExcessiveAgency': ('os.system', 'auto_approve', 'skip_confirm', 'confirm'),
    'LLM07-SystemPromptLeak': ('system prompt', 'instructions'),
    'LLM08-VectorEmbeddingWeaknesses': ('chroma', 'faiss', 'weaviate', 'pinecone', 'milvus'),
    'LLM09-Misinformation': ('assert',),
    'LLM10-UnboundedConsumption': ('max_tokens', 'num_predict', 'while'),
}

def scan_rules(files, rules):
    """Apply every regex in ``rules`` to every scanned source file.

    Returns ``(findings_by_category, total_findings, files_with_findings)``.
    A file is read at most once per category so a repo with N categories does
    not pay N full-tree reads.
    """
    by_cat = {cat: [] for cat in rules}
    total = 0
    hit_files = set()
    for rec in files:
        raw = rec.get('raw')
        if raw is None:
            continue
        ext = rec.get('ext', '')
        if ext and ext not in SRC_EXT and ext not in CODE_EXT:
            continue
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError:
            try:
                text = raw.decode('latin-1')
            except Exception:
                continue
        if not text:
            continue
        # cheap pre-filter: skip files too small to hold a match
        if len(text) < 8:
            continue
        lowered = text.lower()
        for cat, pats in rules.items():
            keys = RULE_KEYWORDS.get(cat)
            if keys and not any(k in lowered for k in keys):
                continue
            for pat, sev, cwe in pats:
                try:
                    m = pat.search(text)
                except re.error:
                    continue
                if not m:
                    continue
                line_no = text.count('\n', 0, m.start()) + 1
                start = text.rfind('\n', 0, m.start()) + 1
                end = text.find('\n', m.end())
                snippet = text[start:end if end != -1 else len(text)].strip()
                by_cat[cat].append({
                    'severity': sev, 'file': rec['path'], 'line': line_no,
                    'cwe': cwe, 'snippet': snippet[:180],
                })
                total += 1
                hit_files.add(rec['path'])
                break  # one finding per rule per file keeps output bounded
    return by_cat, total, hit_files


def severity_counts(findings):
    counts = {'high': 0, 'medium': 0, 'low': 0}
    for f in findings:
        s = f.get('severity', 'low')
        counts[s] = counts.get(s, 0) + 1
    return counts


def detect_license(repo):
    """Return ``(spdx_id, class, source_file)`` by reading the licence file."""
    root = Path(repo)
    for name in ('LICENSE', 'LICENSE.txt', 'LICENSE.md', 'LICENCE', 'LICENCE.txt',
                 'COPYING', 'COPYING.txt', 'LICENSE.rst'):
        p = root / name
        if not p.is_file():
            continue
        try:
            text = p.read_text(encoding='utf-8', errors='replace')[:20000]
        except OSError:
            continue
        for spdx, pat in LIC_PATTERNS:
            if pat.search(text):
                if spdx in LIC_CLASS_A:
                    cls = 'A'
                elif spdx in LIC_CLASS_B:
                    cls = 'B'
                elif LIC_NONCOMMERCIAL_HINT.search(text):
                    cls = 'C'
                else:
                    cls = 'B'
                return spdx, cls, name
        return 'UNKNOWN', 'C', name
    return 'NOASSERTION', 'C', None


def collect_git(repo):
    head = run_git(repo, 'rev-parse', 'HEAD')
    url = run_git(repo, 'config', '--get', 'remote.origin.url')
    branch = run_git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
    stamp = run_git(repo, 'log', '-1', '--date=iso-strict', '--format=%ad')
    return {'head': head, 'url': url, 'branch': branch, 'committed_at': stamp}


def language_breakdown(files):
    counts = {}
    for rec in files:
        ext = rec.get('ext') or '(none)'
        counts[ext] = counts.get(ext, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: -kv[1])[:15])


def loc_counts(files):
    scanned = 0
    code = 0
    for rec in files:
        raw = rec.get('raw')
        if not raw:
            continue
        scanned += 1
        code += raw.count(b'\n') + (0 if raw.endswith(b'\n') else 1)
    return scanned, code


# ---------------------------------------------------------------- the run
def analyse(repo, project_name=None):
    """Run the full static analysis over one cloned repository."""
    repo = Path(repo)
    if not repo.is_dir():
        raise FileNotFoundError(f'no such repository: {repo}')

    global LICENSE_INFO, GIT
    all_files = walk_files(repo)
    GIT = collect_git(repo)
    spdx, lic_class, lic_src = detect_license(repo)
    LICENSE_INFO = {'spdx': spdx, 'class': lic_class, 'source': lic_src}

    deps = parse_deps(repo, all_files)
    owasp, owasp_total, owasp_files = scan_rules(all_files, OWASP_TOP10)
    llm, llm_total, llm_files = scan_rules(all_files, OWASP_LLM10)

    src_files, code_lines = loc_counts(all_files)
    name = project_name or repo.name.replace('_UPSTREAM_CLONE', '') or 'project'

    report = {
        'schema': 'anticloud.tier-bench/1',
        'project': name,
        'source': {
            'repo_path': str(repo),
            'git': GIT,
        },
        'metrics': {
            'files_total': len(all_files),
            'source_files_scanned': src_files,
            'lines_of_code': code_lines,
            'languages': language_breakdown(all_files),
        },
        'licence': {
            'spdx': spdx,
            'class': lic_class,
            'source_file': lic_src,
            'redistribution_allowed': lic_class == 'A',
        },
        'dependencies': {
            'count': len(deps),
            'unique': len({(d['ecosystem'], d['name']) for d in deps}),
            'by_ecosystem': {
                e: sum(1 for d in deps if d['ecosystem'] == e)
                for e in sorted({d['ecosystem'] for d in deps})
            },
            'list': deps[:500],
        },
        'owasp_top10': {
            'total_findings': owasp_total,
            'files_with_findings': len(owasp_files),
            'severity': severity_counts([f for v in owasp.values() for f in v]),
            'categories': {
                cat: {'count': len(v), 'findings': v[:25]}
                for cat, v in sorted(owasp.items())
            },
        },
        'owasp_llm_top10': {
            'total_findings': llm_total,
            'files_with_findings': len(llm_files),
            'severity': severity_counts([f for v in llm.values() for f in v]),
            'categories': {
                cat: {'count': len(v), 'findings': v[:25]}
                for cat, v in sorted(llm.items())
            },
        },
        'sbom': make_sbom(name, GIT['head'][:12] or 'unknown', all_files, deps),
    }
    return report


def main(argv=None):
    ap = argparse.ArgumentParser(
        description='Static-analysis benchmark for cloned Anticloud projects.')
    ap.add_argument('repo', help='path to the cloned repository (UPSTREAM_CLONE)')
    ap.add_argument('-o', '--out', help='write the report JSON here')
    ap.add_argument('-n', '--name', help='project name for the report')
    ap.add_argument('--sbom-out', help='write the CycloneDX SBOM separately')
    ap.add_argument('--quiet', action='store_true')
    args = ap.parse_args(argv)

    t0 = time.time()
    report = analyse(args.repo, args.name)
    report['elapsed_seconds'] = round(time.time() - t0, 2)
    payload = json.dumps(report, indent=2, default=str)

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload + '\n', encoding='utf-8')
    else:
        print(payload)

    if args.sbom_out:
        sb = Path(args.sbom_out)
        sb.parent.mkdir(parents=True, exist_ok=True)
        sb.write_text(json.dumps(report['sbom'], indent=2) + '\n', encoding='utf-8')

    if not args.quiet:
        print(
            f"{report['project']}: "
            f"{report['metrics']['files_total']} files, "
            f"{report['metrics']['lines_of_code']} LOC, "
            f"licence={report['licence']['spdx']}({report['licence']['class']}), "
            f"deps={report['dependencies']['unique']}, "
            f"owasp={report['owasp_top10']['total_findings']} "
            f"llm={report['owasp_llm_top10']['total_findings']} "
            f"in {report['elapsed_seconds']}s",
            file=sys.stderr,
        )
    return 0


if __name__ == '__main__':
    raise SystemExit(main())