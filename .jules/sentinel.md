## 2024-09-14 - [Hardcoded Django Configurations]
**Vulnerability:** Core Django security configurations (SECRET_KEY, DEBUG, ALLOWED_HOSTS) were hardcoded in the codebase, which could lead to unauthorized access, debug information leakage, or host header attacks if committed or deployed as-is.
**Learning:** Even default or test settings in Django need to be properly managed via environment variables to prevent accidental exposure when moving from development to production, while preserving fallback values for developer convenience.
**Prevention:** Always use environment variables for sensitive settings in Django `settings.py` right from project initialization.
