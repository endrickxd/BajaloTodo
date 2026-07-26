## 2024-05-24 - Hardcoded Django Secret Key
**Vulnerability:** Hardcoded Django SECRET_KEY and insecure default DEBUG and ALLOWED_HOSTS in settings.py.
**Learning:** Hardcoded secrets in version control can lead to full application compromise (e.g. session hijacking).
**Prevention:** Always load secrets via environment variables and ensure DEBUG is False by default in production.
