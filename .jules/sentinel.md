## 2024-05-18 - [CRITICAL] Fixed hardcoded Django secrets
**Vulnerability:** Django settings including SECRET_KEY, DEBUG, and ALLOWED_HOSTS were hardcoded in settings.py.
**Learning:** This is a common pattern that risks exposing sensitive information or enabling unsafe settings in production environments. Using environment variables correctly allows for safer configuration management without breaking local development by providing safe fallbacks.
**Prevention:** Always use environment variables for sensitive or environment-specific configurations like SECRET_KEY, DEBUG, and ALLOWED_HOSTS in Django settings, ensuring to provide appropriate type casting (e.g., boolean conversion for DEBUG, string splitting for ALLOWED_HOSTS).
