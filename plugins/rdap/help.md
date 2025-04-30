# Description

The Registration Data Access Protocol (RDAP) is the successor to WHOIS. Like WHOIS, RDAP provides access to information about Internet resources (domain names, autonomous system numbers, and IP addresses)

# Key Features

* IP Lookup
* Domain Lookup
* ASN Lookup

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* RDAP 20-12-2022

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### ASN Lookup

This action is used to perform an ASN (autonomous system number) lookup

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asn|integer|None|True|Autonomous system number for which information will be searched|None|12345|None|None|
  
Example input:

```
{
  "asn": 12345
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|country|string|False|The two-character country code of the autonomous number|US|
|endAutnum|integer|False|The ending number in the block of Autonomous System numbers|12345|
|entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|[{"roles":["registrant"],"handle":"RIPE-NCC-END-MNT"},{"roles":["administrative"],"handle":"PG12821-RIPE"},{"roles":["registrant"],"handle":"ORG-GSs1-RIPE"},{"roles":["technical","administrative"],"handle":"LG1196-ORG"},{"roles":["registrant"],"handle":"AS12345-MNT"}]|
|events|[]event|False|List of events that have occurred|[{"eventAction":"last changed","eventDate":"2020-05-13T13:44:31Z"}]|
|handle|string|False|The RIR-unique identifier of the autnum registration|AS12345|
|name|string|False|The identifier assigned to the autonomous number registration by the registration holder|AS12345|
|port43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|whois.ripe.net|
|startAutnum|integer|False|The starting number in the block of Autonomous System numbers|12345|
|status|[]string|False|The state of the autnum|["client delete prohibited","client transfer prohibited","client update prohibited"]|
|type|string|False|The RIR-specific classification of the autonomous number per that RIR's registration model|ExampleType|
  
Example output:

```
{
  "country": "US",
  "endAutnum": 12345,
  "entities": [
    {
      "handle": "RIPE-NCC-END-MNT",
      "roles": [
        "registrant"
      ]
    },
    {
      "handle": "PG12821-RIPE",
      "roles": [
        "administrative"
      ]
    },
    {
      "handle": "ORG-GSs1-RIPE",
      "roles": [
        "registrant"
      ]
    },
    {
      "handle": "LG1196-ORG",
      "roles": [
        "technical",
        "administrative"
      ]
    },
    {
      "handle": "AS12345-MNT",
      "roles": [
        "registrant"
      ]
    }
  ],
  "events": [
    {
      "eventAction": "last changed",
      "eventDate": "2020-05-13T13:44:31Z"
    }
  ],
  "handle": "AS12345",
  "name": "AS12345",
  "port43": "whois.ripe.net",
  "startAutnum": 12345,
  "status": [
    "client delete prohibited",
    "client transfer prohibited",
    "client update prohibited"
  ],
  "type": "ExampleType"
}
```

#### Domain Lookup

This action is used to perform a domain lookup

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain for which information will be searched|None|example.com|None|None|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|[{"roles":["registrar"],"handle":"376","fullname":"RESERVED-Internet Assigned Numbers Authority"}]|
|events|[]event|False|List of events that have occurred|[{"eventAction":"registration","eventDate":"1995-08-14T04:00:00Z"},{"eventAction":"expiration","eventDate":"2023-08-13T04:00:00Z"},{"eventAction":"last changed","eventDate":"2022-08-14T07:01:31Z"},{"eventAction":"last update of RDAP database","eventDate":"2022-12-19T13:17:15Z"}]|
|name|string|False|The LDH name of the domain|EXAMPLE.COM|
|nameservers|[]string|False|List of nameservers|["A.IANA-SERVERS.NET","B.IANA-SERVERS.NET"]|
|port43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|whois.ripe.net|
|publicIds|[]publicId|False|List of public IDs|[{"type":"IANA Registrar ID","identifier":"376"}]|
|registryDomainId|string|False|The registry-unique identifier of the domain object instance|2336799_DOMAIN_COM-VRSN|
|secureDns|secureDns|False|Secure DNS|{"delegationSigned":true,"dsData":[{"keyTag":31406,"algorithm":8,"digestType":2,"digest":"F78CF3344F72137235098ECBBD08947C2C9001C7F6A085A17F518B5D8F6B916D"},{"keyTag":31589,"algorithm":8,"digestType":2,"digest":"CDE0D742D6998AA554A92D890F8184C698CFAC8A26FA59875A990C03E576343C"},{"keyTag":43547,"algorithm":8,"digestType":1,"digest":"B6225AB2CC613E0DCA7962BDC2342EA4F1B56083"},{"keyTag":43547,"algorithm":8,"digestType":2,"digest":"615A64233543F66F44D68933625B17497C89A70E858ED76A2145997EDF96A918"},{"keyTag":31589,"algorithm":8,"digestType":1,"digest":"3490A6806D47F17A34C29E2CE80E8A999FFBE4BE"},{"keyTag":31406,"algorithm":8,"digestType":1,"digest":"189968811E6EBA862DD6C209F75623D8D9ED9142"}]}|
|status|[]string|False|The state of the IP network|["client delete prohibited","client transfer prohibited","client update prohibited"]|
|unicodeName|string|False|The unicode name of the domain|ExampleUnicodeName|
|variants|[]variant|False|List of variants|[]|
  
Example output:

```
{
  "entities": [
    {
      "fullname": "RESERVED-Internet Assigned Numbers Authority",
      "handle": "376",
      "roles": [
        "registrar"
      ]
    }
  ],
  "events": [
    {
      "eventAction": "registration",
      "eventDate": "1995-08-14T04:00:00Z"
    },
    {
      "eventAction": "expiration",
      "eventDate": "2023-08-13T04:00:00Z"
    },
    {
      "eventAction": "last changed",
      "eventDate": "2022-08-14T07:01:31Z"
    },
    {
      "eventAction": "last update of RDAP database",
      "eventDate": "2022-12-19T13:17:15Z"
    }
  ],
  "name": "EXAMPLE.COM",
  "nameservers": [
    "A.IANA-SERVERS.NET",
    "B.IANA-SERVERS.NET"
  ],
  "port43": "whois.ripe.net",
  "publicIds": [
    {
      "identifier": "376",
      "type": "IANA Registrar ID"
    }
  ],
  "registryDomainId": "2336799_DOMAIN_COM-VRSN",
  "secureDns": {
    "delegationSigned": true,
    "dsData": [
      {
        "algorithm": 8,
        "digest": "F78CF3344F72137235098ECBBD08947C2C9001C7F6A085A17F518B5D8F6B916D",
        "digestType": 2,
        "keyTag": 31406
      },
      {
        "algorithm": 8,
        "digest": "CDE0D742D6998AA554A92D890F8184C698CFAC8A26FA59875A990C03E576343C",
        "digestType": 2,
        "keyTag": 31589
      },
      {
        "algorithm": 8,
        "digest": "B6225AB2CC613E0DCA7962BDC2342EA4F1B56083",
        "digestType": 1,
        "keyTag": 43547
      },
      {
        "algorithm": 8,
        "digest": "615A64233543F66F44D68933625B17497C89A70E858ED76A2145997EDF96A918",
        "digestType": 2,
        "keyTag": 43547
      },
      {
        "algorithm": 8,
        "digest": "3490A6806D47F17A34C29E2CE80E8A999FFBE4BE",
        "digestType": 1,
        "keyTag": 31589
      },
      {
        "algorithm": 8,
        "digest": "189968811E6EBA862DD6C209F75623D8D9ED9142",
        "digestType": 1,
        "keyTag": 31406
      }
    ]
  },
  "status": [
    "client delete prohibited",
    "client transfer prohibited",
    "client update prohibited"
  ],
  "unicodeName": "ExampleUnicodeName",
  "variants": []
}
```

#### IP Address Lookup

This action is used to perform an IP address lookup

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|getAsn|boolean|None|True|Whether to return ASN information|None|True|None|None|
|ipAddress|string|None|True|IP address for which information will be searched|None|1.1.1.1|None|None|
  
Example input:

```
{
  "getAsn": true,
  "ipAddress": "1.1.1.1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ansCountryCode|string|False|ASN country code|FR|
|ansRegistry|string|False|ASN registry|ripencc|
|asn|string|False|ASN|3215|
|asnCidr|string|False|ASN CIDR|2.2.0.0/16|
|asnDate|string|False|ASN date|2010-07-12|
|asnDescription|string|False|ASN description|France Telecom - Orange, FR|
|country|string|False|The two-character country code of the network|FR|
|endAddress|string|False|The ending IP address of the network, either IPv4 or IPv6|2.15.255.255|
|entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|[{"roles":["registrant"],"handle":"FT-BRX"}]|
|events|[]event|False|List of events that have occurred|[{"eventAction":"last changed","eventDate":"2017-04-10T14:16:37Z"}]|
|handle|string|False|The RIR-unique identifier of the network registration|2.0.0.0 - 2.15.255.255|
|ipVersion|string|False|The IP protocol version of the network, 'v4' signifies an IPv4 network, and 'v6' signifies an IPv6 network|v4|
|name|string|False|The identifier assigned to the network registration by the registration holder|FR-TELECOM-20100712|
|parentHandle|string|False|The RIR-unique identifier of the parent network of this network registration|0.0.0.0 - 255.255.255.255|
|port43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|whoios.ripe.net|
|startAddress|string|False|The starting IP address of the network, either IPv4 or IPv6|2.0.0.0|
|status|[]string|False|The state of the IP network|["client delete prohibited","client transfer prohibited","client update prohibited"]|
|type|string|False|The RIR-specific classification of the network per that RIR's registration model|ALLOCATED PA|
  
Example output:

```
{
  "ansCountryCode": "FR",
  "ansRegistry": "ripencc",
  "asn": 3215,
  "asnCidr": "2.2.0.0/16",
  "asnDate": "2010-07-12",
  "asnDescription": "France Telecom - Orange, FR",
  "country": "FR",
  "endAddress": "2.15.255.255",
  "entities": [
    {
      "handle": "FT-BRX",
      "roles": [
        "registrant"
      ]
    }
  ],
  "events": [
    {
      "eventAction": "last changed",
      "eventDate": "2017-04-10T14:16:37Z"
    }
  ],
  "handle": "2.0.0.0 - 2.15.255.255",
  "ipVersion": "v4",
  "name": "FR-TELECOM-20100712",
  "parentHandle": "0.0.0.0 - 255.255.255.255",
  "port43": "whoios.ripe.net",
  "startAddress": "2.0.0.0",
  "status": [
    "client delete prohibited",
    "client transfer prohibited",
    "client update prohibited"
  ],
  "type": "ALLOCATED PA"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**variantName**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|LDH Name|string|None|False|The LDH name of the domain|None|
|Unicode Name|string|None|False|The unicode name of the domain|None|
  
**variant**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IDN Table|string|None|False|The Internationalized Domain Name (IDN) table that has been registered in the IANA Repository of IDN Practices|None|
|Relation|[]string|None|False|The relationship between the variants and the containing domain object|None|
|Variant Names|[]variantName|None|False|List of variant names|None|
  
**ipAddresses**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IPv4|[]string|None|False|IPv4 addresses of the nameserver|None|
|IPv6|[]string|None|False|IPv6 addresses of the nameserver|None|
  
**event**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Event Action|string|None|False|The reason for the event|None|
|Event Actor|string|None|False|The actor responsible for the event|None|
|Event Date|string|None|False|The time and date the event occurred|None|
  
**publicId**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Identifier|string|None|False|The public identifier of the type related to 'type'|None|
|Type|string|None|False|The type of public identifier|None|
  
**address**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Country Name|string|None|False|The country name of the entity|None|
|Extended Address|string|None|False|The entity extended address|None|
|Locality|string|None|False|The location of the entity|None|
|Post Office Box|string|None|False|The entity post office box|None|
|Postal Code|string|None|False|The entity's postal code|None|
|Region|string|None|False|The entity's region|None|
|Street Address|string|None|False|The entity's street address|None|
  
**entity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Address|address|None|False|The address of the entity|None|
|Fullname|string|None|False|The entity fullname|None|
|Handle|string|None|False|The registry-unique identifier of the nameserver|None|
|Kind|string|None|False|The kind of the entity|None|
|Language|string|None|False|Information about the language of the entity|None|
|Organization|string|None|False|Name of the organization|None|
|Phone|string|None|False|The entity phone number|None|
|Role|string|None|False|The role of the entity|None|
|Roles|[]string|None|False|List of roles|None|
|Title|string|None|False|The title of the entity|None|
  
**nameserver**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Handle|string|None|False|The registry-unique identifier of the nameserver|None|
|IP Addresses|ipAddresses|None|False|IP addresses|None|
|LDH Name|string|None|False|The LDH name of the nameserver|None|
|Port 43|string|None|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|None|
|Unicode Name|string|None|False|The DNS Unicode name of the nameserver|None|
  
**dsData**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Algorithm|integer|None|False|The algorithm field of a DNS DS record|None|
|Digest|string|None|False|The digest field of a DNS DS record|None|
|Digest Type|integer|None|False|The digest type field of a DNS DS record|None|
|Key Tag|integer|None|False|The key tag field of a DNS DS record|None|
  
**keyData**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Algorithm|integer|None|False|The algorithm field of a DNSKEY record|None|
|Events|[]event|None|False|Events|None|
|Flags|integer|None|False|The flags field value in the DNSKEY record|None|
|Protocol|integer|None|False|The protocol field value of the DNSKEY record|None|
|Public Key|string|None|False|The public key in the DNSKEY record|None|
  
**secureDns**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Delegation Signed|boolean|None|False|Whether there are DS records in the parent|None|
|DS Data|[]dsData|None|False|DS Data|None|
|Key Data|[]keyData|None|False|Key Data|None|
|Zone Signed|boolean|None|False|Whether the zone has been signed|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.6 - Updated SDK to the latest version (6.3.3)
* 2.0.5 - Updated SDK to the latest version (6.2.5)
* 2.0.4 - Updated SDK to the latest version (v6.2.2) | Address vulnerabilities
* 2.0.3 - Bumping requirements.txt | SDK Bump to 6.1.4
* 2.0.2 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 2.0.1 - Updated SDK to the latest version
* 2.0.0 - `Domain Lookup`, `IP Address Lookup`, `ASN Lookup`: Updated action outputs and refactored
* 1.0.0 - Initial plugin - Actions: `Domain Lookup`, `IP Address Lookup`, `ASN Lookup`

# Links

* [RDAP](https://rdap.org)

## References

* [RDAP](https://rdap.org)
* [ipwhois](https://ipwhois.readthedocs.io/en/latest/index.html)