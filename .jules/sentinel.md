## 2025-01-20 - [Fix hardcoded Django settings]
**Vulnerability:** Hardcoded `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were found in `videodownloader_project/settings.py`. Exposing the secret key allows attackers to forge sessions, while hardcoded `DEBUG=True` risks exposing internal application structure/stack traces, and `ALLOWED_HOSTS=['*']` permits Host header attacks.
**Learning:** Hardcoded configuration values can pose a critical security risk when code is published publicly or accessed via unauthorized means.
**Prevention:** Use environment variables (via `os.environ.get()`) to manage configuration settings, defaulting to secure local overrides for development and testing without affecting production.
