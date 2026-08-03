## 2024-08-03 - [Secure Django Settings]
**Vulnerability:** Hardcoded Django `SECRET_KEY`, `DEBUG=True`, and `ALLOWED_HOSTS=['*']` in settings.py.
**Learning:** These settings are often left hardcoded for local development convenience but expose applications in production.
**Prevention:** Use environment variables `os.environ.get()` with fallbacks to secure production without breaking local development.
