## 2026-08-05 - Securing Django Settings
**Vulnerability:** Hardcoded SECRET_KEY, DEBUG=True, and ALLOWED_HOSTS=['*'] in videodownloader_project/settings.py
**Learning:** These settings were insecure by default and are commonly missed in basic Django setups. Utilizing os.environ.get with fallback defaults is a great way to handle this securely while not breaking existing local setups.
**Prevention:** Avoid hardcoding secrets. Always ensure environment variables are used for sensitive configurations, with fallback logic for local environments.
