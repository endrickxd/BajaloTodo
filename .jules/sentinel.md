## 2024-08-14 - Hardcoded Django Secrets
**Vulnerability:** Django settings (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`) were hardcoded in `settings.py`, risking exposure of sensitive keys in version control and enabling dangerous debug mode in production.
**Learning:** Fixing hardcoded configurations requires balancing security with usability; completely removing fallbacks can break existing local development environments.
**Prevention:** Always pull sensitive values and environment-specific toggles from environment variables (e.g., `os.environ.get()`), using safe defaults or existing hardcoded values as fallbacks *only* to preserve local development continuity while production relies on the secure variables.
