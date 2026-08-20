## 2024-08-20 - [Hardcoded Secrets & Insecure Defaults in Django Settings]
**Vulnerability:** Django settings `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded with insecure values (`DEBUG = True`, `ALLOWED_HOSTS = ['*']`).
**Learning:** Hardcoding secrets and debug flags in settings files can lead to data exposure and compromise in production environments if not overridden.
**Prevention:** Always use environment variables (`os.environ.get()`) to manage sensitive settings and configuration flags, providing safe fallbacks for local development.
