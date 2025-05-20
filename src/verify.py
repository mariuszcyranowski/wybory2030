from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import base64
import json

# Wczytaj klucz publiczny komisji
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Wczytaj dane z QR (np. ze stringa)
data = json.loads(qr_content)
token_bytes = base64.urlsafe_b64decode(data["token"])
signature_bytes = base64.urlsafe_b64decode(data["sig"])

try:
    public_key.verify(signature_bytes, token_bytes)
    print("✅ Podpis poprawny – token autentyczny.")
except Exception as e:
    print("❌ Nieprawidłowy podpis – odrzuć token.")

