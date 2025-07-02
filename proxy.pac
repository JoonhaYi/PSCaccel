function FindProxyForURL(url, host) {
  //   // Don't proxy local addresses
  //   if (isPlainHostName(host) || dnsDomainIs(host, ".local")) {
  //     return "DIRECT";
  //   }

  //   // Proxy only example.com
  //   if (shExpMatch(host, "*.pulsars.nanograv.org")) {
  //     return "PROXY 127.0.0.1:8080";
  //   }

  //   // Default rule: direct connection
  //   return "DIRECT";
  return "PROXY 127.0.0.1:8080";
}
