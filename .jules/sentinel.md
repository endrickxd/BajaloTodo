## 2024-07-28 - Hardcoded Django Secrets
**Vulnerability:** Django settings like SECRET_KEY, DEBUG, and ALLOWED_HOSTS were hardcoded in settings.py, which could expose sensitive data and debug information in a production environment.
**Learning:** It is crucial to manage configuration variables securely using environment variables, avoiding hardcoding them in version control.
**Prevention:** Always implement `os.environ.get()` with appropriate fallbacks to decouple configuration from code and enhance security.
