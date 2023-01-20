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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|asnObject|False|Results containing information about the given ASN|{}|

Example output:

```
{
  "results": {
    "handle": "AS12345",
    "startAutnum": 12345,
    "endAutnum": 12345,
    "name": "AS12345",
    "entities": [
      {
        "handle": "AS12345-MNT",
        "roles": [ "registrant" ],
        "objectClassName": "entity"
      }
    ],
    "links": [
      {
        "value": "https://rdap.db.ripe.net/autnum/12345",
        "rel": "self",
        "href": "https://rdap.db.ripe.net/autnum/12345"
      }
    ],
    "events": [
      {
        "eventAction": "last changed",
        "eventDate": "2020-05-13T13:44:31Z"
      }
    ],
    "notices": [
      {
        "title": "Terms and Conditions",
        "description": [ "This is the description..." ],
        "links": [
          {
            "value": "https://rdap.db.ripe.net/autnum/12345",
            "rel": "terms-of-service",
            "href": "http://www.ripe.net/db/support/example.pdf",
            "type": "application/pdf"
          }
        ]
      }
    ],
    "port43": "whois.ripe.net",
    "objectClassName": "autnum"
  }
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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|domainObject|False|Results containing information about the given domain|{}|

Example output:

```
{
  "results": {
    "objectClassName": "domain",
    "handle": "2336799_DOMAIN_COM-VRSN",
    "ldhName": "EXAMPLE.COM",
    "links": [
      {
        "value": "https://rdap.verisign.com/com/v1/domain/EXAMPLE.COM",
        "rel": "self",
        "href": "https://rdap.verisign.com/com/v1/domain/EXAMPLE.COM",
        "type": "application/rdap+json"
      }
    ],
    "status": [
      "client delete prohibited",
      "client transfer prohibited",
      "client update prohibited"
    ],
    "entities": [
      {
        "objectClassName": "entity",
        "handle": "376",
        "roles": [
          "registrar"
        ],
        "publicIds": [
          {
            "type": "IANA Registrar ID",
            "identifier": "376"
          }
        ],
        "vcardArray": [
          "vcard",
          [
            [
              "version",
              {},
              "text",
              "4.0"
            ],
            [
              "fn",
              {},
              "text",
              "RESERVED-Internet Assigned Numbers Authority"
            ]
          ]
        ],
        "entities": [
          {
            "objectClassName": "entity",
            "roles": [
              "abuse"
            ],
            "vcardArray": [
              "vcard",
              [
                [
                  "version",
                  {},
                  "text",
                  "4.0"
                ],
                [
                  "fn",
                  {},
                  "text",
                  ""
                ],
                [
                  "tel",
                  {
                    "type": "voice"
                  },
                  "uri",
                  ""
                ],
                [
                  "email",
                  {},
                  "text",
                  ""
                ]
              ]
            ]
          }
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
    "secureDNS": {
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
      {
        "objectClassName": "nameserver",
        "ldhName": "A.IANA-SERVERS.NET"
      },
      {
        "objectClassName": "nameserver",
        "ldhName": "B.IANA-SERVERS.NET"
      }
    ],
    "rdapConformance": [
      "rdap_level_0",
      "icann_rdap_technical_implementation_guide_0",
      "icann_rdap_response_profile_0"
    ],
    "notices": [
      {
        "title": "Terms of Use",
        "description": [
          "Service subject to Terms of Use."
        ],
        "links": [
          {
            "href": "https://www.verisign.com/domain-names/registration-data-access-protocol/terms-service/index.xhtml",
            "type": "text/html"
          }
        ]
      },
      {
        "title": "Status Codes",
        "description": [
          "For more information on domain status codes, please visit https://icann.org/epp"
        ],
        "links": [
          {
            "href": "https://icann.org/epp",
            "type": "text/html"
          }
        ]
      },
      {
        "title": "RDDS Inaccuracy Complaint Form",
        "description": [
          "URL of the ICANN RDDS Inaccuracy Complaint Form: https://icann.org/wicf"
        ],
        "links": [
          {
            "href": "https://icann.org/wicf",
            "type": "text/html"
          }
        ]
      }
    ]
  }
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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|ipAddressObject|False|Results containing information about the given IP address|{}|

Example output:

```
{
  "results:": {
    "rdapConformance": [
      "history_version_0",
      "nro_rdap_profile_0",
      "cidr0",
      "rdap_level_0"
    ],
    "notices": [
      {
        "title": "Terms and Conditions",
        "description": [
          "This is the description..."
        ],
        "links": [
          {
            "value": "https://rdap.apnic.net/ip/1.1.1.1/32",
            "rel": "terms-of-service",
            "href": "http://www.example.net/db/example.html",
            "type": "text/html"
          }
        ]
      }
    ],
    "country": "AU",
    "events": [
      {
        "eventAction": "registration",
        "eventDate": "2011-08-10T23:12:35Z"
      }
    ],
    "name": "APNIC-LABS",
    "remarks": [
      {
        "description": [
          "APNIC and Cloudflare DNS Resolver project",
          "Routed globally by AS13335/Cloudflare",
          "Research prefix for APNIC Labs"
        ],
        "title": "description"
      }
    ],
    "links": [
      {
        "value": "https://rdap.apnic.net/ip/1.1.1.1/32",
        "rel": "self",
        "href": "https://rdap.apnic.net/ip/1.1.1.0/24",
        "type": "application/rdap+json"
      }
    ],
    "status": [
      "active"
    ],
    "type": "ASSIGNED PORTABLE",
    "endAddress": "1.1.1.255",
    "ipVersion": "v4",
    "startAddress": "1.1.1.0",
    "objectClassName": "ip network",
    "handle": "1.1.1.0 - 1.1.1.255",
    "entities": [
      {
        "roles": [
          "registrant"
        ],
        "events": [
          {
            "eventAction": "last changed",
            "eventDate": "2017-10-11T01:28:39Z"
          }
        ],
        "links": [
          {
            "value": "https://rdap.apnic.net/ip/1.1.1.1/32",
            "rel": "self",
            "href": "https://rdap.apnic.net/entity/ORG-ARAD1-AP",
            "type": "application/rdap+json"
          }
        ],
        "objectClassName": "entity",
        "handle": "ORG-ARAD1-AP"
      }
    ],
    "port43": "whois.apnic.net",
    "asn": "15169",
    "asnCidr": "1.1.1.1/24",
    "asnCountryCode": "US",
    "asnDate": "2007-03-13",
    "asnDescription": "Example description",
    "asnRegistry": "arin"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### asEventActor

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Event Action|string|False|The reason for the event|
|Event Date|string|False|The time and date the event occurred|

#### asnObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Country|string|False|The two-character country code of the autnum|
|End Autnum|integer|False|The ending number in the block of Autonomous System numbers|
|Entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|
|Events|[]event|False|List of events that have occurred|
|Handle|string|False|The RIR-unique identifier of the autnum registration|
|Links|[]link|False|Links|
|Name|string|False|The identifier assigned to the autnum registration by the registration holder|
|Object Class Name|string|False|The type of object being processed|
|Port 43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|
|Remarks|[]notice|False|Information about the object class|
|StartAutnum|integer|False|The starting number in the block of Autonomous System numbers|
|Status|[]string|False|The state of the autnum|
|Type|string|False|The RIR-specific classification of the autnum per that RIR's registration model|

#### asnResult

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ASN|string|False|Globally unique identifier used for routing information exchange with Autonomous Systems|
|CIDR|string|False|Network routing block assigned to an ASN|
|Country Code|string|False|ASN assigned country code in ISO 3166-1 format|
|Date|string|False|ASN allocation date in ISO 8601 format|
|Description|string|False|The ASN description|
|Registry|string|False|ASN assigned regional internet registry|

#### domainObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|
|Events|[]event|False|List of events that have occurred|
|Handle|string|False|The registry-unique identifier of the domain object instance|
|LDH Name|string|False|The LDH name of the domain|
|Links|[]link|False|Links|
|Nameservers|[]nameserver|False|List of nameservers|
|Network|[]ipAddressObject|False|Network|
|Notices|[]notice|False|Information about the service providing RDAP information and/or information about the entire response|
|Object Class Name|string|False|The type of object being processed|
|Port 43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|
|Public IDs|[]publicId|False|List of public IDs|
|RDAP Conformance|[]string|False|RDAP conformance|
|Remarks|[]notice|False|Information about the object class|
|Secure DNS|secureDns|False|Secure DNS|
|Status|[]string|False|The state of the IP network|
|Unicode Name|string|False|The unicode name of the domain|
|Variants|[]variant|False|List of variants|

#### dsData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Algorithm|integer|False|The algorithm field of a DNS DS record|
|Digest|string|False|The digest field of a DNS DS record|
|Digest Type|integer|False|The digest type field of a DNS DS record|
|Events|[]event|False|Events|
|Key Tag|integer|False|The key tag field of a DNS DS record|
|Links|[]link|False|Links|

#### entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|As Event Actor|[]asEventActor|False|As event actor|
|Entities|[]object|False|Entities|
|Events|[]event|False|Events|
|Handle|string|False|The registry-unique identifier of the entity|
|Links|[]link|False|Links|
|Object Class Name|string|False|The type of object being processed|
|Port 43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|
|Public IDs|[]publicId|False|List of public IDs|
|Remarks|[]notice|False|Information about the object class|
|Roles|[]string|False|List of roles|
|Status|[]string|False|The state of the entity|

#### event

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Event Action|string|False|The reason for the event|
|Event Actor|string|False|The actor responsible for the event|
|Event Date|string|False|The time and date the event occurred|

#### ipAddressObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Country|string|False|The two-character country code of the network|
|End Address|string|False|The ending IP address of the network, either IPv4 or IPv6|
|Entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|
|Events|[]event|False|List of events that have occurred|
|Handle|string|False|The RIR-unique identifier of the network registration|
|IP Version|string|False|The IP protocol version of the network, 'v4' signifies an IPv4 network, and 'v6' signifies an IPv6 network|
|Links|[]link|False|Links|
|Name|string|False|The identifier assigned to the network registration by the registration holder|
|Notices|[]notice|False|Information about the service providing RDAP information and/or information about the entire response|
|Object Class Name|string|False|The type of object being processed|
|Parent Handle|string|False|The RIR-unique identifier of the parent network of this network registration|
|Port 43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|
|RDAP Conformance|[]string|False|RDAP conformance|
|Remarks|[]notice|False|Information about the object class|
|Start Address|string|False|The starting IP address of the network, either IPv4 or IPv6|
|Status|[]string|False|The state of the IP network|
|Type|string|False|The RIR-specific classification of the network per that RIR's registration model|

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
|Links|[]link|False|Links|
|Protocol|integer|False|The protocol field value of the DNSKEY record|
|Public Key|string|False|The public key in the DNSKEY record|

#### link

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Href|string|False|Href|
|Rel|string|False|Rel|
|Type|string|False|Type|
|Value|string|False|Value|

#### nameserver

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Entities|[]entity|False|Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people|
|Events|[]event|False|List of events that have occurred|
|Handle|string|False|The registry-unique identifier of the nameserver|
|IP Addresses|ipAddresses|False|IP addresses|
|LDH Name|string|False|The LDH name of the nameserver|
|Links|[]link|False|Links|
|Object Class Name|string|False|The type of object being processed|
|Port 43|string|False|The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found|
|Remarks|[]notice|False|Information about the object class|
|Status|[]string|False|The state of the nameserver|
|Unicode Name|string|False|The DNS Unicode name of the nameserver|

#### notice

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|[]string|False|Description|
|Links|[]link|False|Links|
|Title|string|False|Title|

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

* 1.0.0 - Initial plugin - Actions: `Domain Lookup`, `IP Address Lookup`, `ASN Lookup`

# Links

* [RDAP](https://rdap.org)

## References

* [RDAP](https://rdap.org)
* [ipwhois](https://ipwhois.readthedocs.io/en/latest/index.html)
