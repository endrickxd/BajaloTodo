## 2025-01-28 - Hardcoded Django Secrets

**Vulnerability:** Django settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded directly in the codebase. This poses a critical security risk because sensitive secrets could be exposed publicly if the code is shared, leading to potential exploits, and running with debug enabled in production environments exposes stack traces.

**Learning:** Important settings required for the security of a Django application should never be hardcoded into version-controlled files. They need to be provided via environment variables at runtime or via secured configurations. When converting to environment variables, provide the existing hardcoded values as fallback options to avoid breaking local development environments.

**Prevention:** Use `os.environ.get()` to load the necessary configurations (e.g. `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS`) dynamically. Example: `SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'default-dev-key')`.
