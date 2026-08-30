## 2024-05-15 - Hardcoded Secrets in Django Settings
**Vulnerability:** Django settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded with sensitive/insecure defaults, increasing the risk of secrets leaking or the application being run in an insecure state in production.
**Learning:** Default Django projects start with hardcoded settings, which can easily end up in version control if not actively secured.
**Prevention:** Use environment variables (`os.environ.get`) in `settings.py` to allow the deployment environment to inject secure configurations. Keep local development defaults as fallbacks so local environments don't break.
