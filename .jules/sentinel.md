## 2023-11-10 - Server-Side Request Forgery (SSRF) in `requests.get`

**Vulnerability:**
The `download_via_cobalt` function in `downloader/utils.py` calls `requests.get(download_url, ...)` where `download_url` is derived from an external API response without explicit validation of the URL hostname. This makes the application vulnerable to Server-Side Request Forgery (SSRF), allowing an attacker to force the server to issue HTTP requests to internal IP addresses or arbitrary remote endpoints.

**Learning:**
DNS rebinding or simply responding with private IP addresses in redirected or returned URLs can bypass naive string-matching URL checks. To correctly mitigate SSRF in `requests`, we must hook into the underlying connection creation (e.g. by overriding `HTTPConnection._new_conn`) so that DNS resolution occurs exactly once and the resolved IP is verified against private, loopback, and local ranges immediately before connection.

**Prevention:**
Implement an IP validation layer that validates all resolved IP addresses (using `socket.getaddrinfo` and checking against restricted networks using `ipaddress`) before issuing requests. Use a custom HTTPAdapter to enforce this globally for any outgoing requests that rely on externally provided URLs.
