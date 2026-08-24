## 2024-10-24 - Hardcoded Secrets in Django Settings
**Vulnerability:** The Django SECRET_KEY was hardcoded directly into the settings.py file, and DEBUG was explicitly hardcoded to True.
**Learning:** Hardcoding sensitive configuration values exposes the application to severe risks if the source code is compromised, and leaving DEBUG enabled can leak stack traces to attackers.
**Prevention:** Use environment variables (e.g. `os.environ.get`) to load sensitive values and configuration flags like SECRET_KEY and DEBUG, providing safe fallbacks for local development when necessary.
