## 2024-11-20 - Hardcoded Django Secrets in Settings
**Vulnerability:** Django SECRET_KEY, DEBUG, and ALLOWED_HOSTS are hardcoded directly in `settings.py`.
**Learning:** This could accidentally commit production secrets to version control and allow execution of debug mode or any host in production if the file is deployed directly.
**Prevention:** Use environment variables with `os.environ.get()` and provide the previous hardcoded variables as fallbacks to ensure development and testing don't break.