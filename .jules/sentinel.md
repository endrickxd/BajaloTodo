## 2025-02-27 - Hardcoded Django Secrets in Settings
**Vulnerability:** Django settings `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `videodownloader_project/settings.py`, exposing sensitive data and allowing debugging in production environments if the file was pushed as is.
**Learning:** Hardcoded configuration variables pose a significant security risk, especially in production environments. We must rely on environment variables to inject sensitive and environment-specific configuration securely.
**Prevention:** Use `os.environ.get()` to load configuration variables such as `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` securely via environment variables while keeping local testing fallbacks.
