## 2026-08-25 - Hardcoded Django settings
**Vulnerability:** Django SECRET_KEY, DEBUG, and ALLOWED_HOSTS were hardcoded in settings.py, risking exposure of sensitive configurations.
**Learning:** Hardcoded credentials in source control make them easily accessible to anyone with repository access and difficult to rotate securely.
**Prevention:** Use environment variables via `os.environ.get()` to manage sensitive configurations, with secure fallbacks only for local development.
