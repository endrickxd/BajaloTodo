## 2024-10-27 - Secure Django Settings
**Vulnerability:** Hardcoded Django secrets (SECRET_KEY), hardcoded debug mode on (DEBUG=True) and permissive allowed hosts in settings.py which can lead to data leaks and RCE in production.
**Learning:** Hardcoded configuration variables should never be deployed to production, but just deleting them can crash local environments if proper `.env` support isn't present in the tooling.
**Prevention:** Always use environment variables for sensitive settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` using tools like `os.environ.get()` with safe fallbacks for local dev until full secret management is built out.
