## 2024-05-24 - [CRITICAL] Hardcoded SECRET_KEY in Django settings
**Vulnerability:** The Django SECRET_KEY is hardcoded in the codebase.
**Learning:** Hardcoding secrets exposes the application to security risks. The SECRET_KEY in Django is used for cryptographic signing, so exposing it is critical.
**Prevention:** Use environment variables and `os.environ.get()` to store and fetch sensitive keys like `SECRET_KEY`.
