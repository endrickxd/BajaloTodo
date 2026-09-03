## 2024-09-03 - Hardcoded Django Secrets
**Vulnerability:** Hardcoded SECRET_KEY, DEBUG=True, and ALLOWED_HOSTS=['*'] in settings.py.
**Learning:** Default Django setup generates a settings file with hardcoded secrets, which is unsafe for production environments. Fallbacks must be used to preserve local functionality while securing the app.
**Prevention:** Use environment variables (e.g., os.environ.get) for configuration settings like SECRET_KEY, DEBUG, and ALLOWED_HOSTS from the beginning.
