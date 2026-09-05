## 2025-03-05 - Insecure Hardcoded Django Settings
**Vulnerability:** Django settings including `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded with insecure development values in `settings.py`.
**Learning:** Hardcoding sensitive settings directly in version control exposes the application to severe risks, such as session hijacking or remote code execution, if the repository is compromised. Keeping `DEBUG=True` in production can leak sensitive configuration data through error pages.
**Prevention:** Always externalize configuration using environment variables for sensitive settings like `SECRET_KEY`, `DEBUG`, and database credentials. Provide fallbacks to development defaults only to maintain local workflow integrity while enforcing secure overrides in production environments.
