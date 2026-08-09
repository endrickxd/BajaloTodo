## 2024-05-18 - Hardcoded Django Secrets
**Vulnerability:** Django `SECRET_KEY`, `DEBUG = True`, and `ALLOWED_HOSTS = ["*"]` were hardcoded in `settings.py`.
**Learning:** These settings are often hardcoded for local development ease, but when pushed to production, they lead to critical vulnerabilities, such as exposing debug information and session hijacking risks. We secured this using environment variables with local fallbacks.
**Prevention:** Use `os.environ.get()` with safe fallbacks during development for sensitive configurations to prevent accidental deployment with hardcoded values.
