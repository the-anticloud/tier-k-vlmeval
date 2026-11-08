"""
Anticloud Zero-Trust Local Mesh
mTLS between all components even on localhost.
Self-signed CA + per-service short-lived certs.
No cloud PKI. Works air-gapped.
"""
import datetime, ipaddress, os, socket
from pathlib import Path
from typing import Optional, Tuple

try:
    from cryptography import x509
    from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.backends import default_backend
    CRYPTO_OK = True
except ImportError:
    CRYPTO_OK = False


def _require_crypto():
    if not CRYPTO_OK:
        raise ImportError("pip install cryptography")


def generate_ca(ca_dir: str) -> Tuple[str, str]:
    """Generate self-signed CA cert + key. Returns (cert_path, key_path)."""
    _require_crypto()
    ca_dir = Path(ca_dir)
    ca_dir.mkdir(parents=True, exist_ok=True)
    cert_path = ca_dir / "ca.crt"
    key_path  = ca_dir / "ca.key"
    if cert_path.exists() and key_path.exists():
        return str(cert_path), str(key_path)

    key = rsa.generate_private_key(public_exponent=65537, key_size=4096,
                                    backend=default_backend())
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Anticloud FZ LLE"),
        x509.NameAttribute(NameOID.COMMON_NAME, "Anticloud Local CA"),
    ])
    now = datetime.datetime.utcnow()
    cert = (x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + datetime.timedelta(days=3650))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .sign(key, hashes.SHA256(), default_backend()))

    cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    key_path.write_bytes(key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.TraditionalOpenSSL,
        serialization.NoEncryption()))
    return str(cert_path), str(key_path)


def issue_service_cert(service_name: str, ca_dir: str, out_dir: str,
                        ttl_days: int = 1) -> Tuple[str, str]:
    """Issue a short-lived cert for a service, signed by local CA."""
    _require_crypto()
    ca_cert_path, ca_key_path = generate_ca(ca_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    cert_path = out_dir / f"{service_name}.crt"
    key_path  = out_dir / f"{service_name}.key"

    with open(ca_cert_path, "rb") as f:
        ca_cert = x509.load_pem_x509_certificate(f.read(), default_backend())
    with open(ca_key_path, "rb") as f:
        ca_key = serialization.load_pem_private_key(f.read(), None, default_backend())

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048,
                                    backend=default_backend())
    subject = x509.Name([
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Anticloud FZ LLE"),
        x509.NameAttribute(NameOID.COMMON_NAME, service_name),
    ])
    now = datetime.datetime.utcnow()
    san = x509.SubjectAlternativeName([
        x509.DNSName("localhost"),
        x509.DNSName(socket.gethostname()),
        x509.IPAddress(ipaddress.IPv4Address("127.0.0.1")),
    ])
    cert = (x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(ca_cert.subject)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + datetime.timedelta(days=ttl_days))
        .add_extension(san, critical=False)
        .add_extension(
            x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH,
                                    ExtendedKeyUsageOID.CLIENT_AUTH]),
            critical=False)
        .sign(ca_key, hashes.SHA256(), default_backend()))

    cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    key_path.write_bytes(key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.TraditionalOpenSSL,
        serialization.NoEncryption()))
    return str(cert_path), str(key_path)


def get_ssl_context(cert_path: str, key_path: str, ca_cert_path: str,
                     server_side: bool = True):
    """Return configured ssl.SSLContext for mTLS."""
    import ssl
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER if server_side else ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_cert_chain(cert_path, key_path)
    ctx.load_verify_locations(ca_cert_path)
    ctx.verify_mode = ssl.CERT_REQUIRED
    if not server_side:
        ctx.check_hostname = False
    return ctx


def cert_fingerprint(cert_path: str) -> str:
    """SHA-256 fingerprint of a PEM cert for pinning."""
    import ssl, hashlib
    _require_crypto()
    with open(cert_path, "rb") as f:
        cert = x509.load_pem_x509_certificate(f.read(), default_backend())
    return cert.fingerprint(hashes.SHA256()).hex()
