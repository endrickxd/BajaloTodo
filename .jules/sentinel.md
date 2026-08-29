## 2024-11-20 - [Hardcoded Django Settings]
**Vulnerability:** Django SECRET_KEY and other sensitive configurations like DEBUG and ALLOWED_HOSTS were hardcoded in settings.py.
**Learning:** Hardcoding sensitive settings exposes the app to potential security risks. Using environment variables allows secure production deployment, but it is important to provide fallbacks for local development testing to not break environments.
**Prevention:** Always use `os.environ.get('VAR_NAME', 'fallback_value')` for sensitive configuration variables in settings.py.
