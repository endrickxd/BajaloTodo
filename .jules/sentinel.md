## 2024-05-24 - SSRF in download via Cobalt endpoint
**Vulnerability:** The application blindly accepts an arbitrary URL from an external Cobalt endpoint and downloads it using `requests.get` without checking if the URL resolves to a private IP (e.g. 127.0.0.1 or AWS metadata).
**Learning:** External API responses cannot be blindly trusted when they are used to perform secondary outbound requests.
**Prevention:** Implement SSRF protection using a custom HTTPAdapter that overrides connection creation to resolve the hostname and check if the IP falls into a private/loopback/link-local/multicast/unspecified range before initiating the actual socket connection.
