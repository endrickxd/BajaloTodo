## 2024-05-18 - SSRF Vulnerability in Cobalt Download Fetching
**Vulnerability:** The application fetches external URLs returned by third-party Cobalt API endpoints without verifying if they point to internal infrastructure. This leads to a Server-Side Request Forgery (SSRF) vulnerability.
**Learning:** External API responses containing URLs to be fetched should be explicitly validated to ensure they resolve to public IPs and do not point to private/internal networks or loopback addresses.
**Prevention:** Implement application-layer URL validation (e.g., using `socket.getaddrinfo` to resolve hostname to IPs and verify they are public/routable before fetching) when making `requests.get()` calls for media downloads.
