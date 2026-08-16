## 2023-10-27 - [Exposed Django settings]
**Vulnerability:** Hardcoded Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` values in `videodownloader_project/settings.py`.
**Learning:** Hardcoded configuration data leaves the application extremely vulnerable, primarily because the Django secret key can be used for session hijacking, cryptographic signing bypass, or even code execution in certain scenarios if leaked, while setting debug to true displays sensitive stack traces.
**Prevention:** Always use environment variables through `os.environ.get` for sensitive configurations like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` before committing.
