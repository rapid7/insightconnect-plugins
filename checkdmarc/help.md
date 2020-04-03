# Description

[Checkdmarc](https://domainaware.github.io/checkdmarc/) is a Python module and command line parser for SPF and DMARC records. The checkdmarc plugin is used to parse SPF and DMARC records.

# Key Features

* Parse DNS records

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Check Domains

This action is used to check domains.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain to check. e.g. fbi.gov, google.com|None|rapid7.com|
|timeout|number|6|True|Timeout in seconds for request. Default is 6 seconds|None|6|

Example input:

```
{
  "domain": "whitehouse.gov",
  "timeout": 10.0
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|report|False|Report|

Example output:

```
{
   "report":{
      "domain":"whitehouse.gov",
      "base_domain":"whitehouse.gov",
      "ns":{
         "hostnames":[
            "a22-66.akam.net",
            "ns1-145.akam.net",
            "ns1-176.akam.net",
            "zc.akam.net",
            "use6.akam.net",
            "usw1.akam.net",
            "usw5.akam.net",
            "usw6.akam.net",
            "a1-61.akam.net",
            "a3-67.akam.net",
            "a5-64.akam.net",
            "asia9.akam.net",
            "a12-64.akam.net",
            "a20-65.akam.net"
         ],
         "warnings":[

         ]
      },
      "mx":{
         "hosts":[

         ],
         "warnings":[
            "No MX records found. Is the domain parked?"
         ]
      },
      "spf":{
         "record":"v=spf1 +mx include:spf.mandrillapp.com ip4:214.3.140.16/32 ip4:214.3.140.255/32 ip4:214.3.115.12/32 ip4:214.3.115.10/32 ip4:214.3.115.225/32 ip4:214.3.115.14/32 ip4:214.3.140.22/32 ~all",
         "valid":true,
         "dns_lookups":2,
         "warnings":[
            "whitehouse.gov does not have any MX records"
         ],
         "parsed":{
            "pass":[
               {
                  "value":"214.3.140.16/32",
                  "mechanism":"ip4"
               },
               {
                  "value":"214.3.140.255/32",
                  "mechanism":"ip4"
               },
               {
                  "value":"214.3.115.12/32",
                  "mechanism":"ip4"
               },
               {
                  "value":"214.3.115.10/32",
                  "mechanism":"ip4"
               },
               {
                  "value":"214.3.115.225/32",
                  "mechanism":"ip4"
               },
               {
                  "value":"214.3.115.14/32",
                  "mechanism":"ip4"
               },
               {
                  "value":"214.3.140.22/32",
                  "mechanism":"ip4"
               }
            ],
            "neutral":[

            ],
            "softfail":[

            ],
            "fail":[

            ],
            "include":[
               {
                  "domain":"spf.mandrillapp.com",
                  "record":"v=spf1 ip4:198.2.128.0/24 ip4:198.2.132.0/22 ip4:198.2.136.0/23 ip4:198.2.186.0/23 ip4:205.201.131.128/25 ip4:205.201.134.128/25 ip4:205.201.136.0/23 ip4:205.201.139.0/24 ip4:198.2.180.0/24 ip4:198.2.179.0/24 ip4:198.2.178.0/24 ip4:198.2.177.0/24 ~all",
                  "dns_lookups":0,
                  "parsed":{
                     "pass":[
                        {
                           "value":"198.2.128.0/24",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"198.2.132.0/22",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"198.2.136.0/23",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"198.2.186.0/23",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"205.201.131.128/25",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"205.201.134.128/25",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"205.201.136.0/23",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"205.201.139.0/24",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"198.2.180.0/24",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"198.2.179.0/24",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"198.2.178.0/24",
                           "mechanism":"ip4"
                        },
                        {
                           "value":"198.2.177.0/24",
                           "mechanism":"ip4"
                        }
                     ],
                     "neutral":[

                     ],
                     "softfail":[

                     ],
                     "fail":[

                     ],
                     "include":[

                     ],
                     "all":"softfail"
                  },
                  "warnings":[

                  ]
               }
            ],
            "all":"softfail"
         }
      },
      "dmarc":{
         "record":"v=DMARC1;p=none;fo=1;pct=100;rua=mailto:user@example.com,mailto:user@example.com;ruf=mailto:user@example.com",
         "valid":false,
         "location":"whitehouse.gov",
         "error":"mail.pci.gov does not indicate that it accepts DMARC reports about whitehouse.gov - Authorization record not found: whitehouse.gov._report._dmarc.mail.pci.gov IN TXT \"v=DMARC1\""
      }
   }
}
```

#### Check Domains Alternate Nameservers

This action will check DMARC records against alternate name servers.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain to check. e.g. fbi.gov, google.com in alternate nameserver|None|rapid7.com|
|nameservers|[]string|['1.1.1.1', '1.0.0.1']|True|Nameserver to check against|None|["1.1.1.1","1.0.0.1"]|
|timeout|number|6|True|Timeout in seconds for request. Default is 6 seconds|None|6|

Example input:

```
{
  "report": {
    "base_domain": "rapid7.com",
    "dmarc": {
      "location": "rapid7.com",
      "record": "v=DMARC1; p=quarantine; rua=mailto:user@example.com',mailto:user@example.com'",
      "tags": {
        "adkim": {
          "explicit": false,
          "value": "r"
        },
        "aspf": {
          "explicit": false,
          "value": "r"
        },
        "fo": {
          "explicit": false,
          "value": [
            "0"
          ]
        },
        "p": {
          "explicit": true,
          "value": "quarantine"
        },
        "pct": {
          "explicit": false,
          "value": 100
        },
        "rf": {
          "explicit": false,
          "value": [
            "afrf"
          ]
        },
        "ri": {
          "explicit": false,
          "value": 86400
        },
        "rua": {
          "explicit": true,
          "value": [
            {
              "address": "user@example.com'",
              "scheme": "mailto"
            },
            {
              "address": "user@example.com'",
              "scheme": "mailto"
            }
          ]
        },
        "sp": {
          "explicit": false,
          "value": "quarantine"
        },
        "v": {
          "explicit": true,
          "value": "DMARC1"
        }
      },
      "valid": true,
      "warnings": []
    },
    "domain": "rapid7.com",
    "mx": {
      "hosts": [
        {
          "addresses": [
            "2607:f8b0:4001:c07::1a",
            "74.125.69.26"
          ],
          "hostname": "aspmx.l.google.com",
          "preference": 1,
          "starttls": true,
          "tls": true
        },
        {
          "addresses": [
            "173.194.77.26",
            "2607:f8b0:4023:401::1a"
          ],
          "hostname": "alt1.aspmx.l.google.com",
          "preference": 5,
          "starttls": true,
          "tls": true
        },
        {
          "addresses": [
            "2607:f8b0:4002:c08::1b",
            "64.233.177.27"
          ],
          "hostname": "alt2.aspmx.l.google.com",
          "preference": 5,
          "starttls": true,
          "tls": true
        },
        {
          "addresses": [
            "173.194.68.27",
            "2607:f8b0:400d:c0c::1b"
          ],
          "hostname": "alt3.aspmx.l.google.com",
          "preference": 10,
          "starttls": true,
          "tls": true
        },
        {
          "addresses": [
            "173.194.215.27",
            "2607:f8b0:400c:c0c::1a"
          ],
          "hostname": "alt4.aspmx.l.google.com",
          "preference": 10,
          "starttls": true,
          "tls": true
        }
      ],
      "warnings": [
        "The domain 2607:f8b0:4001:c07::1a does not exist",
        "The reverse DNS of 2607:f8b0:4001:c07::1a is 2607:f8b0:4001:c07::1a, but the A/AAAA DNS records for 2607:f8b0:4001:c07::1a do not resolve to 2607:f8b0:4001:c07::1a",
        "The domain 2607:f8b0:4001:c07::1a does not exist",
        "The reverse DNS of 2607:f8b0:4001:c07::1a is 2607:f8b0:4001:c07::1a, but the A/AAAA DNS records for 2607:f8b0:4001:c07::1a do not resolve to 2607:f8b0:4001:c07::1a",
        "The domain 2607:f8b0:4023:401::1a does not exist",
        "The reverse DNS of 2607:f8b0:4023:401::1a is 2607:f8b0:4023:401::1a, but the A/AAAA DNS records for 2607:f8b0:4023:401::1a do not resolve to 2607:f8b0:4023:401::1a",
        "The domain 2607:f8b0:4023:401::1a does not exist",
        "The reverse DNS of 2607:f8b0:4023:401::1a is 2607:f8b0:4023:401::1a, but the A/AAAA DNS records for 2607:f8b0:4023:401::1a do not resolve to 2607:f8b0:4023:401::1a"
      ]
    },
    "ns": {
      "hostnames": [
        "ns-1653.awsdns-14.co.uk",
        "ns-439.awsdns-54.com",
        "ns-739.awsdns-28.net",
        "ns-1390.awsdns-45.org"
      ],
      "warnings": []
    },
    "spf": {
      "dns_lookups": 2,
      "parsed": {
        "all": "softfail",
        "fail": [],
        "include": [
          {
            "dns_lookups": 0,
            "domain": "rapid7.com._nspf.vali.email",
            "parsed": {
              "all": "fail",
              "fail": [],
              "include": [],
              "neutral": [],
              "pass": [],
              "softfail": []
            },
            "record": "v=spf1 -all",
            "warnings": []
          },
          {
            "dns_lookups": 0,
            "domain": "%!{(MISSING)i}._ip.%!{(MISSING)h}._ehlo.%!{(MISSING)d}._spf.vali.email",
            "parsed": {
              "all": "fail",
              "fail": [],
              "include": [],
              "neutral": [],
              "pass": [],
              "softfail": []
            },
            "record": "v=spf1 -all",
            "warnings": []
          }
        ],
        "neutral": [],
        "pass": [],
        "softfail": []
      },
      "record": "v=spf1 include:rapid7.com._nspf.vali.email include:%!{(MISSING)i}._ip.%!{(MISSING)h}._ehlo.%!{(MISSING)d}._spf.vali.email ~all",
      "valid": true,
      "warnings": []
    }
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|report|False|Report|

```
{
  "report": {
    "base_domain": "rapid7.com",
    "dmarc": {
      "location": "rapid7.com",
      "record": "v=DMARC1; p=quarantine; rua=mailto:user@example.com',mailto:user@example.com'",
      "tags": {
        "adkim": {
          "explicit": false,
          "value": "r"
        },
        "aspf": {
          "explicit": false,
          "value": "r"
        },
        "fo": {
          "explicit": false,
          "value": [
            "0"
          ]
        },
        "p": {
          "explicit": true,
          "value": "quarantine"
        },
        "pct": {
          "explicit": false,
          "value": 100
        },
        "rf": {
          "explicit": false,
          "value": [
            "afrf"
          ]
        },
        "ri": {
          "explicit": false,
          "value": 86400
        },
        "rua": {
          "explicit": true,
          "value": [
            {
              "address": "user@example.com'",
              "scheme": "mailto"
            },
            {
              "address": "user@example.com'",
              "scheme": "mailto"
            }
          ]
        },
        "sp": {
          "explicit": false,
          "value": "quarantine"
        },
        "v": {
          "explicit": true,
          "value": "DMARC1"
        }
      },
      "valid": true,
      "warnings": []
    },
    "domain": "rapid7.com",
    "mx": {
      "hosts": [
        {
          "addresses": [
            "2607:f8b0:4001:c07::1a",
            "74.125.132.26"
          ],
          "hostname": "aspmx.l.google.com",
          "preference": 1,
          "starttls": true,
          "tls": true
        },
        {
          "addresses": [
            "173.194.77.26",
            "2607:f8b0:4023:401::1a"
          ],
          "hostname": "alt1.aspmx.l.google.com",
          "preference": 5,
          "starttls": true,
          "tls": true
        },
        {
          "addresses": [
            "2607:f8b0:4002:c08::1b",
            "64.233.177.27"
          ],
          "hostname": "alt2.aspmx.l.google.com",
          "preference": 5,
          "starttls": true,
          "tls": true
        },
        {
          "addresses": [
            "173.194.68.27",
            "2607:f8b0:400d:c0c::1b"
          ],
          "hostname": "alt3.aspmx.l.google.com",
          "preference": 10,
          "starttls": true,
          "tls": true
        },
        {
          "addresses": [
            "173.194.215.27",
            "2607:f8b0:400c:c0c::1a"
          ],
          "hostname": "alt4.aspmx.l.google.com",
          "preference": 10,
          "starttls": true,
          "tls": true
        }
      ],
      "warnings": [
        "The domain 2607:f8b0:4001:c07::1a does not exist",
        "The reverse DNS of 2607:f8b0:4001:c07::1a is 2607:f8b0:4001:c07::1a, but the A/AAAA DNS records for 2607:f8b0:4001:c07::1a do not resolve to 2607:f8b0:4001:c07::1a",
        "The domain 2607:f8b0:4001:c07::1a does not exist",
        "The reverse DNS of 2607:f8b0:4001:c07::1a is 2607:f8b0:4001:c07::1a, but the A/AAAA DNS records for 2607:f8b0:4001:c07::1a do not resolve to 2607:f8b0:4001:c07::1a",
        "The domain 2607:f8b0:4023:401::1a does not exist",
        "The reverse DNS of 2607:f8b0:4023:401::1a is 2607:f8b0:4023:401::1a, but the A/AAAA DNS records for 2607:f8b0:4023:401::1a do not resolve to 2607:f8b0:4023:401::1a",
        "The domain 2607:f8b0:4023:401::1a does not exist",
        "The reverse DNS of 2607:f8b0:4023:401::1a is 2607:f8b0:4023:401::1a, but the A/AAAA DNS records for 2607:f8b0:4023:401::1a do not resolve to 2607:f8b0:4023:401::1a"
      ]
    },
    "ns": {
      "hostnames": [
        "ns-1653.awsdns-14.co.uk",
        "ns-439.awsdns-54.com",
        "ns-739.awsdns-28.net",
        "ns-1390.awsdns-45.org"
      ],
      "warnings": []
    },
    "spf": {
      "dns_lookups": 2,
      "parsed": {
        "all": "softfail",
        "fail": [],
        "include": [
          {
            "dns_lookups": 0,
            "domain": "rapid7.com._nspf.vali.email",
            "parsed": {
              "all": "fail",
              "fail": [],
              "include": [],
              "neutral": [],
              "pass": [],
              "softfail": []
            },
            "record": "v=spf1 -all",
            "warnings": []
          },
          {
            "dns_lookups": 0,
            "domain": "%!{(MISSING)i}._ip.%!{(MISSING)h}._ehlo.%!{(MISSING)d}._spf.vali.email",
            "parsed": {
              "all": "fail",
              "fail": [],
              "include": [],
              "neutral": [],
              "pass": [],
              "softfail": []
            },
            "record": "v=spf1 -all",
            "warnings": []
          }
        ],
        "neutral": [],
        "pass": [],
        "softfail": []
      },
      "record": "v=spf1 include:rapid7.com._nspf.vali.email include:%!{(MISSING)i}._ip.%!{(MISSING)h}._ehlo.%!{(MISSING)d}._spf.vali.email ~all",
      "valid": true,
      "warnings": []
    }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.1.3 - Add example inputs
* 2.1.2 - Changed description in action `check_domains_alternate_nameservers` | Fix typo in word `nameservers` to `name_servers` | Changed email addresses to `user@example.com`
* 2.1.1 - New spec and help.md format for the Extension Library
* 2.1.0 - Added action Check Domains Alternate Nameservers
* 2.0.0 - Added timeout to Check Domain
* 1.0.0 - Initial plugin

# Links

## References

* [Checkdmarc](https://domainaware.github.io/checkdmarc/)
