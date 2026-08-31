## 2024-05-15 - Django Hardcoded Secrets Extracted
**Vulnerability:** Django's `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `settings.py`, risking exposure of the secret key in version control and preventing secure environment-specific configuration (like disabling DEBUG in production).
**Learning:** Even simple default Django installations often commit these keys by default. When remediating, it's vital to use `os.environ.get()` with the original hardcoded values as defaults to avoid breaking existing local development environments.
**Prevention:** Always initialize Django settings with environment variable wrappers (`os.environ.get()` or libraries like `environ` / `python-decouple`) immediately upon project creation.
