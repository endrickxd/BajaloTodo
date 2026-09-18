## 2026-09-18 - Django Config Security Enhancement
**Vulnerability:** Hardcoded `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` in Django settings.
**Learning:** Found critical configurations hardcoded in `settings.py`. This introduces severe security risks when deployed to production, especially with `DEBUG = True` which can leak sensitive stack traces and `ALLOWED_HOSTS = ['*']` which opens up the app to Host header attacks.
**Prevention:** Always use environment variables for sensitive settings like `SECRET_KEY` and deployment-specific flags like `DEBUG` and `ALLOWED_HOSTS`. Ensure the code falls back to sensible defaults for local development to prevent breaking test environments.
