import base64
import os
import json
import time
from cryptography.hazmat.primitives.asymmetric import ed25519

# === 1. Przygotuj klucz prywatny komisji ===
private_key = ed25519.Ed25519PrivateKey.generate()

# === 2. Funkcja generująca zawartość QR kodu (token + podpis) ===
def generate_token_payload():
    token_bytes = os.urandom(32)  # 256-bit token
    token_b64 = base64.urlsafe_b64encode(token_bytes).decode('utf-8')

    signature = private_key.sign(token_bytes)
    signature_b64 = base64.urlsafe_b64encode(signature).decode('utf-8')

    payload = {
        "token": token_b64,
        "sig": signature_b64
    }

    return json.dumps(payload, separators=(',', ':'))

# === 3. Benchmark ===
def benchmark(count: int):
    start = time.perf_counter()
    for _ in range(count):
        _ = generate_token_payload()
    end = time.perf_counter()

    duration = end - start
    print(f"Wygenerowano {count} tokenów w {duration:.2f} sekundy")
    print(f"{count / duration:.2f} tokenów na sekundę")

# === 4. Uruchom benchmark dla np. 100_000 tokenów ===
if __name__ == "__main__":
    benchmark(100_000)

