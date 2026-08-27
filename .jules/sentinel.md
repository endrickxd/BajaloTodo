## 2026-08-27 - Fix hardcoded Django secrets
**Vulnerability:** Hardcoded Django SECRET_KEY, DEBUG mode enabled in production, and permissive ALLOWED_HOSTS ('*') in settings.py.
**Learning:** Hardcoded configuration allows anyone with access to the source code to potentially exploit the application (e.g., through session tampering or host header attacks). Keeping debug enabled in production exposes detailed error pages.
**Prevention:** Use environment variables for sensitive settings, debug flags, and host configurations to ensure they can be securely managed and separated from source control.
