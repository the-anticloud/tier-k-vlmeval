# K_VLMEVAL

## 1. WHAT — K_VLMEVAL (TIER_6_SECURITY_EVAL)
**Upstream pin:** `54a063c5bf75245c35599daab9826d0a5b8e2671` (GitHub API commits/main, unified 2026-10-15).

K_VLMEVAL is a first-party Anticloud component in TIER_6_SECURITY_EVAL. It is developed in this repository (no third-party upstream); the source of truth is the code in this directory.
Scanned source: 1627 code/text files, ~332693 lines. Dominant extensions: {'.md': 379, '.py': 1060, '.json': 155, '.toml': 1, '.yaml': 12, '.yml': 4, '.js': 8, '.sh': 8}.
Key entry points / manifests: pyproject.toml, anticloud\cli.py, src\k_vlmeval_anticloud\cli.py, UPSTREAM_CLONE\anticloud\cli.py.
Representative files:
- `00_README.md`
- `aioss_integration.py`
- `anticloud-edits.json`
- `BENCH.json`
- `bench_engine.py`
- `DATA_ROOM_INDEX.md`
- `LICENSE.md`
- `NOTICE.md`
- `pyproject.toml`
- `README.md`
- `sbom.cdx.json`
- `SECURITY_PATCHES.md`
- `01_INVESTOR_PACKAGE\CAP_TABLE.md`
- `01_INVESTOR_PACKAGE\FINANCIAL_MODEL.md`
- `01_INVESTOR_PACKAGE\GTM_STRATEGY.md`

## 2. INSTALL

```bash
# inspect source
ls "K_VLMEVAL"
pip install -e .
```

## 3. USE

```bash
python anticloud/cli.py --help
```

## 4. API

Top-level Python imports observed in source (first 60 lines per file):
- `from **lowest to highest**.`
- `from . import AggregationType, MetricType, ResponseParseType`
- `from . import build_dataset`
- `from . import puzzles`
- `from .. import conversation as conversation_lib`
- `from ....utils.mp_util import cpu_count as quota_cpu_count`
- `from ...smp.file import load`
- `from ..arguments import DataArguments`
- `from ..base import BaseModel`
- `from ..base_metric import BaseMetric`
- `from ..constants import (DEFAULT_IM_END_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_I`
- `from ..constants import DEFAULT_SPEECH_TOKEN, IGNORE_INDEX, IMAGE_TOKEN_INDEX, S`
- `from ..constants import IGNORE_INDEX`
- `from ..dataset import DATASET_MODALITY`
- `from ..dataset import DATASET_MODALITY, DATASET_TYPE`
- `from ..dataset import DATASET_TYPE`
- `from ..dataset.utils.chartmimic.evaluator.chart_type_evaluator import ChartTypeE`
- `from ..dataset.utils.chartmimic.evaluator.color_evaluator import ColorEvaluator`
- `from ..dataset.utils.chartmimic.evaluator.layout_evaluator import LayoutEvaluato`
- `from ..dataset.utils.chartmimic.evaluator.text_evaluator import TextEvaluator`

## 5. DEPENDENCIES

Extensions histogram: {".md": 379, ".py": 1060, ".json": 155, ".toml": 1, ".yaml": 12, ".yml": 4, ".js": 8, ".sh": 8}. Manifests detected: pyproject.toml, anticloud\cli.py, src\k_vlmeval_anticloud\cli.py, UPSTREAM_CLONE\anticloud\cli.py.

## 6. CONFIGURE

Environment variables and config files are read from source defaults; no mandatory external config was detected by the scan. Check the entry-point files above for env-var names. Common pattern: copy any `*.example` / `config.*` file next to the entry point and edit values.

## 7. CONTRIBUTING

First-party repo: open an issue describing the change, keep patches small, add/extend tests next to the module, and ensure the 16-check suite stays green before submitting.

## 8. LICENSE — Anticommons 0.1.0

This first-party component is released under the Anticommons 0.1.0 license. See LICENSE (or LICENCE) in the repository root; if absent, the Anticommons 0.1.0 terms apply as stated by the project owner.

## 9. UPSTREAM — first-party (no third-party upstream)

First-party Anticloud work: there is no third-party upstream clone for this project. Provenance is the local change history of this directory, not a pinned external SHA.

