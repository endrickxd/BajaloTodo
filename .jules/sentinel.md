## 2024-05-19 - [Hardcoded Django Settings]
**Vulnerability:** Django settings `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `settings.py`, risking sensitive credential leakage, debug information disclosure in production, and inadequate host validation.
**Learning:** Hardcoded credentials and debug settings must be avoided, even in initial configuration files, as they frequently get committed to source control. They should be configurable through the environment.
**Prevention:** Use environment variables (e.g., `os.environ.get()`) to manage sensitive settings, falling back to safe local defaults only when appropriate.
