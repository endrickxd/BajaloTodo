## 2024-09-13 - Secure handling of Django settings

**Vulnerability:** Hardcoded `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` in `settings.py` exposed sensitive information and could lead to misconfiguration in production environments.
**Learning:** Django settings often need different values for development vs. production. Hardcoding them leads to security vulnerabilities if the code is public or accessed improperly. Using environment variables is crucial for managing these settings securely.
**Prevention:** Use `os.environ.get()` for sensitive or environment-specific settings in `settings.py`. To ensure local development doesn't break, use the original hardcoded values as fallbacks in `os.environ.get(..., fallback_value)`. Ensure `import os` is present.
