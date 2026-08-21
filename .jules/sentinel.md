## 2024-05-18 - [Fix Hardcoded Secrets in Settings]
**Vulnerability:** Django core settings (SECRET_KEY, DEBUG, ALLOWED_HOSTS) were hardcoded in `settings.py`, risking sensitive credential exposure.
**Learning:** For Django applications, always secure production configuration using environment variables, while maintaining local defaults for seamless developer workflows.
**Prevention:** Use `os.environ.get()` with safe defaults in settings configurations.
