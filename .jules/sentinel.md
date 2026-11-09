## 2024-11-09 - [Fix external URL SSRF]
**Vulnerability:** The application was vulnerable to SSRF by using `requests.get()` to download from external URLs provided by the Cobalt API responses without any validation.
**Learning:** External API responses cannot be fully trusted, and they might provide a `download_url` that points to an internal IP address or domain.
**Prevention:** Implement a custom requests adapter that resolves and validates IP addresses to avoid hitting internal network ranges.