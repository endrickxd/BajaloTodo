## 2024-08-13 - [Secure Django Configuration]
**Vulnerability:** Hardcoded `SECRET_KEY`, `DEBUG = True`, and `ALLOWED_HOSTS = ['*']` in `settings.py`.
**Learning:** Hardcoding sensitive configuration variables in the repository exposes the application to severe security risks (e.g., unauthorized access, data breaches, and detailed error information leakage in production).
**Prevention:** Use environment variables (e.g., `os.environ.get()`) to manage sensitive configurations and provide safe fallbacks for local development to prevent breaking the application while securing production environments.
