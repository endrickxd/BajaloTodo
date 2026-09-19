## 2024-05-18 - Hardcoded Django Security Settings
**Vulnerability:** Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `videodownloader_project/settings.py`, exposing secrets and potentially leaving debug mode on in production.
**Learning:** Security settings like secrets and flags controlling debug behavior need to be read from the environment rather than being stored in source code. Fallbacks are kept to allow for local development.
**Prevention:** Always use `os.environ.get()` for sensitive configuration variables and add sensible fallbacks if needed for local non-production environments.
