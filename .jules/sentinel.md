
## 2024-10-22 - Secure Django Configuration Loading
**Vulnerability:** Django `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` settings were hardcoded in `settings.py`, risking sensitive credential exposure and insecure configurations in production.
**Learning:** Hardcoded configuration settings often persist because they're convenient during development, but they represent a critical vulnerability if pushed to a public repository or deployed to production without modification.
**Prevention:** Always use environment variables (e.g., `os.environ.get()`) to manage sensitive Django settings, providing safe defaults for local development environments without compromising production security.
