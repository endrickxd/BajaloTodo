## 2024-06-25 - Hardcoded Django Secrets in Settings
**Vulnerability:** Found hardcoded Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` configurations directly in `videodownloader_project/settings.py`.
**Learning:** Hardcoding secrets exposes the application to compromise if the source code repository is accessed by unauthorized individuals. It also couples environment-specific settings to the codebase, making secure deployments to production environments difficult.
**Prevention:** Always load sensitive configurations like `SECRET_KEY` and environment-specific settings like `DEBUG` and `ALLOWED_HOSTS` from environment variables, providing secure fallbacks for local development where necessary, keeping secrets out of version control.
