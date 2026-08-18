## 2024-05-15 - [Hardcoded Django Security Settings]
**Vulnerability:** Django settings including SECRET_KEY, DEBUG, and ALLOWED_HOSTS were hardcoded in `settings.py`.
**Learning:** These settings control key application behaviors. Hardcoding them leads to exposure of the `SECRET_KEY`, potentially leaving `DEBUG` enabled in production (leaking sensitive errors), and allowing any domain for `ALLOWED_HOSTS`.
**Prevention:** Always pull sensitive configuration values from environment variables (`os.environ.get()`), using safe fallback values for local development where applicable.
