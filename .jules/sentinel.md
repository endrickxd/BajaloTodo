## 2024-11-04 - SSRF Vulnerability in Cobalt Download Utility
**Vulnerability:** `downloader/utils.py` fails to validate the `download_url` obtained from the Cobalt API response before performing a `requests.get()` in the `download_via_cobalt` function.
**Learning:** External API responses returning redirect URLs must be strictly validated before they are accessed to prevent Server-Side Request Forgery, even when using popular libraries like `requests`.
**Prevention:** Implement strict IP validation logic to resolve IP addresses behind domains and block any requests attempting to access local, private, loopback, link-local, multicast, or unspecified IP ranges. Use a custom HTTPAdapter for `requests` to prevent TOCTOU (Time-of-Check to Time-of-Use) DNS rebinding attacks.
