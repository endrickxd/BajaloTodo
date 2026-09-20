## 2024-11-28 - [Critical] Hardcoded Django Settings
**Vulnerability:** Django settings `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` were hardcoded in `settings.py`. This poses a critical risk if the code is deployed to production without modifications or if the repository becomes public.
**Learning:** Hardcoding security settings is a common default for Django projects, but it's important to externalize these as environment variables before moving closer to production. We also need to keep the original hardcoded values as fallbacks using `os.environ.get()` so that local development and test environments do not break.
**Prevention:** Use `os.environ.get()` with fallbacks for sensitive settings to ensure secure defaults for production without breaking local development setups.
