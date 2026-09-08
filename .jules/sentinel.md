## 2026-09-08 - Hardcoded Django Deployment Settings
**Vulnerability:** Hardcoded SECRET_KEY, DEBUG = True, and ALLOWED_HOSTS = ['*'] in default Django settings.py.
**Learning:** Default Django templates leave critical deployment configurations insecure to prioritize developer experience, requiring explicit mitigation before production.
**Prevention:** Always refactor Django settings to consume environment variables for secrets, debug flags, and host lists upon project initialization. Use fallbacks to maintain local operability.
