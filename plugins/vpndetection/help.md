# Description

Check whether an IP address is a VPN, a privacy relay, a Tor exit, a hosting or CDN address or a proxy with [VPNDetection](https://vpndetection.io), with its location, its ASN and, with an API key, the provider behind each detection

# Key Features

* Check an IP address for VPN, privacy relay and Tor use, with its hostname, country and ASN, with no API key
* With an API key, add hosting, CDN and residential, datacenter, mobile and public proxy detection, each with its provider, its confidence and the date last seen, the city, the organization and the abuse contact

# Requirements

* None for the VPN, relay, Tor and anycast flags, the hostname, the country and the ASN. A [VPNDetection API key](https://vpndetection.io/pricing) adds the hosting, CDN, proxy and service flags, the providers, the city, the organization and the abuse contact

# Supported Product Versions

* VPNDetection API 2026-11-20

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|False|VPNDetection API key. Optional: without one the plugin answers the VPN, relay, Tor and anycast flags, the hostname, the country and the ASN|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions


#### Lookup IP Address

This action is used to check an IP address for VPN, privacy relay, Tor, hosting, CDN and proxy use, with its location 
and ASN

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|The IPv4 or IPv6 address to look up|None|185.220.101.1|None|None|
  
Example input:

```
{
  "address": "185.220.101.1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|abuse|abuse|False|The address's abuse contact (needs an API key)|None|
|asn|asn|False|The autonomous system that announces the address|None|
|cdn|detection|False|CDN detection: the provider, the confidence and the date the address was last seen as one|None|
|company|company|False|The organization the address is registered to (needs an API key)|None|
|dcproxy|detection|False|Datacenter Proxy detection: the provider, the confidence and the date the address was last seen as one|None|
|hosting|detection|False|Hosting detection: the provider, the confidence and the date the address was last seen as one|None|
|hostname|string|False|The address's reverse DNS hostname|berlin01.tor-exit.artikel10.org|
|ip|string|True|The address looked up|185.220.101.1|
|is_anycast|boolean|True|Whether the address is announced from many locations (anycast)|False|
|is_bittorrent|boolean|False|Whether the address was seen on BitTorrent (needs an API key)|False|
|is_bogon|boolean|True|Whether the address is private or reserved, so not routed on the internet|False|
|is_carrier|boolean|False|Whether the address belongs to a mobile carrier (needs an API key)|False|
|is_cdn|boolean|False|Whether the address belongs to a content delivery network (needs an API key)|False|
|is_dcproxy|boolean|False|Whether the address is a datacenter proxy's exit (needs an API key)|False|
|is_dns_resolver|boolean|False|Whether the address runs an open DNS resolver (needs an API key)|False|
|is_hosting|boolean|False|Whether the address belongs to a hosting or cloud provider (needs an API key)|False|
|is_mobproxy|boolean|False|Whether the address is a mobile proxy's exit (needs an API key)|False|
|is_pubproxy|boolean|False|Whether the address runs an open public proxy (needs an API key)|False|
|is_relay|boolean|True|Whether the address is a privacy relay's or web gateway's exit|False|
|is_resproxy|boolean|False|Whether the address is a residential proxy's exit (needs an API key)|False|
|is_satellite|boolean|False|Whether the address belongs to a satellite internet provider (needs an API key)|False|
|is_smtp|boolean|False|Whether the address runs an SMTP server (needs an API key)|False|
|is_ssh|boolean|False|Whether the address runs an SSH server (needs an API key)|False|
|is_tor|boolean|True|Whether the address is a Tor exit node|True|
|is_vpn|boolean|True|Whether the address is a VPN server's exit|False|
|is_web|boolean|False|Whether the address runs a web server (needs an API key)|False|
|location|location|False|Where the address is: the country without an API key, down to the city with one|None|
|mobproxy|detection|False|Mobile Proxy detection: the provider, the confidence and the date the address was last seen as one|None|
|partial|boolean|True|True when the answer lacks the flags that need an API key: no key is set, a free key's trial is spent, or the organization's overage cap is reached. A missing flag then means unknown, not false|True|
|pubproxy|detection|False|Public Proxy detection: the provider, the confidence and the date the address was last seen as one|None|
|relay|detection|False|Relay detection: the provider, the confidence and the date the address was last seen as one|None|
|resproxy|detection|False|Residential Proxy detection: the provider, the confidence and the date the address was last seen as one|None|
|tor|detection|False|Tor detection: the provider, the confidence and the date the address was last seen as one|None|
|vpn|detection|False|VPN detection: the provider, the confidence and the date the address was last seen as one|None|
  
Example output:

```
{
  "abuse": {
    "Address": {},
    "Country": {},
    "Email": "user@example.com",
    "Name": {},
    "Network": {},
    "Phone": {}
  },
  "asn": {
    "ASN": 60729,
    "Country": {},
    "Domain": {},
    "Name": "Stiftung Erneuerbare Freiheit",
    "Prefix": {},
    "RPKI Status": {},
    "Type": {}
  },
  "cdn": {
    "Confidence": {},
    "Last Seen": {},
    "Provider": "1clickvpn",
    "Provider Name": {}
  },
  "company": {
    "Country": {},
    "Domain": {},
    "Name": "SERVERS COM LUX2",
    "Type": {}
  },
  "dcproxy": {
    "Confidence": {},
    "Last Seen": {},
    "Provider": "1clickvpn",
    "Provider Name": {}
  },
  "hosting": {
    "Confidence": {},
    "Last Seen": {},
    "Provider": "1clickvpn",
    "Provider Name": {}
  },
  "hostname": "berlin01.tor-exit.artikel10.org",
  "ip": "185.220.101.1",
  "is_anycast": false,
  "is_bittorrent": false,
  "is_bogon": false,
  "is_carrier": false,
  "is_cdn": false,
  "is_dcproxy": false,
  "is_dns_resolver": false,
  "is_hosting": false,
  "is_mobproxy": false,
  "is_pubproxy": false,
  "is_relay": false,
  "is_resproxy": false,
  "is_satellite": false,
  "is_smtp": false,
  "is_ssh": false,
  "is_tor": true,
  "is_vpn": false,
  "is_web": false,
  "location": {
    "Accuracy Radius": 10,
    "City": {},
    "Continent": "EU",
    "Continent Name": {},
    "Country": {},
    "Country Name": {},
    "Latitude": 52.52,
    "Longitude": {},
    "Postal Code": {},
    "Region": {},
    "Region Code": {},
    "Timezone": {}
  },
  "mobproxy": {
    "Confidence": {},
    "Last Seen": {},
    "Provider": "1clickvpn",
    "Provider Name": {}
  },
  "partial": true,
  "pubproxy": {
    "Confidence": {},
    "Last Seen": {},
    "Provider": "1clickvpn",
    "Provider Name": {}
  },
  "relay": {
    "Confidence": {},
    "Last Seen": {},
    "Provider": "1clickvpn",
    "Provider Name": {}
  },
  "resproxy": {
    "Confidence": {},
    "Last Seen": {},
    "Provider": "1clickvpn",
    "Provider Name": {}
  },
  "tor": {
    "Confidence": {},
    "Last Seen": {},
    "Provider": "1clickvpn",
    "Provider Name": {}
  },
  "vpn": {
    "Confidence": {},
    "Last Seen": {},
    "Provider": "1clickvpn",
    "Provider Name": {}
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**detection**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Confidence|string|None|False|How sure the detection is: low, medium or high|high|
|Last Seen|string|None|False|The date the address was last seen as one, YYYY-MM-DD|2026-11-20|
|Provider|string|None|False|The provider's identifier|1clickvpn|
|Provider Name|string|None|False|The provider's name|1Click VPN|
  
**location**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Accuracy Radius|integer|None|False|How far off the coordinates may be, in kilometers (needs an API key)|10|
|City|string|None|False|The city (needs an API key)|Berlin|
|Continent|string|None|False|The continent code|EU|
|Continent Name|string|None|False|The continent's name|Europe|
|Country|string|None|False|The ISO 3166-1 alpha-2 country code|DE|
|Country Name|string|None|False|The country's name|Germany|
|Latitude|float|None|False|The latitude (needs an API key)|52.52|
|Longitude|float|None|False|The longitude (needs an API key)|13.405|
|Postal Code|string|None|False|The postal code (needs an API key)|10115|
|Region|string|None|False|The region (needs an API key)|Berlin|
|Region Code|string|None|False|The ISO 3166-2 region code (needs an API key)|DE-BE|
|Timezone|string|None|False|The IANA time zone|Europe/Berlin|
  
**asn**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ASN|integer|None|False|The autonomous system number|60729|
|Country|string|None|False|The autonomous system's country code|DE|
|Domain|string|None|False|The autonomous system's domain|zwiebelfreunde.de|
|Name|string|None|False|The autonomous system's name|Stiftung Erneuerbare Freiheit|
|Prefix|string|None|False|The announced prefix that holds the address|185.220.101.0/24|
|RPKI Status|string|None|False|The prefix's RPKI validation status|valid|
|Type|string|None|False|The kind of network: hosting, isp, business, education or government|hosting|
  
**company**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Country|string|None|False|The organization's country code|LU|
|Domain|string|None|False|The organization's domain|servers.com|
|Name|string|None|False|The organization's name|SERVERS COM LUX2|
|Type|string|None|False|The kind of organization|hosting|
  
**abuse**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Address|string|None|False|The abuse contact's postal address|1 Example Street, Springfield|
|Country|string|None|False|The abuse contact's country code|US|
|Email|string|None|False|The abuse contact's email address|user@example.com|
|Name|string|None|False|The abuse contact's name|Example Networks|
|Network|string|None|False|The registered network the contact covers|188.42.0.0-188.42.255.255|
|Phone|string|None|False|The abuse contact's phone number|+1-555-0100|


## Troubleshooting

* Without an API key, or once a free key's trial is spent, the `partial` output is `true` and the flags that need a key are left out: a missing flag means unknown, not false
* A private or reserved address answers `is_bogon` `true` and nothing else
* An invalid API key fails the connection test with a 401 error: check the key in your VPNDetection account

# Version History

* 1.0.0 - Initial plugin - Actions: `Lookup IP Address`

# Links

* [VPNDetection](https://vpndetection.io)
* [Terms of use, including keyless use](https://vpndetection.io/terms#no-key)
* [Privacy policy](https://vpndetection.io/privacy)

## References

* [VPNDetection API](https://docs.vpndetection.io)