## 2024-06-03 - [Django Hardcoded Secrets]
**Vulnerability:** Django SECRET_KEY, DEBUG, and ALLOWED_HOSTS were hardcoded in settings.py, which is insecure for production environments.
**Learning:** Hardcoding sensitive configuration directly in settings files can lead to compromised secrets if the repository is exposed or if the code is deployed as-is.
**Prevention:** Always read sensitive configuration and environment-specific settings (like SECRET_KEY, DEBUG, ALLOWED_HOSTS) from environment variables using tools like `os.environ.get()` or libraries like `django-environ`, providing safe fallbacks for local development if necessary.
