## 2024-08-24 - [Critical] Hardcoded Django Secrets

**Vulnerability:** Django settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `settings.py`. This included `DEBUG = True` and `ALLOWED_HOSTS = ['*']` which are dangerous defaults for production.

**Learning:** Leaving Django default insecure configurations in place can lead to serious breaches, such as secret key exposure allowing session hijacking, and `DEBUG = True` leaking sensitive configuration data via stack traces.

**Prevention:** Always secure sensitive Django settings by loading them from environment variables (e.g., using `os.environ.get()`). Keep safe fallback defaults for local development to ensure it doesn't break environments unexpectdely.
