## 2024-09-09 - Hardcoded Django Secrets in Settings
**Vulnerability:** Django settings including `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `videodownloader_project/settings.py`.
**Learning:** Hardcoding secrets exposes sensitive configuration, making the application vulnerable to various attacks if the source code is compromised.
**Prevention:** Use environment variables (e.g., `os.environ.get`) to inject sensitive configuration values, providing safe defaults for local development environments to avoid breaking them.