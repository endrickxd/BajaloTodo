## 2024-08-20 - Hardcoded Django Secrets in Settings
**Vulnerability:** Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded directly in `settings.py`.
**Learning:** Hardcoded configuration settings expose sensitive application information and debugging capabilities in the source code.
**Prevention:** Always use environment variables for sensitive settings (`os.environ.get()`), maintaining fallback values to ensure local development environments do not break.
