## 2024-05-14 - [Hardcoded Django Configuration]
**Vulnerability:** Hardcoded SECRET_KEY, DEBUG = True, and ALLOWED_HOSTS = ["*"] in production settings.
**Learning:** Found common Django anti-pattern where production secrets and debug flags are committed directly to codebase. This allows trivial exploitation in deployment.
**Prevention:** Always use environment variables for sensitive settings with safe defaults for local development.
