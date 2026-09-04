## 2024-03-24 - [Fix Hardcoded Secrets]
**Vulnerability:** Django settings.py contains hardcoded `SECRET_KEY`, `DEBUG = True`, and `ALLOWED_HOSTS = ['*']`. This exposes the application to severe risks including session hijacking, remote code execution (via DEBUG info leaks), and host header injection.
**Learning:** Hardcoded sensitive configuration in settings files is a common pattern that risks being committed to version control.
**Prevention:** Use environment variables (e.g., `os.environ.get()`) to manage sensitive settings, providing the hardcoded values as fallback to avoid breaking local development environments.
