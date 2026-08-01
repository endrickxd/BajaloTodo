## 2024-08-01 - [CRITICAL] Fix Hardcoded Django SECRET_KEY
**Vulnerability:** Hardcoded Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` found in `videodownloader_project/settings.py`. These settings can be dangerous if left in production environments as they expose the application to malicious activities (like session hijacking, debug info leak).
**Learning:** Development environments often hardcode sensitive configuration inside `settings.py` files for ease of testing.
**Prevention:** Always read security-sensitive configuration from environment variables (e.g., using `os.environ.get()`), using safe defaults as fallback only in strictly controlled contexts like local development/testing.
