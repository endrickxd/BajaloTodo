## 2024-08-11 - [Secure Django Settings]
**Vulnerability:** Hardcoded `SECRET_KEY`, `DEBUG = True`, and `ALLOWED_HOSTS = ['*']` in `settings.py`.
**Learning:** Default Django projects often have hardcoded secrets and insecure settings for production, which can lead to session hijacking, remote code execution (RCE) via debug pages, and host header injection attacks.
**Prevention:** Use environment variables for sensitive settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` with safe fallbacks for local development.
