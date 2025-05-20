import base64
import os
import qrcode
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

# === 1. Klucz prywatny komisji (wygeneruj raz i przechowuj bezpiecznie) ===
private_key = ed25519.Ed25519PrivateKey.generate()
public_key = private_key.public_key()

# Zapisz klucze do pliku (opcjonalnie)
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# === 2. Wygeneruj losowy token 256-bitowy ===
token_bytes = os.urandom(32)  # 256-bit
token_b64 = base64.urlsafe_b64encode(token_bytes).decode('utf-8')

# === 3. Podpisz token prywatnym kluczem ===
signature = private_key.sign(token_bytes)
signature_b64 = base64.urlsafe_b64encode(signature).decode('utf-8')

# === 4. Zakoduj jako JSON lub prosty ciąg (do QR) ===
payload = {
    "token": token_b64,
    "sig": signature_b64
}

# Dla uproszczenia jako string JSON:
import json
qr_content = json.dumps(payload, separators=(',', ':'))
print(qr_content)

# === 5. Wygeneruj QR kod ===
img = qrcode.make(qr_content)
img.save("token_qr.png")
print("QR kod zapisany jako token_qr.png")
