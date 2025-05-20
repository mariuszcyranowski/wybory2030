# Wybory 2030 – Bezpieczne głosowanie z użyciem tokenów QR i blockchaina

Projekt demonstruje bezpieczny i anonimowy protokół głosowania oparty o:

- Jednorazowe tokeny zakodowane w kodach QR
- Podpis cyfrowy (Ed25519)
- Możliwość weryfikacji głosu przez wyborcę dzięki rejestrowi blockchain

## 🧩 Struktura projektu

```shell
.
├── private_key.pem                      # Klucz prywatny komisji wyborczej (do podpisywania tokenów)
├── public_key.pem                       # Klucz publiczny (do weryfikacji tokenów)
├── requirements.txt                     # Lista zależności Pythona
├── token_qr.png                         # Przykładowy kod QR z tokenem
├── Wybory 2030 - Proces głosowania.svg  # Diagram procesu głosowania
└── src/
   ├── generate.py                       # Generator tokenów QR + benchmark wydajności
   └── verify.py                         # Weryfikacja podpisanego tokena
```

## 🔐 Zasada działania

1. **Losowy token (256 bitów)** generowany jest w sposób bezpieczny kryptograficznie.
2. Token jest podpisywany cyfrowo przez komisję wyborczą (kluczem prywatnym Ed25519).
3. Zakodowany token + podpis trafiają do kodu QR w formacie JSON.
4. Terminal głosujący weryfikuje podpis używając klucza publicznego.
5. Wyborca oddaje głos anonimowo – głos wraz z hashem trafia do blockchaina.

## 📷 Grafiki

### Proces głosowania

![Diagram procesu głosowania](Wybory%202030%20-%20Proces%20g%C5%82osowania.svg)

### Przykładowy kod QR tokenu

```json
{"token":"xZhzKyXMOIKROnFpY9YlFxpVjlBbkiZ6JRF-F60tNKE=","sig":"O6oTJ-aoaMCzvdBmh52ESOL-8EI-VO7MTcOorG0GhAdrNTHHS0f6PzZUVQZuLf0vzGEBXwkzuxecJWAIhEidAg=="}
```

![Kod QR tokenu](token_qr.png)

## ▶️ Uruchomienie

1. Stwórz środowisko virtualne i zainstaluj zależności:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Wygeneruj i przetestuj tokeny:

   ```bash
   python src/generate.py
   ```

3. Zweryfikuj podpisany token:

   ```bash
   python src/verify.py
   ```

## 📄 Licencja

MIT – możesz swobodnie używać, modyfikować i wdrażać koncepcję w zastosowaniach demonstracyjnych i badawczych.

---

> Projekt edukacyjny mający na celu zaprezentowanie możliwości zastosowania podpisów cyfrowych i QR kodów w nowoczesnych systemach głosowania.