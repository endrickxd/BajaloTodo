## 2024-05-18 - [Django Settings Hardcoded Secrets]
**Vulnerability:** Django settings file `settings.py` contained hardcoded `SECRET_KEY`, `DEBUG = True`, and `ALLOWED_HOSTS = ['*']`, exposing the application to severe risks if deployed to production.
**Learning:** Even though local development requires easy-to-use defaults, production environments must be able to inject secure configuration securely without modifying the codebase.
**Prevention:** Always use environment variables (`os.environ.get`) for sensitive configuration in Django settings, using the insecure hardcoded values as local development fallbacks.
