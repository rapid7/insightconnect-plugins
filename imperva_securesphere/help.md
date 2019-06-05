
# Imperva SecureSphere

## About

[Imperva SecureSphere](https://www.imperva.com/Products/WebApplicationFirewall-WAF) is a web application firewall that analyzes all user access to your business-critical web applications and protects your applications and data from cyber attacks.
This plugin utilizes the API builting to Impervase SecureSphere appliance.

## Actions

### Upload SSL Certificate

This action is used to upload a SSL certificate to your SecureSphere server.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sslkeyname|string|None|True|The name of the SSL Key to create be added|None|
|pkcs12password|password|None|False|PKCS12 file password|None|
|certificate|bytes|None|False|Base64 encoded PEM certificate, enclosed between '-----BEGIN CERTIFICATE-----' and '-----END CERTIFICATE-----'|None|
|format|string|None|True|Certificate format type|['pem', 'pkcs12']|
|sitename|string|None|True|The name of the parent site of the web service to access|None|
|servergroupname|string|None|True|The name of the parent server group of the web service to access|None|
|private|bytes|None|False|Base64 encoded PEM certificate, enclosed between '-----BEGIN PRIVATE-----' and '----- END PRIVATE-----'|None|
|hsm|boolean|False|False|Is certificate used by HSM|None|
|pkcs12file|bytes|None|False|PKCS12 file content|None|
|webservicename|string|None|True|The name of the web service to access|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Username and password|None|
|url|string|None|False|URL to SecureSphere Server|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Upload SSL certificates

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types

## References

* [Imperva SecureSphere](https://www.imperva.com/Products/WebApplicationFirewall-WAF)
