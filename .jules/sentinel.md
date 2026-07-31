## 2024-05-18 - Hardcoded Django Secrets in Settings
**Vulnerability:** Django settings `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `settings.py`. This is a critical security vulnerability as it risks exposing secret keys and enabling debug mode in production, potentially leaking sensitive application data and architecture details.
**Learning:** Hardcoding secrets is a common mistake when prototyping Django applications. It's crucial to always configure Django to read sensitive settings from environment variables before pushing to production or sharing code.
**Prevention:** Use `os.environ.get()` with safe fallbacks for local development, and ensure production environments inject these secrets securely via environment variables.
