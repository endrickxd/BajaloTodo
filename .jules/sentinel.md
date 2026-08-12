## 2024-05-18 - [Hardcoded Django Secrets]
**Vulnerability:** Django settings `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded.
**Learning:** Hardcoding sensitive configuration values exposes the application to severe risks if the repository is compromised. It's a common oversight in early development phases that persists into production.
**Prevention:** Always use environment variables to load sensitive configuration settings. Provide local development fallbacks if necessary to avoid breaking existing workflows, but ensure production environments override these fallbacks.
