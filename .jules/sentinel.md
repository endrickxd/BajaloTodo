## 2023-10-27 - [Django Settings Hardcoded Secrets]
**Vulnerability:** Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `settings.py`.
**Learning:** Hardcoding sensitive settings is a common pattern in initial Django setups but poses a critical risk if deployed to production, exposing the application to session hijacking and unauthorized host attacks.
**Prevention:** Always use environment variables (`os.environ.get`) for sensitive configuration variables in Django, providing safe local defaults to maintain a seamless development experience without compromising production security.
