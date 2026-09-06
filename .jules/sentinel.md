## 2024-09-06 - [CRITICAL] Fix insecure Django settings
**Vulnerability:** Django settings `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `videodownloader_project/settings.py`.
**Learning:** Hardcoded configuration parameters like `SECRET_KEY` and `DEBUG = True` present a significant security risk if deployed in a production environment as they could allow arbitrary code execution, session hijacking, or information disclosure.
**Prevention:** Always use environment variables for sensitive settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS`. When modifying existing codebases to be more secure, always provide fallbacks for the original values to ensure that local development and testing environments do not break.
