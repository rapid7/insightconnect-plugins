# Description

The Registration Data Access Protocol (RDAP) is the successor to WHOIS. Like WHOIS, RDAP provides access to information about Internet resources (domain names, autonomous system numbers, and IP addresses)

# Key Features

* IP Lookup
* Domain Lookup
* ASN Lookup

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions

* RDAP 20-12-2022

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### ASN Lookup

This action is used to perform an ASN (autonomous system number) lookup.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|asn|integer|None|True|Autonomous system number for which information will be searched|None|12345|

Example input:

```
{
  "asn": 12345
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|country|string|False|The two-character country code of the autonomous number|
|endAutnum|integer|False|The ending number in the block of Autonomous System numbers|
|entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|
|events|[]event|False|List of events that have occurred|
|handle|string|False|The RIR-unique identifier of the autnum registration|
|name|string|False|The identifier assigned to the autonomous number registration by the registration holder|
|port43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|
|startAutnum|integer|False|The starting number in the block of Autonomous System numbers|
|status|[]string|False|The state of the autnum|
|type|string|False|The RIR-specific classification of the autonomous number per that RIR's registration model|

Example output:

```
{
  "handle": "AS12345",
  "startAutnum": 12345,
  "endAutnum": 12345,
  "name": "AS12345",
  "events": [
    {
      "eventAction": "last changed",
      "eventDate": "2020-05-13T13:44:31Z"
    }
  ],
  "entities": [
    {
      "roles": [
        "registrant"
      ],
      "handle": "RIPE-NCC-END-MNT"
    },
    {
      "roles": [
        "administrative"
      ],
      "handle": "PG12821-RIPE"
    },
    {
      "roles": [
        "registrant"
      ],
      "handle": "ORG-GSs1-RIPE"
    },
    {
      "roles": [
        "technical",
        "administrative"
      ],
      "handle": "LG1196-ORG"
    },
    {
      "roles": [
        "registrant"
      ],
      "handle": "AS12345-MNT"
    }
  ],
  "port43": "whois.ripe.net"
}
```

#### Domain Lookup

This action is used to perform a domain lookup.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain for which information will be searched|None|example.com|

Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|
|events|[]event|False|List of events that have occurred|
|name|string|False|The LDH name of the domain|
|nameservers|[]string|False|List of nameservers|
|port43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|
|publicIds|[]publicId|False|List of public IDs|
|registryDomainId|string|False|The registry-unique identifier of the domain object instance|
|secureDns|secureDns|False|Secure DNS|
|status|[]string|False|The state of the IP network|
|unicodeName|string|False|The unicode name of the domain|
|variants|[]variant|False|List of variants|

Example output:

```
{
  "name": "EXAMPLE.COM",
  "registryDomainId": "2336799_DOMAIN_COM-VRSN",
  "status": [
    "client delete prohibited",
    "client transfer prohibited",
    "client update prohibited"
  ],
  "entities": [
    {
      "roles": [
        "registrar"
      ],
      "handle": "376",
      "fullname": "RESERVED-Internet Assigned Numbers Authority"
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
  "publicIds": [
    {
      "type": "IANA Registrar ID",
      "identifier": "376"
    }
  ],
  "secureDns": {
    "delegationSigned": true,
    "dsData": [
      {
        "keyTag": 31406,
        "algorithm": 8,
        "digestType": 2,
        "digest": "F78CF3344F72137235098ECBBD08947C2C9001C7F6A085A17F518B5D8F6B916D"
      },
      {
        "keyTag": 31589,
        "algorithm": 8,
        "digestType": 2,
        "digest": "CDE0D742D6998AA554A92D890F8184C698CFAC8A26FA59875A990C03E576343C"
      },
      {
        "keyTag": 43547,
        "algorithm": 8,
        "digestType": 1,
        "digest": "B6225AB2CC613E0DCA7962BDC2342EA4F1B56083"
      },
      {
        "keyTag": 43547,
        "algorithm": 8,
        "digestType": 2,
        "digest": "615A64233543F66F44D68933625B17497C89A70E858ED76A2145997EDF96A918"
      },
      {
        "keyTag": 31589,
        "algorithm": 8,
        "digestType": 1,
        "digest": "3490A6806D47F17A34C29E2CE80E8A999FFBE4BE"
      },
      {
        "keyTag": 31406,
        "algorithm": 8,
        "digestType": 1,
        "digest": "189968811E6EBA862DD6C209F75623D8D9ED9142"
      }
    ]
  },
  "nameservers": [
    "A.IANA-SERVERS.NET",
    "B.IANA-SERVERS.NET"
  ]
}
```

#### IP Address Lookup

This action is used to perform an IP address lookup.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|getAsn|boolean|None|True|Whether to return ASN information|None|True|
|ipAddress|string|None|True|IP address for which information will be searched|None|1.1.1.1|

Example input:

```
{
  "getAsn": true,
  "ipAddress": "1.1.1.1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ansCountryCode|string|False|ASN country code|
|ansRegistry|string|False|ASN registry|
|asn|string|False|ASN|
|asnCidr|string|False|ASN CIDR|
|asnDate|string|False|ASN date|
|asnDescription|string|False|ASN description|
|country|string|False|The two-character country code of the network|
|endAddress|string|False|The ending IP address of the network, either IPv4 or IPv6|
|entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|
|events|[]event|False|List of events that have occurred|
|handle|string|False|The RIR-unique identifier of the network registration|
|ipVersion|string|False|The IP protocol version of the network, 'v4' signifies an IPv4 network, and 'v6' signifies an IPv6 network|
|name|string|False|The identifier assigned to the network registration by the registration holder|
|parentHandle|string|False|The RIR-unique identifier of the parent network of this network registration|
|port43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|
|startAddress|string|False|The starting IP address of the network, either IPv4 or IPv6|
|status|[]string|False|The state of the IP network|
|type|string|False|The RIR-specific classification of the network per that RIR's registration model|

Example output:

```
{
  "asn": "3215",
  "asnCidr": "2.2.0.0/16",
  "ansCountryCode": "FR",
  "asnDate": "2010-07-12",
  "asnDescription": "France Telecom - Orange, FR",
  "ansRegistry": "ripencc",
  "handle": "2.0.0.0 - 2.15.255.255",
  "startAddress": "2.0.0.0",
  "endAddress": "2.15.255.255",
  "ipVersion": "v4",
  "name": "FR-TELECOM-20100712",
  "type": "ALLOCATED PA",
  "country": "FR",
  "parentHandle": "0.0.0.0 - 255.255.255.255",
  "entities": [
    {
      "roles": [
        "registrant"
      ],
      "handle": "FT-BRX"
    }
  ],
  "events": [
    {
      "eventAction": "last changed",
      "eventDate": "2017-04-10T14:16:37Z"
    }
  ],
  "port43": "whois.ripe.net"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### address

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Country Name|string|False|The country name of the entity|
|Extended Address|string|False|The entity extended address|
|Locality|string|False|The location of the entity|
|Post Office Box|string|False|The entity post office box|
|Postal Code|string|False|The entity's postal code|
|Region|string|False|The entity's region|
|Street Address|string|False|The entity's street address|

#### dsData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Algorithm|integer|False|The algorithm field of a DNS DS record|
|Digest|string|False|The digest field of a DNS DS record|
|Digest Type|integer|False|The digest type field of a DNS DS record|
|Key Tag|integer|False|The key tag field of a DNS DS record|

#### entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Address|address|False|The address of the entity|
|Fullname|string|False|The entity fullname|
|Handle|string|False|The registry-unique identifier of the nameserver|
|Kind|string|False|None|
|Language|string|False|Information about the language of the entity|
|Organization|string|False|Name of the organization|
|Phone|string|False|The entity phone number|
|Role|string|False|The role of the entity|
|Roles|[]string|False|List of roles|
|Title|string|False|The title of the entity|

#### event

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Event Action|string|False|The reason for the event|
|Event Actor|string|False|The actor responsible for the event|
|Event Date|string|False|The time and date the event occurred|

#### ipAddresses

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IPv4|[]string|False|IPv4 addresses of the nameserver|
|IPv6|[]string|False|IPv6 addresses of the nameserver|

#### keyData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Algorithm|integer|False|The algorithm field of a DNSKEY record|
|Events|[]event|False|Events|
|Flags|integer|False|The flags field value in the DNSKEY record|
|Protocol|integer|False|The protocol field value of the DNSKEY record|
|Public Key|string|False|The public key in the DNSKEY record|

#### nameserver

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Handle|string|False|The registry-unique identifier of the nameserver|
|IP Addresses|ipAddresses|False|IP addresses|
|LDH Name|string|False|The LDH name of the nameserver|
|Port 43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|
|Unicode Name|string|False|The DNS Unicode name of the nameserver|

#### publicId

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Identifier|string|False|The public identifier of the type related to 'type'|
|Type|string|False|The type of public identifier|

#### secureDns

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Delegation Signed|boolean|False|Whether there are DS records in the parent|
|DS Data|[]dsData|False|DS Data|
|Key Data|[]keyData|False|Key Data|
|Zone Signed|boolean|False|Whether the zone has been signed|

#### variant

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IDN Table|string|False|The Internationalized Domain Name (IDN) table that has been registered in the IANA Repository of IDN Practices|
|Relation|[]string|False|The relationship between the variants and the containing domain object|
|Variant Names|[]variantName|False|List of variant names|

#### variantName

|Name|Type|Required|Description|
|----|----|--------|-----------|
|LDH Name|string|False|The LDH name of the domain|
|Unicode Name|string|False|The unicode name of the domain|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - `Domain Lookup`, `IP Address Lookup`, `ASN Lookup`: Updated action outputs and refactored
* 1.0.0 - Initial plugin - Actions: `Domain Lookup`, `IP Address Lookup`, `ASN Lookup`

# Links

* [RDAP](https://rdap.org)

## References

* [RDAP](https://rdap.org)
* [ipwhois](https://ipwhois.readthedocs.io/en/latest/index.html)
