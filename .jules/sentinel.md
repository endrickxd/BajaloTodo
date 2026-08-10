## 2024-05-18 - Hardcoded Django Settings
**Vulnerability:** Django `settings.py` contained hardcoded `SECRET_KEY`, `DEBUG = True`, and `ALLOWED_HOSTS = ["*"]` which could lead to severe security compromises if deployed to production as-is.
**Learning:** Legacy or rapid-prototyped Django projects often commit standard development settings. These must be converted to use environment variables to allow secure production deployments while providing fallbacks for seamless local development.
**Prevention:** Implement the 12-factor app methodology for configuration by using `os.environ.get()` for all sensitive settings early in the project lifecycle.
