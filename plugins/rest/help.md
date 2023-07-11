# Description
The HTTP Requests plugin allows users to automate HTTP requests to API services such as [RESTful based services](https://en.wikipedia.org/wiki/Representational_state_transfer).

# Key Features
*This plugin does not contain any key features.*  

# Requirements
*This plugin does not contain any requirements.*  

# Supported Product Versions
* 2022-09-05

# Documentation

## Setup
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|authentication_type|string|No Authentication|False|Type of authentication|['Basic Auth', 'Digest Auth', 'Bearer Token', 'Rapid7 Insight', 'OpsGenie', 'Pendo', 'Custom', 'No Authentication']|Basic Auth|
|base_url|string|None|True|Base URL e.g. https://httpbin.org|None|https://httpbin.org/|
|basic_auth_credentials|credential_username_password|None|False|Username and password. Provide if you choose Basic Auth or Digest Auth authentication type|None|{"username": "user@example.com", "password": "mypassword"}|
|client_certificate|file|None|False|Client certificate for mutual TLS (Certificate or Certificate/Key combination)|None|LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tClBJSUVHRENDqXdDZ0F3SUJBZ0lJU3F4Vjgva3ZoSWN3RFFZSktvWklodmNoQVFFTEJRQXdNVEVPTUF3R0ExVUUKQXd3RlZrUlFRMEV4RWpBUUJnTlZCQW9NQ2ZaRVVGWkpVMEZEUVRFTE1Ba0dBMVVFQmhNQ1ZWTXdIaGNOTWpJdwpPVEEzTVRReE16TTRXaGNOTWpRd09UQTJNVFF4TXpNNFdqQ0I1VEVtTUNRR0NTcUdTSWIzRFFFSkFSWVhZV1JoCmJWOWliR0ZyYkdWNVFISmhjR2xrTnk0amIyMHhOREF5QmdvSmtpYUprL0lzWkFFQkRDUTNOVFExWTJabE5pMHgKTTJRMUxUUmpNalF0WVNZMllTMDJPVFUzTWprMFpqRTJabUV4TFRBckJnTlZCQU1NSkRjMU5EVmpabVUyTFRFMwpaRFV0TkdNeU5DMWhOalpoTFRZNU5UY3lPVFJtTVRabVlURVRNQUVHQTFVRUN3d0tSR1Z3WVhKMGJXVnVkREVWCk1CTUdBMVVFQ2d3TVQzSm5ZVzVwZW1GMGFXOXVNUTB3Q3dZRFZRUUhEQVJEYVhSNU1RNHdEQVlEVlFRSURBVlQKZEdGMFpURUxNQWtHQTFVRUJoTUNWVk13Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLQW9JQgpBUURVWk1LUHUxS0cra3NjUGpNZjZHSnFKdnJXM3pmajlUK1psQTBkblVQRk9lZjYvWEhWV0drV1crYkJJRkJJCkl3d0dBeFVWTStrU1N1N3VReWY3QnhSQlNxM0FLVzBiblZWZy9FaGhBd2VyYi9zT1NGbHpiOEptMDNBVE04QlgKaXRla2VBYzM4UW5jL3lwZG44MmRxYUF5TFYyTGw0QnZlWDRiYUp2a3RpVlRIUG9iZmhsYXFmTUh0M1hDVG1sNgpJVWRSVjczZ1NsTHdpY05yWHdtdXk2T3dJeEdKQm9DOVZYWE00T3oxMmY2WXJHQzlMaDNkYmRxN04yZm9qSGM5CjVQdUJoaGFRK2J6NWNBSXQvYWZQZEQrYzkyd3B4Z0JRTEVUampZazBNYlpDcGpna0tTODhRbjFjeVo1RmNJVTQKck5sTS9PSkRQZ3BLejFEa1VwWVFlL05aQWdNQkFBR2pmekI5TUF3R0ExVWRFd0VCL3dRQ01BQXdId1lEVlIwagpCQmd3Rm9BVXI5MXV0cUJMbkhtNUZnaGk1aU14RUtlQzY2RXdIUVlEVlIwbEJCWXdGQVlJS3dZQkJRVUhBd0lHCkNDc0dBUVVGQndNRU1CMEdBMVVkRGdRV0JCVDYrcXRmVjZiTWxkZlpFSEtua1NoZkUzZ3pjakFPQmdOVkhROEIKQWY4RUJBTUNCZUF3RFFZSktvWklodmNOQVFFTEJRQURnZ0VCQUJBSWhpaFpiZzMzNmhWVEZEdzVoL05TQzZVSgp3bExwUkhxb29sU3J3TTV4S1l3K3k2aVJURTdCdUZ1aktvL2ZJWm52YklHUDRiZEw5OUJ0TmRPNjh4elZnNDBICmEwZ0FLUXp1aWZUYUhyWFg3Ti9SanpRclVHMTRFdTJXMmQvaVNtQ2tzM1ExTmM1R1VGblVnYXNlYzllZ1F3UTIKNnJyM2x2NFJDVkNFektSeWltUWVNSjdLaElhK3BKck5yRHBDUFJMdTlDTkhkUTA5OUdoS2xaV2kzSC9vczZhVQpmSTIzcDFzc3dBK01nN2h3M01rS0lTcTdvOEt3c3JVaUZST2NXM0ZPMnFVNGNrMDc0MlB1SkxJUEJLMjJSakpKCnFUemhZaVlnbGczdFdlSkRmb05tbWdOMmR3b3F2dW5ta0dsQ0ZlOU5TK2hyVkxMeTcrTkdXSTJBSmZQPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0t|
|default_headers|object|None|False|Custom headers to include in all requests associated with this connection. To pass a encrypted key as a header value, enter your key in the Secret Key input and set the value of the header in this field to "CUSTOM_SECRET_INPUT" instead of secret key. The plugin will replace "CUSTOM_SECRET_INPUT" with the encrypted key stored in the Secret Key input when the plugin runs.|None|{ "User-Agent": "Rapid7 InsightConnect", "Custom-Key-Header": "CUSTOM_SECRET_INPUT" }|
|fail_on_http_errors|boolean|True|False|Indicates whether the plugin should fail on standard HTTP errors (4xx-5xx)|None|True|
|private_key|file|None|False|Private key for mutual TLS (requires Client Certificate)|None|LS0tLS1CRudJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpQSUlFcFFJQkFBS0NBUUVPMUdUQ2o3dFNodnBMSEQ0ekgraGlvbUw2MXQ4MzQvVS9tWfFOSFoxRHhUbm4rdjF4CjFWaHBGbHZtd1NCUVNDTU1CZ01WRpRQcExrcnU4a01uK3djVVFVcXR3Q2x0RzUxVllQeElZUU1IUTIvN0RraFoKYzIvQ1p0TndFelBBVjRyWHBIZ0hOL0VKNFA4cVhYL05uYW1nTWkxZGk1ZUFiM2wrRzJpYjVMWWxVeHo2RzM0WgpXcW56QjdkMXdrNW91aUZIVVZlOTRFcFM4SW5EYTE4SnJzdWpzQ01SaVFhQXZWVjF6T0RzOWZYK21LeGd2UzRkCjNXM2F1emRuNkl4M1BlVDdnWVlXa1BtOCtYQUNMZjJuejNRL25QZHNLY1lBVUN4RTQ0Mkk5REcyUXFZNEpDa3YKUEVKOVhNbWVSWENGT0t6WlRQemlRejRLU3M5UTVGS1dFSHZ6R1FJREFRQUJBb0lCQVFDOWFiYVJsQTcvVFF2YQovaVY5MlRLYmlmWUYxai96emUyUU94YVBTSWI5eHF4NWk3a08rSytQUHhwRk5Wb2pXdzRIOW92QXd2Q2lYYTFEClV5UytuQXVXUnRFNVJEaUhuZ0pjWWVEeWswOHR0c29BYk1sSlIydnBZN3JaaFJlTmVzYmhhQ0dYNUNCVnRFSEcKQ1JQSC9WUmVLMUwzZ0g4TDZ4OXB0aHNCRnVlbWU5c2pmdXpaUlVMUkx4YkxZVS9hQWJoSDlxR2Z1NEwyY0RDMgozSGV1MVNrdjZzTllWbzNPQW9mVkY4dWFDUUtzeWhPWGJ2b1REM1lvR3NycTh2Q1ZPNHdIRWhvdG8zZFVzNGs5Cm8zMVdvcnprNndYYVV3b0pUcGZxbWRBUnRlb0twdWZ3aFZ6K0k1c1Ezb1c4U3RjM0FXSTk4RTFSdmRmTHc2elAKeGxRbVIvaDVBb0dCQU96bGZxSzlEeUdJMTJLUkdqYjR1bTdrNUFSUWZaVllYNVdndW9iYmNraVk0b1JtVlBIZgpOYm5hTkloVjN6ZjVHWEgwQk9CR2lvOUU3N0FiMUphMXE3d2FPRnJlUURPeHRCZ1BuTXo5OHRJMWJrOXEvZTB5CmlUNTI4OFFLUXV3TTM3QkNOZmtLZUdTOFhIN2gxZm9FZVUxb1k1M1NLWjFvOEM5YkdMc242UWp6QW9HQkFPV0YKYlROK2MvTG50OUprQ2Z0eDhJdk1vcU05TkJLNStXTmRUMU1CcjlxcmhPYmNsZ0d0TzAvaUs3aEpSY0Q3alpIZwpnMnVrU01iUkR1VUo0ZjFSUlNveFBDZWJrcktyNllNQmRTZ2IrZFIyRWJVQ2NReU5oMFJ3L1ovQlNSQ29SSGxUClhPb29iazlnUUN2WHNROUlUK3lTNFlaaE5iNFQ0eXE4bDBpQlJkYkRBb0dBTE11Y2p6cWJibTB0d3hoTHZkR2QKeEFoUnY5TTFBdndyLzkySklqZDNVOG9mOEZGdldZQW5ualg2Y0pGaE0rK28vU2pYbUx4NGcxVWcyVXZJSUthMworWjR2bmtKdVRsdG1ITWFhRUNDbXhTOHRqTWt1bXpqWmRXTkp5TWJCMHlqYUpnWFo2USt6Tzl5UkhnNURFMXg3CkxZRmhaVVJDcE8vR1RkSG9YTjJIQm1NQ2dZRUF1ZXRWNU5OMjJ2bW1wcTlRZ3JUdUZHQkVFaFQrdkhpWE1rMGcKZDIyelpGOXh2WXhMbXJvWGhJTUJ4VHJkWFJDbndkWHF2dVFKNjdybjVOTVhrNW9rZTZQOFJWMDQvTEJTN0VMZgpBd2wrV3dMMUh2b0dWeFBCMGNmeE9scFlkRHpKa3JuYlZ2WS9QTjhMdkRmdy9oOG1WczA0RUNGb1pqcG9kM0xpCjNPR1NqLzhDZ1lFQWthekw5UDJTVHVPck1HYncrK2xSVER2RVlSUXp2b3U0UEFudHlOQUtNSFo3MmNwc0pRRG8KMXdIelFweHRwc0I3bzNoMTEweFdId2xMQ3BzaXFueExoVlRIek9WUVFaQnR5cjhMTVMwVDY5UVc1ekhmcS9hZQpSeGtYdDR0bmUrL0dQdzFPMlN6d3IxcmxUV2tNRGxoM2VEU3R2TjVaaW9qZXM2OVMwb3QzZWVMPQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo|
|secret|credential_secret_key|None|False|Credential secret key. Provide a Bearer Token, Rapid7 Insight, OpsGenie, Pendo or using "CUSTOM_SECRET_INPUT" in the Default Headers field for Custom authentication type|None|9de5069c5afe602b2ea0a04b66beb2c0|
|ssl_verify|boolean|True|True|Verify TLS/SSL certificate|None|True|
  
Example input:

```
{
  "authentication_type": "No Authentication",
  "base_url": "https://httpbin.org/",
  "basic_auth_credentials": {
    "password": "mypassword",
    "username": "user@example.com"
  },
  "client_certificate": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tClBJSUVHRENDqXdDZ0F3SUJBZ0lJU3F4Vjgva3ZoSWN3RFFZSktvWklodmNoQVFFTEJRQXdNVEVPTUF3R0ExVUUKQXd3RlZrUlFRMEV4RWpBUUJnTlZCQW9NQ2ZaRVVGWkpVMEZEUVRFTE1Ba0dBMVVFQmhNQ1ZWTXdIaGNOTWpJdwpPVEEzTVRReE16TTRXaGNOTWpRd09UQTJNVFF4TXpNNFdqQ0I1VEVtTUNRR0NTcUdTSWIzRFFFSkFSWVhZV1JoCmJWOWliR0ZyYkdWNVFISmhjR2xrTnk0amIyMHhOREF5QmdvSmtpYUprL0lzWkFFQkRDUTNOVFExWTJabE5pMHgKTTJRMUxUUmpNalF0WVNZMllTMDJPVFUzTWprMFpqRTJabUV4TFRBckJnTlZCQU1NSkRjMU5EVmpabVUyTFRFMwpaRFV0TkdNeU5DMWhOalpoTFRZNU5UY3lPVFJtTVRabVlURVRNQUVHQTFVRUN3d0tSR1Z3WVhKMGJXVnVkREVWCk1CTUdBMVVFQ2d3TVQzSm5ZVzVwZW1GMGFXOXVNUTB3Q3dZRFZRUUhEQVJEYVhSNU1RNHdEQVlEVlFRSURBVlQKZEdGMFpURUxNQWtHQTFVRUJoTUNWVk13Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLQW9JQgpBUURVWk1LUHUxS0cra3NjUGpNZjZHSnFKdnJXM3pmajlUK1psQTBkblVQRk9lZjYvWEhWV0drV1crYkJJRkJJCkl3d0dBeFVWTStrU1N1N3VReWY3QnhSQlNxM0FLVzBiblZWZy9FaGhBd2VyYi9zT1NGbHpiOEptMDNBVE04QlgKaXRla2VBYzM4UW5jL3lwZG44MmRxYUF5TFYyTGw0QnZlWDRiYUp2a3RpVlRIUG9iZmhsYXFmTUh0M1hDVG1sNgpJVWRSVjczZ1NsTHdpY05yWHdtdXk2T3dJeEdKQm9DOVZYWE00T3oxMmY2WXJHQzlMaDNkYmRxN04yZm9qSGM5CjVQdUJoaGFRK2J6NWNBSXQvYWZQZEQrYzkyd3B4Z0JRTEVUampZazBNYlpDcGpna0tTODhRbjFjeVo1RmNJVTQKck5sTS9PSkRQZ3BLejFEa1VwWVFlL05aQWdNQkFBR2pmekI5TUF3R0ExVWRFd0VCL3dRQ01BQXdId1lEVlIwagpCQmd3Rm9BVXI5MXV0cUJMbkhtNUZnaGk1aU14RUtlQzY2RXdIUVlEVlIwbEJCWXdGQVlJS3dZQkJRVUhBd0lHCkNDc0dBUVVGQndNRU1CMEdBMVVkRGdRV0JCVDYrcXRmVjZiTWxkZlpFSEtua1NoZkUzZ3pjakFPQmdOVkhROEIKQWY4RUJBTUNCZUF3RFFZSktvWklodmNOQVFFTEJRQURnZ0VCQUJBSWhpaFpiZzMzNmhWVEZEdzVoL05TQzZVSgp3bExwUkhxb29sU3J3TTV4S1l3K3k2aVJURTdCdUZ1aktvL2ZJWm52YklHUDRiZEw5OUJ0TmRPNjh4elZnNDBICmEwZ0FLUXp1aWZUYUhyWFg3Ti9SanpRclVHMTRFdTJXMmQvaVNtQ2tzM1ExTmM1R1VGblVnYXNlYzllZ1F3UTIKNnJyM2x2NFJDVkNFektSeWltUWVNSjdLaElhK3BKck5yRHBDUFJMdTlDTkhkUTA5OUdoS2xaV2kzSC9vczZhVQpmSTIzcDFzc3dBK01nN2h3M01rS0lTcTdvOEt3c3JVaUZST2NXM0ZPMnFVNGNrMDc0MlB1SkxJUEJLMjJSakpKCnFUemhZaVlnbGczdFdlSkRmb05tbWdOMmR3b3F2dW5ta0dsQ0ZlOU5TK2hyVkxMeTcrTkdXSTJBSmZQPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0t",
  "default_headers": {
    "Custom-Key-Header": "CUSTOM_SECRET_INPUT",
    "User-Agent": "Rapid7 InsightConnect"
  },
  "fail_on_http_errors": true,
  "private_key": "LS0tLS1CRudJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpQSUlFcFFJQkFBS0NBUUVPMUdUQ2o3dFNodnBMSEQ0ekgraGlvbUw2MXQ4MzQvVS9tWfFOSFoxRHhUbm4rdjF4CjFWaHBGbHZtd1NCUVNDTU1CZ01WRpRQcExrcnU4a01uK3djVVFVcXR3Q2x0RzUxVllQeElZUU1IUTIvN0RraFoKYzIvQ1p0TndFelBBVjRyWHBIZ0hOL0VKNFA4cVhYL05uYW1nTWkxZGk1ZUFiM2wrRzJpYjVMWWxVeHo2RzM0WgpXcW56QjdkMXdrNW91aUZIVVZlOTRFcFM4SW5EYTE4SnJzdWpzQ01SaVFhQXZWVjF6T0RzOWZYK21LeGd2UzRkCjNXM2F1emRuNkl4M1BlVDdnWVlXa1BtOCtYQUNMZjJuejNRL25QZHNLY1lBVUN4RTQ0Mkk5REcyUXFZNEpDa3YKUEVKOVhNbWVSWENGT0t6WlRQemlRejRLU3M5UTVGS1dFSHZ6R1FJREFRQUJBb0lCQVFDOWFiYVJsQTcvVFF2YQovaVY5MlRLYmlmWUYxai96emUyUU94YVBTSWI5eHF4NWk3a08rSytQUHhwRk5Wb2pXdzRIOW92QXd2Q2lYYTFEClV5UytuQXVXUnRFNVJEaUhuZ0pjWWVEeWswOHR0c29BYk1sSlIydnBZN3JaaFJlTmVzYmhhQ0dYNUNCVnRFSEcKQ1JQSC9WUmVLMUwzZ0g4TDZ4OXB0aHNCRnVlbWU5c2pmdXpaUlVMUkx4YkxZVS9hQWJoSDlxR2Z1NEwyY0RDMgozSGV1MVNrdjZzTllWbzNPQW9mVkY4dWFDUUtzeWhPWGJ2b1REM1lvR3NycTh2Q1ZPNHdIRWhvdG8zZFVzNGs5Cm8zMVdvcnprNndYYVV3b0pUcGZxbWRBUnRlb0twdWZ3aFZ6K0k1c1Ezb1c4U3RjM0FXSTk4RTFSdmRmTHc2elAKeGxRbVIvaDVBb0dCQU96bGZxSzlEeUdJMTJLUkdqYjR1bTdrNUFSUWZaVllYNVdndW9iYmNraVk0b1JtVlBIZgpOYm5hTkloVjN6ZjVHWEgwQk9CR2lvOUU3N0FiMUphMXE3d2FPRnJlUURPeHRCZ1BuTXo5OHRJMWJrOXEvZTB5CmlUNTI4OFFLUXV3TTM3QkNOZmtLZUdTOFhIN2gxZm9FZVUxb1k1M1NLWjFvOEM5YkdMc242UWp6QW9HQkFPV0YKYlROK2MvTG50OUprQ2Z0eDhJdk1vcU05TkJLNStXTmRUMU1CcjlxcmhPYmNsZ0d0TzAvaUs3aEpSY0Q3alpIZwpnMnVrU01iUkR1VUo0ZjFSUlNveFBDZWJrcktyNllNQmRTZ2IrZFIyRWJVQ2NReU5oMFJ3L1ovQlNSQ29SSGxUClhPb29iazlnUUN2WHNROUlUK3lTNFlaaE5iNFQ0eXE4bDBpQlJkYkRBb0dBTE11Y2p6cWJibTB0d3hoTHZkR2QKeEFoUnY5TTFBdndyLzkySklqZDNVOG9mOEZGdldZQW5ualg2Y0pGaE0rK28vU2pYbUx4NGcxVWcyVXZJSUthMworWjR2bmtKdVRsdG1ITWFhRUNDbXhTOHRqTWt1bXpqWmRXTkp5TWJCMHlqYUpnWFo2USt6Tzl5UkhnNURFMXg3CkxZRmhaVVJDcE8vR1RkSG9YTjJIQm1NQ2dZRUF1ZXRWNU5OMjJ2bW1wcTlRZ3JUdUZHQkVFaFQrdkhpWE1rMGcKZDIyelpGOXh2WXhMbXJvWGhJTUJ4VHJkWFJDbndkWHF2dVFKNjdybjVOTVhrNW9rZTZQOFJWMDQvTEJTN0VMZgpBd2wrV3dMMUh2b0dWeFBCMGNmeE9scFlkRHpKa3JuYlZ2WS9QTjhMdkRmdy9oOG1WczA0RUNGb1pqcG9kM0xpCjNPR1NqLzhDZ1lFQWthekw5UDJTVHVPck1HYncrK2xSVER2RVlSUXp2b3U0UEFudHlOQUtNSFo3MmNwc0pRRG8KMXdIelFweHRwc0I3bzNoMTEweFdId2xMQ3BzaXFueExoVlRIek9WUVFaQnR5cjhMTVMwVDY5UVc1ekhmcS9hZQpSeGtYdDR0bmUrL0dQdzFPMlN6d3IxcmxUV2tNRGxoM2VEU3R2TjVaaW9qZXM2OVMwb3QzZWVMPQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo",
  "secret": "9de5069c5afe602b2ea0a04b66beb2c0",
  "ssl_verify": true
}
```  

## Technical Details

### Actions
  

#### DELETE
  
Make a DELETE request  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|body_any|string|None|False|Payload (string) to submit to the server when making the HTTP Request call. This can be any type of input, such as an array or integers etc.. If a data object is to be sent, please use the 'Body Object' input|None|test data|
|body_object|object|None|False|Payload to submit to the server when making the HTTP Request call|None|{"user": "user@example.com"}|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|
  
Example input:

```
{
  "body_any": "test data",
  "body_object": {
    "user": "user@example.com"
  },
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```  

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|body_object|object|False|Response payload from the server as an object. Note, if the response has invalid object structure (list, string..) plugin will wrap it with object map|{'user': 'user@example.com'}|
|body_string|string|False|Response payload from the server as a string|test data|
|headers|object|False|Response headers from the server|{'Host': 'rapid7.com'}|
|status|integer|False|Status code of the response from the server|200|
  
Example output:

```
{
  "body_object": {
    "user": "user@example.com"
  },
  "body_string": "test data",
  "headers": {
    "Host": "rapid7.com"
  },
  "status": 200
}
```  

#### GET
  
Make a GET request  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|body_any|string|None|False|Payload (string) to submit to the server when making the HTTP Request call. This can be any type of input, such as an array or integers etc.. If a data object is to be sent, please use the 'Body Object' input|None|test data|
|body_object|object|None|False|Payload to submit to the server when making the HTTP Request call|None|{"user": "user@example.com"}|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|
  
Example input:

```
{
  "body_any": "test data",
  "body_object": {
    "user": "user@example.com"
  },
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```  

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|body_object|object|False|Response payload from the server as an object. Note, if the response has invalid object structure (list, string..) plugin will wrap it with object map|{'user': 'user@example.com'}|
|body_string|string|False|Response payload from the server as a string|test data|
|headers|object|False|Response headers from the server|{'Host': 'rapid7.com'}|
|status|integer|False|Status code of the response from the server|200|
  
Example output:

```
{
  "body_object": {
    "user": "user@example.com"
  },
  "body_string": "test data",
  "headers": {
    "Host": "rapid7.com"
  },
  "status": 200
}
```  

#### PATCH
  
Make a PATCH request  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|body_any|string|None|False|Payload (string) to submit to the server when making the HTTP Request call. This can be any type of input, such as an array or integers etc.. If a data object is to be sent, please use the 'Body Object' input|None|test data|
|body_object|object|None|False|Payload to submit to the server when making the HTTP Request call|None|{"user": "user@example.com"}|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|
  
Example input:

```
{
  "body_any": "test data",
  "body_object": {
    "user": "user@example.com"
  },
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```  

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|body_object|object|False|Response payload from the server as an object. Note, if the response has invalid object structure (list, string..) plugin will wrap it with object map|{'user': 'user@example.com'}|
|body_string|string|False|Response payload from the server as a string|test data|
|headers|object|False|Response headers from the server|{'Host': 'rapid7.com'}|
|status|integer|False|Status code of the response from the server|200|
  
Example output:

```
{
  "body_object": {
    "user": "user@example.com"
  },
  "body_string": "test data",
  "headers": {
    "Host": "rapid7.com"
  },
  "status": 200
}
```  

#### POST
  
Make a POST request  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|body_any|string|None|False|Payload (string) to submit to the server when making the HTTP Request call. This can be any type of input, such as an array or integers etc.. If a data object is to be sent, please use the 'Body Object' input|None|test data|
|body_object|object|None|False|Payload to submit to the server when making the HTTP Request call|None|{"user": "user@example.com"}|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|
  
Example input:

```
{
  "body_any": "test data",
  "body_object": {
    "user": "user@example.com"
  },
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```  

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|body_object|object|False|Response payload from the server as an object. Note, if the response has invalid object structure (list, string..) plugin will wrap it with object map|{'user': 'user@example.com'}|
|body_string|string|False|Response payload from the server as a string|test data|
|headers|object|False|Response headers from the server|{'Host': 'rapid7.com'}|
|status|integer|False|Status code of the response from the server|200|
  
Example output:

```
{
  "body_object": {
    "user": "user@example.com"
  },
  "body_string": "test data",
  "headers": {
    "Host": "rapid7.com"
  },
  "status": 200
}
```  

#### PUT
  
Make a PUT request  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|body_any|string|None|False|Payload (string) to submit to the server when making the HTTP Request call. This can be any type of input, such as an array or integers etc.. If a data object is to be sent, please use the 'Body Object' input|None|test data|
|body_object|object|None|False|Payload to submit to the server when making the HTTP Request call|None|{"user": "user@example.com"}|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|
  
Example input:

```
{
  "body_any": "test data",
  "body_object": {
    "user": "user@example.com"
  },
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```  

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|body_object|object|False|Response payload from the server as an object. Note, if the response has invalid object structure (list, string..) plugin will wrap it with object map|{'user': 'user@example.com'}|
|body_string|string|False|Response payload from the server as a string|test data|
|headers|object|False|Response headers from the server|{'Host': 'rapid7.com'}|
|status|integer|False|Status code of the response from the server|200|
  
Example output:

```
{
  "body_object": {
    "user": "user@example.com"
  },
  "body_string": "test data",
  "headers": {
    "Host": "rapid7.com"
  },
  "status": 200
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*  

### Custom Types
  
*This plugin does not contain any custom output types.*  

## Troubleshooting
  
*There is no troubleshooting for this plugin.*  

# Version History
  
*This plugin does not contain a version history.*  

# Links
  

## References
  
*This plugin does not contain any references.*