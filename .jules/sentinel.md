
## 2024-05-18 - Hardcoded Django Secrets
**Vulnerability:** Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `settings.py`.
**Learning:** Hardcoding sensitive configuration like `SECRET_KEY` makes it possible to hijack sessions or tamper with cryptographic signatures. Hardcoding `DEBUG=True` in a public repository can lead to stack trace leaks if deployed directly.
**Prevention:** Always use environment variables (`os.environ.get()`) to load sensitive application configuration.
