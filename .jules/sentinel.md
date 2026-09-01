## 2024-05-21 - Hardcoded Django Secrets
**Vulnerability:** Hardcoded Django secrets (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`) in settings.py.
**Learning:** These variables control application security and should not be hardcoded in version control, as they can expose signing keys or cause data leakage if deployed with `DEBUG=True`.
**Prevention:** Use environment variables (e.g., `os.environ.get()`) to manage sensitive settings, and provide safe defaults for local development.
