## 2024-07-28 - Django Config Injection Security Update
**Vulnerability:** Hardcoded Django `SECRET_KEY` and `DEBUG = True` forced globally.
**Learning:** Hardcoded secrets and active debug modes in production can leak sensitive stack traces and allow session tampering. Defaulting to these values in `settings.py` without environment overrides prevents secure deployments.
**Prevention:** Always wrap sensitive configuration variables using `os.environ.get()`, providing the original hardcoded values as fallback to avoid breaking local dev setups while allowing secure overriding in production.
