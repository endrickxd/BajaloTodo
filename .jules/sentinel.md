## 2024-09-18 - Hardcoded Django Configuration Secrets
**Vulnerability:** Critical Django settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `videodownloader_project/settings.py`. This exposes sensitive keys to version control and risks deploying with `DEBUG=True` in production.
**Learning:** Even in non-production codebases, hardcoded configuration values represent a significant vulnerability. We must use environment variables to inject secrets, while providing functional fallbacks for local development testing (`os.environ.get('KEY', 'fallback')`).
**Prevention:** Configure project scaffolding tools to automatically generate settings files that read from the environment or `.env` files by default. Avoid committing raw configuration values to Git.
