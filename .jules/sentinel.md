## 2024-11-20 - Hardcoded Django Configuration

**Vulnerability:** Django settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `settings.py`. Hardcoding secrets is a critical vulnerability as it exposes them to anyone with repository access. Hardcoding `DEBUG=True` and `ALLOWED_HOSTS=['*']` in a shared file can easily lead to these insecure settings being deployed to production.

**Learning:** It's a common anti-pattern to leave default Django settings unmodified from project creation. These settings must be externalized to environment variables to ensure they can be safely configured differently in development versus production environments. Using `os.environ.get()` with a fallback preserves local development workflow while allowing production environments to inject secure values.

**Prevention:** Always use environment variables for sensitive configuration and environment-specific settings (like `DEBUG` and `ALLOWED_HOSTS`). Ensure template projects or initial setups are immediately refactored to follow twelve-factor app principles for configuration.
