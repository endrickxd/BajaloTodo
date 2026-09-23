## 2024-09-23 - Hardcoded Secrets in Django Settings
**Vulnerability:** Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` values are hardcoded in `videodownloader_project/settings.py`.
**Learning:** Hardcoded configuration parameters can lead to immediate security compromises, especially if the repository becomes public or is accessed by unauthorized users. Hardcoding debug mode to true risks exposing application errors and sensitive information to users.
**Prevention:** Use environment variables (via `os.environ.get()`) combined with sensible local fallback defaults to secure these settings without breaking local development environments.