## 10. BENCHMARKS (from on-disk BENCH.json)

BENCH.json present on disk. Excerpt: `{"schema": "anticloud.tier-bench/1", "project": "K_VLMEVAL", "source": {"repo_path": "E:\\fenta\\Downloads\\The Anticloud\\TIER_6_SECURITY_EVAL\\K_VLMEVAL\\UPSTREAM_CLONE", "git": {"head": "", "url": "https://github.com/open-compass/VLMEvalKit", "branch": "master", "committed_at": "2026-09-29T11:06:59+04:00"}}, "metrics": {"files_total": 327, "source_files_scanned": 269, "lines_of_code": 88158, "languages": {".py": 267, ".md": 15, ".txt": 6, ".rst": 6, ".svg": 5, "(none)": 4, ".js": 4, ".sh": 4, ".yaml": 3, ".css": 3, ".json": 2, ".ipynb": 2, ".conf": 2, ".html": 2, ".cfg": 1}}, "licence": {"spdx": "Apache-2.0", "class": "A", "source_file": "LICENSE", "redistribution_allowed": true}, "dependencies": {"count": 3, "unique": 3, "by_ecosystem": {"pypi": 3}, "list": [{"ecosystem": "pypi", "name": "-r", "version": "", "source_file": "setup.py", "raw": "-r"}, {"ecosystem": "pypi", "name": "-e", "version": "", "source_file": "setup.py", "raw": "-e"}, {"ecosystem": "pypi", "name": "vlmutil", "version": "= vlmeval:cli", "source_file": "setup.py", "raw": "vlmutil = vlmeval:cli"}]}, "owasp_top10": {"total_findings": 106, "files_wit`
File/LOC scan at doc time: 1627 files, ~332693 lines. Result register (ISOLATED_LAB_RESULTS/03_Result_Register.md): present; anticloud/ overlay entries: 16; installer/ dir: present.

## Appendix — full scanned file list (evidence)

