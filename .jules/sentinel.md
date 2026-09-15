## 2024-09-15 - [Hardcoded Django Secrets]
**Vulnerability:** Django settings file (videodownloader_project/settings.py) contained hardcoded `SECRET_KEY`, `DEBUG = True`, and wildcard `ALLOWED_HOSTS`.
**Learning:** These settings are often hardcoded during initial development, leading to potential production exposure (stack traces, Host header attacks) if not properly managed before deployment.
**Prevention:** Use environment variables (via `os.environ.get`) to securely manage sensitive settings in production while retaining safe fallback defaults for local development.
