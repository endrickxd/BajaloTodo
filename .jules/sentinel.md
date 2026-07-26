## 2024-05-24 - Fix Hardcoded Django SECRET_KEY and DEBUG Mode
**Vulnerability:** Hardcoded Django `SECRET_KEY` in `settings.py` and `DEBUG = True` enabled.
**Learning:** Hardcoded secrets in version control can lead to session hijacking and cryptographic bypass. `DEBUG = True` in production leaks sensitive environment and stack trace details to end users.
**Prevention:** Use environment variables (e.g., `os.environ`) for secrets and configuration flags, ensuring they are injected securely at runtime.
