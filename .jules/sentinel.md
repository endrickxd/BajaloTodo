## 2026-08-07 - Hardcoded Django Settings
**Vulnerability:** Django settings file (settings.py) contained hardcoded SECRET_KEY, DEBUG = True, and ALLOWED_HOSTS = ['*'].
**Learning:** These settings, if deployed to production, represent a critical security risk (secret exposure, information leakage, and Host header injection). Fallbacks are necessary to not break local development.
**Prevention:** Always use environment variables (e.g., os.environ.get()) for sensitive or environment-specific configuration values in Django settings.
