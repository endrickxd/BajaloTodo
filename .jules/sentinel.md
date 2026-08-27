## 2024-10-18 - [Fix Hardcoded Secrets in Django Settings]
**Vulnerability:** Django settings `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded with insecure or overly permissive values (`DEBUG=True`, `ALLOWED_HOSTS=['*']`).
**Learning:** Hardcoding sensitive or environment-specific values in configuration files makes it trivial for them to be exposed in production.
**Prevention:** Use environment variables (`os.environ.get()`) to configure sensitive values, providing the insecure/development values as defaults to not break local environments.
