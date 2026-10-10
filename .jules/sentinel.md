## 2024-10-10 - Application-layer SSRF Mitigation TOCTOU limitation
**Vulnerability:** Application-layer SSRF validation using DNS resolution (`socket.getaddrinfo`) followed by URL retrieval (via `requests`) is vulnerable to Time-of-Check to Time-of-Use (TOCTOU) DNS rebinding attacks.
**Learning:** The IP address resolved during validation might change before the actual request is made by `requests`. A fast-changing DNS record can trick the validation logic into checking a benign IP, while the subsequent request resolves to an internal IP.
**Prevention:** The ideal prevention is network-layer egress filtering. Application-layer mitigation is imperfect against sophisticated DNS rebinding, but checking for unresolvable IPs or using fixed IP proxies are alternatives.
