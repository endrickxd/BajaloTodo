## 2026-09-06 - Secure Hardcoded Django Settings
**Vulnerability:** Django settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded directly in `videodownloader_project/settings.py`.
**Learning:** Hardcoded configuration settings can leak sensitive data (e.g., SECRET_KEY) or allow dangerous misconfigurations in production environments (e.g., DEBUG=True, ALLOWED_HOSTS=['*']). Leaving these hardcoded prevents dynamic configuration in different environments (like production versus development).
**Prevention:** Use environment variables (via `os.environ.get`) for sensitive configuration options to ensure secrets and environment-specific settings are injected safely rather than stored directly in the repository.
