## 2025-02-14 - Prevent SSRF in download_via_cobalt
**Vulnerability:** `downloader/utils.py` uses the URL returned by Cobalt API for direct file streaming without validating the target URL. This leads to Server-Side Request Forgery (SSRF) since Cobalt instances or network manipulators can return URLs pointing to internal infrastructure.
**Learning:** External APIs returning URLs to be consumed by backend `requests.get` need strict validation to prevent SSRF, particularly loopback and internal addresses.
**Prevention:** Use a validation function to verify IP addresses and reject internal blocks before allowing HTTP requests.

## 2025-02-14 - SSRF Mitigation Limit: TOCTOU and Redirect State
**Vulnerability:** Even with `is_safe_url` resolving DNS and checking IPs, a Time-of-Check to Time-of-Use (TOCTOU) DNS rebinding vulnerability persists. The IP validated may differ from the IP subsequently fetched by `requests.get` if the DNS TTL is very short. Additionally, manual redirect loops drop cookies set on 3xx responses.
**Learning:** Pure application-layer SSRF validation in Python without deep hook overrides in `urllib3`'s connection pool remains imperfect against DNS rebinding.
**Prevention:** Consider enforcing SSRF protection at the network/infrastructure layer (e.g., egress firewalls) for definitive security, or overriding connection pooling to pin the validated IP.