- `00_README.md`
- `aioss_integration.py`
- `anticloud-edits.json`
- `BENCH.json`
- `bench_engine.py`
- `DATA_ROOM_INDEX.md`
- `LICENSE.md`
- `NOTICE.md`
- `pyproject.toml`
- `README.md`
- `sbom.cdx.json`
- `SECURITY_PATCHES.md`
- `01_INVESTOR_PACKAGE\CAP_TABLE.md`
- `01_INVESTOR_PACKAGE\FINANCIAL_MODEL.md`
- `01_INVESTOR_PACKAGE\GTM_STRATEGY.md`
- `01_INVESTOR_PACKAGE\HIRING_PLAN.md`
- `01_INVESTOR_PACKAGE\IP_ASSIGNMENT.md`
- `01_INVESTOR_PACKAGE\USE_OF_FUNDS.md`
- `02_COMMITMENT_TO_SOCIETY\COMMITMENT_TO_SOCIETY.md`
- `03_COMMITMENT_TO_HUMANITY\COMMITMENT_TO_HUMANITY.md`
- `04_COMMITMENT_TO_ENVIRONMENT\COMMITMENT_TO_ENVIRONMENT.md`
- `05_COMMITMENTS_TO_PAST_PRESENT_FUTURE\COMMITMENTS_TO_PAST_PRESENT_FUTURE.md`
- `06_WHITELABELLING_AND_REPACKAGING\WHITELABELLING_AND_REPACKAGING.md`
- `07_ENTERPRISE_LICENSE_AND_PRICING\ENTERPRISE_LICENSE_AND_PRICING.md`
- `08_INTELLECTUAL_PROPERTY_AND_RIGHTS\INTELLECTUAL_PROPERTY_AND_RIGHTS.md`
- `09_COMPLIANCE\COMPLIANCE.md`
- `10_TECHNICAL_HANDOFF\TECHNICAL_HANDOFF.md`
- `11_TUTORIAL_DEVELOPERS\TUTORIAL_DEVELOPERS.md`
- `12_TUTORIAL_ENTERPRISE\TUTORIAL_ENTERPRISE.md`
- `13_TUTORIAL_USERS\TUTORIAL_USERS.md`
- `14_DEVELOPER_COOKBOOKS\DEVELOPER_COOKBOOKS.md`
- `15_DISASTER_RECOVERY\DISASTER_RECOVERY.md`
- `16_VULNERABILITY_MANAGEMENT\VULNERABILITY_MANAGEMENT.md`
- `17_HOW_TO_UPDATE\HOW_TO_UPDATE.md`
- `18_COMMAND_LINE_INTERFACE\COMMAND_LINE_INTERFACE.md`
- `19_SYSTEM_OF_THINGS_SOT\SYSTEM_OF_THINGS_SOT.md`
- `20_ACADEMIC_RESEARCH\ACADEMIC_RESEARCH.md`
- `21_RELATED_SCIENTIFIC_RESEARCH\RELATED_SCIENTIFIC_RESEARCH.md`
- `22_INDEPENDENT_INSURANCE\INDEPENDENT_INSURANCE.md`
- `23_HOW_TO_CITE\HOW_TO_CITE.md`
- `24_ANTICOMMONS_LICENSE\ANTICOMMONS_LICENSE.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\MILLENNIUM_PROBLEM_PROPOSALS.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\HQ_ARCHIVE\HQ_manifest.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P01\P01.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P01\P01.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P02\P02.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P02\P02.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P03\P03.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P03\P03.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P04\P04.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P04\P04.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P04\P04_HQ_solution.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P04\P04_HQ_solution.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P05\P05.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P05\P05.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P06\P06.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P06\P06.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P07\P07.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P07\P07.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P08\P08.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P08\P08.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P09\P09.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P09\P09.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P09\P09_HQ_solution.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P09\P09_HQ_solution.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P10\P10.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P10\P10.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P11\P11.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P11\P11.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P12\P12.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P12\P12.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P13\P13.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P13\P13.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P14\P14.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P14\P14.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P15\P15.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P15\P15.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P16\P16.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P16\P16.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P17\P17.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P17\P17.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P18\P18.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P18\P18.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P19\P19.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P19\P19.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P20\P20.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P20\P20.md`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P20\P20_HQ_solution.json`
- `25_MILLENNIUM_PROBLEM_PROPOSALS\P20\P20_HQ_solution.md`
- `26_INTEGRATIONS_AND_SDK\INTEGRATIONS_AND_SDK.md`
- `27_DEPENDENCIES\DEPENDENCIES.md`
- `28_TECHNICAL_WHITEPAPER\TECHNICAL_WHITEPAPER.md`
- `29_INVESTOR_MEMO\29_INVESTOR_MEMO.md`
- `30_LOI\ENTERPRISE_LOI.md`
- `30_LOI\GENERAL_LOI.md`
- `31_UNIT_ECONOMICS\31_UNIT_ECONOMICS.md`
- `32_CONTRACTS\CONTRACT_100M.md`
- `32_CONTRACTS\CONTRACT_10M.md`
- `32_CONTRACTS\CONTRACT_1M.md`
- `32_CONTRACTS\CONTRACT_5M.md`
- `32_CONTRACTS\CONTRACT_80M.md`
- `32_CONTRACTS\CONTRACT_8M.md`
- `33_COMPETITIVE_MOAT\33_COMPETITIVE_MOAT.md`
- `34_FOUNDER_PROFILE\FOUNDER_PROFILE.md`
- `35_INVESTOR_FAQ\INVESTOR_FAQ.md`
- `36_ADVISORY_BOARD\ADVISORY_BOARD.md`
- `ACADEMIC\01_Research_Use.md`
- `ACADEMIC\02_Method_And_Limitations.md`
- `anticloud\cli.py`
- `anticloud\crdt.py`
- `anticloud\observability.py`
- `anticloud\provenance.py`
- `anticloud\single_binary.py`
- `anticloud\sovereign_memory.py`
- `anticloud\zero_trust.py`
- `anticloud\_version.py`
- `anticloud\__init__.py`
- `anticloud\bench\compliance.py`
- `anticloud\bench\runner.py`
- `anticloud\bench\sbom.py`
- `anticloud\bench\__init__.py`
- `anticloud\crdt\convergence.py`
- `anticloud\crdt\gcounter.py`
- `anticloud\crdt\lww.py`
- `anticloud\crdt\orset.py`
- `anticloud\crdt\pncounter.py`
- `anticloud\crdt\__init__.py`
- `anticloud\deps\lock.py`
- `anticloud\deps\__init__.py`
- `anticloud\licence\classifier.py`
- `anticloud\licence\policy.py`
- `anticloud\licence\__init__.py`
- `anticloud\perf\harness.py`
- `anticloud\perf\__init__.py`
- `anticloud\provenance\chain.py`
- `anticloud\provenance\__init__.py`
- `anticloud\security\safeio.py`
- `anticloud\security\secrets.py`
- `anticloud\security\validators.py`
- `anticloud\security\vault.py`
- `anticloud\security\__init__.py`
- `APPENDIX\05_Plays_Well_With.md`
- `APPENDIX\06_System_Integration_Glimpses.md`
- `APPENDIX\07_Web_of_Relativity_This_Project.md`
- `BRANDING\brand.md`
- `COMMONS\01_OSS_License.md`
- `COMMONS\02_Contributor_Agreement.md`
- `COMMONS\03_Community_Standards.md`
- `COMMONS\COMMONS_LICENSE.md`
- `COMMONS\CONTRIBUTOR_GUIDE.md`
- `COMPLIANCE\01_Control_Mapping.md`
- `COMPLIANCE\02_SOC2_ISO27001_Readiness.md`
- `COMPLIANCE\03_Vulnerability_Management.md`
- `CONTRACTS\MSA\01_Master_Service_Agreement.md`
- `CONTRACTS\MSA\02_SLA_Addendum.md`
- `CONTRACTS\MSA\deployment_log_template.json`
- `CONTRACTS\MSA\DPA_TEMPLATE.md`
- `CONTRACTS\MSA\MASTER_SERVICE_AGREEMENT.md`
- `CONTRACTS\MSA\ORDER_FORM_TEMPLATE.md`
- `DEVELOPMENT\01_Build_And_Test.md`
- `DEVELOPMENT\02_Architecture.md`
- `DEVELOPMENT\03_Extension_Guide.md`
- `DEVELOPMENT\SCAFFOLD.md`
- `DEV_COOKBOOK\cookbook.md`
- `docs\00_README\README.md`
- `docs\01_INVESTOR_PACKAGE\README.md`
- `docs\02_COMMITMENT_TO_SOCIETY\README.md`
- `docs\03_COMMITMENT_TO_HUMANITY\README.md`
- `docs\04_COMMITMENT_TO_ENVIRONMENT\README.md`
- `docs\05_COMMITMENTS_TO_PAST_PRESENT_FUTURE\README.md`
- `docs\06_WHITELABELLING_AND_REPACKAGING\README.md`
- `docs\07_ENTERPRISE_LICENSE_AND_PRICING\README.md`
- `docs\08_INTELLECTUAL_PROPERTY_AND_RIGHTS\README.md`
- `docs\09_COMPLIANCE\README.md`
- `docs\10_TECHNICAL_HANDOFF\README.md`
- `docs\11_TUTORIAL_DEVELOPERS\README.md`
- `docs\12_TUTORIAL_ENTERPRISE\README.md`
- `docs\13_TUTORIAL_USERS\README.md`
- `docs\14_DEVELOPER_COOKBOOKS\README.md`
- `docs\15_DISASTER_RECOVERY\README.md`
- `docs\16_VULNERABILITY_MANAGEMENT\README.md`
- `docs\17_HOW_TO_UPDATE\README.md`
- `docs\18_COMMAND_LINE_INTERFACE\README.md`
- `docs\19_SYSTEM_OF_THINGS_SOT\README.md`
- `docs\20_ACADEMIC_RESEARCH\README.md`
- `docs\21_RELATED_SCIENTIFIC_RESEARCH\README.md`
- `docs\22_INDEPENDENT_INSURANCE\README.md`
- `docs\23_HOW_TO_CITE\README.md`
- `docs\24_ANTICOMMONS_LICENSE\README.md`
- `docs\25_MILLENNIUM_PROBLEM_PROPOSALS\README.md`
- `docs\26_INTEGRATIONS_AND_SDK\README.md`
- `docs\27_DEPENDENCIES\README.md`
- `docs\28_TECHNICAL_WHITEPAPER\README.md`
- `docs\29_INVESTOR_MEMO\README.md`
- `docs\30_LOI\README.md`
- `EDUCATORS\01_Classroom_Use.md`
- `EDUCATORS\02_Lab_Setup.md`
- `ENTERPRISE\01_Deployment.md`
- `ENTERPRISE\02_Integration.md`
- `ENTERPRISE_LICENSING\01_License_Agreement.md`
- `ENTERPRISE_LICENSING\02_Pricing_Sheet.md`
- `ENTERPRISE_LICENSING\03_Compliance_Checklist.md`
- `ENTERPRISE_LICENSING\COMPLIANCE.md`
- `ENTERPRISE_LICENSING\LICENSE_ENTERPRISE.md`
- `ENTERPRISE_LICENSING\PRICING.md`
- `Environment_Lab_Results\raw_metrics.json`
- `Environment_Lab_Results\README.md`
- `ETHICS\01_Epistemic_Gesturalism.md`
- `ETHICS\02_Positions_And_Basis.md`
- `FUNDING\01_Cost_Structure.md`
- `FUNDING\01_Funding_Brief.md`
- `FUNDING\02_Funding_Model.md`
- `FUTURES\01_Post_Quantum.md`
- `FUTURES\02_Post_Humanity.md`
- `GOVERNANCE\01_Decision_Rights.md`
- `GOVERNANCE\02_Change_Control.md`
- `II\01_Budget_Envelope.md`
- `II\02_Accounting_Outcomes.md`
- `II\03_Preprioception.md`
- `II\budget\ii_envelopes.json`
- `installer\license.md`
- `installer\loi.md`
- `installer\tauri.conf.json`
- `ISOLATED_LAB_RESULTS\01_Reproduction.md`
- `ISOLATED_LAB_RESULTS\02_Environment.md`
- `ISOLATED_LAB_RESULTS\03_Result_Register.md`
- `L5_L2_Classification\classification.md`
- `L5_L2_Classification\deploy_guide.md`
- `L5_L2_Classification\developer_cookbook.md`
- `L5_L2_Classification\HOW_TO_OPERATE.md`
- `L5_L2_Classification\HOW_TO_UPDATE.md`
- `L5_L2_Classification\PROTOCOLS.md`
- `LEDGERS\01_Ledger_Status.md`
- `LEDGERS\02_Export.md`
- `MARKETING\01_Positioning.md`
- `MARKETING\02_Competitive_Landscape.md`
- `MARKETING\03_Pricing_And_Competitors.md`
- `OFFICIAL_BENCHMARKS\01_FedRAMP.md`
- `OFFICIAL_BENCHMARKS\01_Index.md`
- `OFFICIAL_BENCHMARKS\02_OSINT.md`
- `OFFICIAL_BENCHMARKS\02_SOC2.md`
- `OFFICIAL_BENCHMARKS\03_OWASP.md`
- `OFFICIAL_BENCHMARKS\03_SOC1.md`
- `OFFICIAL_BENCHMARKS\04_COMPREHENSIVE_BENCHMARKS.json`
- `OFFICIAL_BENCHMARKS\04_COMPREHENSIVE_BENCHMARKS.md`
- `OFFICIAL_BENCHMARKS\04_PAX_Results.md`
- `OFFICIAL_BENCHMARKS\05_OWASP.md`
- `OFFICIAL_BENCHMARKS\06_CRDT.md`
- `OFFICIAL_BENCHMARKS\07_Provenance.md`
- `OFFICIAL_BENCHMARKS\08_ZeroTrust.md`
- `OFFICIAL_BENCHMARKS\09_Observability.md`
- `OFFICIAL_BENCHMARKS\10_SovereignMemory.md`
- `OFFICIAL_BENCHMARKS\11_DeterministicBuild.md`
- `OFFICIAL_BENCHMARKS\simulation_3seed.json`
- `OFFICIAL_BENCHMARKS\simulation_3seed.md`
- `OFFICIAL_BENCHMARKS\01_FedRAMP\01_FedRAMP.json`
- `OFFICIAL_BENCHMARKS\01_FedRAMP\01_FedRAMP.md`
- `OFFICIAL_BENCHMARKS\02_SOC2_TypeII\02_SOC2_TypeII.json`
- `OFFICIAL_BENCHMARKS\02_SOC2_TypeII\02_SOC2_TypeII.md`
- `OFFICIAL_BENCHMARKS\03_SOC1_TypeII\03_SOC1_TypeII.json`
- `OFFICIAL_BENCHMARKS\03_SOC1_TypeII\03_SOC1_TypeII.md`
- `OFFICIAL_BENCHMARKS\04_NIST_AI_RMF\04_NIST_AI_RMF.json`
- `OFFICIAL_BENCHMARKS\04_NIST_AI_RMF\04_NIST_AI_RMF.md`
- `OFFICIAL_BENCHMARKS\05_NIST_SP800_53\05_NIST_SP800_53.json`
- `OFFICIAL_BENCHMARKS\05_NIST_SP800_53\05_NIST_SP800_53.md`
- `OFFICIAL_BENCHMARKS\06_NIST_CSFW\06_NIST_CSFW.json`
- `OFFICIAL_BENCHMARKS\06_NIST_CSFW\06_NIST_CSFW.md`
- `OFFICIAL_BENCHMARKS\07_ISO_27001\07_ISO_27001.json`
- `OFFICIAL_BENCHMARKS\07_ISO_27001\07_ISO_27001.md`
- `OFFICIAL_BENCHMARKS\08_OWASP_LLM_Top10\08_OWASP_LLM_Top10.json`
- `OFFICIAL_BENCHMARKS\08_OWASP_LLM_Top10\08_OWASP_LLM_Top10.md`
- `OFFICIAL_BENCHMARKS\09_OWASP_Top10\09_OWASP_Top10.json`
- `OFFICIAL_BENCHMARKS\09_OWASP_Top10\09_OWASP_Top10.md`
- `OFFICIAL_BENCHMARKS\10_HIPAA\10_HIPAA.json`
- `OFFICIAL_BENCHMARKS\10_HIPAA\10_HIPAA.md`
- `OFFICIAL_BENCHMARKS\11_PCI_DSS\11_PCI_DSS.json`
- `OFFICIAL_BENCHMARKS\11_PCI_DSS\11_PCI_DSS.md`
- `OFFICIAL_BENCHMARKS\12_CMMC_2\12_CMMC_2.json`
- `OFFICIAL_BENCHMARKS\12_CMMC_2\12_CMMC_2.md`
- `OFFICIAL_BENCHMARKS\13_FISMA\13_FISMA.json`
- `OFFICIAL_BENCHMARKS\13_FISMA\13_FISMA.md`
- `OFFICIAL_BENCHMARKS\14_FIPS_140_3\14_FIPS_140_3.json`
- `OFFICIAL_BENCHMARKS\14_FIPS_140_3\14_FIPS_140_3.md`
- `OFFICIAL_BENCHMARKS\15_GDPR\15_GDPR.json`
- `OFFICIAL_BENCHMARKS\15_GDPR\15_GDPR.md`
- `OFFICIAL_BENCHMARKS\16_HITRUST_CSF\16_HITRUST_CSF.json`
- `OFFICIAL_BENCHMARKS\16_HITRUST_CSF\16_HITRUST_CSF.md`
- `OFFICIAL_BENCHMARKS\17_TISAX\17_TISAX.json`
- `OFFICIAL_BENCHMARKS\17_TISAX\17_TISAX.md`
- `OFFICIAL_BENCHMARKS\18_DORA\18_DORA.json`
- `OFFICIAL_BENCHMARKS\18_DORA\18_DORA.md`
- `OFFICIAL_BENCHMARKS\19_SOX_ITGC\19_SOX_ITGC.json`
- `OFFICIAL_BENCHMARKS\19_SOX_ITGC\19_SOX_ITGC.md`
- `OFFICIAL_BENCHMARKS\20_COBIT_2019\20_COBIT_2019.json`
- `OFFICIAL_BENCHMARKS\20_COBIT_2019\20_COBIT_2019.md`
- `OFFICIAL_BENCHMARKS\21_SLSA_L3\21_SLSA_L3.json`
- `OFFICIAL_BENCHMARKS\21_SLSA_L3\21_SLSA_L3.md`
- `OFFICIAL_BENCHMARKS\22_SSDF\22_SSDF.json`
- `OFFICIAL_BENCHMARKS\22_SSDF\22_SSDF.md`
- `OFFICIAL_BENCHMARKS\23_SBOM\23_SBOM.json`
