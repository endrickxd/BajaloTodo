## 2025-02-13 - [Securing Django Settings]
**Vulnerability:** Hardcoded `SECRET_KEY`, `DEBUG = True`, and `ALLOWED_HOSTS = ['*']` in production settings.
**Learning:** Hardcoding secrets and debug settings in version control exposes the application to severe attacks, including session hijacking and arbitrary code execution.
**Prevention:** Use environment variables (e.g., `os.environ.get()`) to manage sensitive configurations and debug states, providing safe fallbacks for local development to prevent breaking tests.
