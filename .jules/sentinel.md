## 2024-10-05 - SSRF Vulnerability in Downloader Output

**Vulnerability:** The `download_via_cobalt` function in `downloader/utils.py` accepts URLs from external APIs and directly fetches them using `requests.get()` without proper validation. This could lead to a Server-Side Request Forgery (SSRF) if the API returns a malicious internal URL or an attacker controls the API response.

**Learning:** `requests.get()` follows redirects by default. Validating a URL before fetching it is insufficient if it redirects to an internal IP address. Using `socket.getaddrinfo` is necessary to resolve all IPs for a given hostname to prevent DNS rebinding or custom DNS A record bypasses.

**Prevention:** Manually handle redirects by setting `allow_redirects=False` in `requests.get()`. After each redirect, validate the new URL's IP addresses using robust methods (`socket.getaddrinfo`) to ensure they do not fall into private, loopback, link-local, multicast, or unspecified ranges. Use `urllib.parse.urljoin` to resolve relative redirect URLs. Note: While this mitigates basic SSRF, sophisticated attacks like TOCTOU (Time-of-Check to Time-of-Use) via DNS rebinding require deeper integrations (e.g., custom transport adapters) that are difficult to implement natively with `requests`.
