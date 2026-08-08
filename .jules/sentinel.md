## 2026-08-08 - Securing Django Settings
**Vulnerability:** Hardcoded Django `SECRET_KEY`, `DEBUG=True`, and `ALLOWED_HOSTS=['*']` in `settings.py`.
**Learning:** Found these settings hardcoded which is a critical risk in production deployment as it can expose secrets, lead to code execution via debug pages, and host header injection. It is safe to fix this by introducing `os.environ.get()` with the original hardcoded values as fallback to avoid breaking local dev.
**Prevention:** Always load sensitive settings and environment-specific toggles from environment variables instead of hardcoding them in `settings.py`.
