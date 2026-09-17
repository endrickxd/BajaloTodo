## 2024-03-24 - [Fix hardcoded Django secrets]
**Vulnerability:** Hardcoded `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` in `videodownloader_project/settings.py`.
**Learning:** Found insecure default configuration in Django settings that could lead to unauthorized access or data exposure if deployed as-is. Refactoring to use `os.environ.get()` with fallbacks mitigates this risk.
**Prevention:** Always use environment variables for sensitive settings in Django configurations.