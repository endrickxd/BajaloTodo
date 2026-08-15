## 2024-05-18 - [Django Settings Secure Configuration]
**Vulnerability:** Hardcoded Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` values in settings file.
**Learning:** Hardcoding security-sensitive settings exposes the application to risks if code is leaked or the environment changes.
**Prevention:** Always use environment variables to configure production secrets and environment-specific settings (like `DEBUG`), providing secure fallbacks for local development to maintain developer experience.
