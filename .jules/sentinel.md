## 2024-05-18 - Hardcoded Django Settings
**Vulnerability:** Django settings like `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `settings.py`. This poses a significant security risk if the codebase is exposed or committed to version control.
**Learning:** It is crucial to load sensitive configuration values from environment variables instead of hardcoding them, while maintaining fallbacks to the original values to avoid breaking the local development environment or test suites that do not use environment variables.
**Prevention:** Use `os.environ.get()` to load configuration variables with sensible fallbacks (e.g., `os.environ.get('SECRET_KEY', 'original_hardcoded_value')`) to secure Django applications effectively without introducing regressions.
