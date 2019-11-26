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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain to check. e.g. fbi.gov, google.com|None|
|timeout|float|6.0|True|Timeout in seconds for request. Default is 6 seconds|None|

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
         "record":"v=DMARC1;p=none;fo=1;pct=100;rua=mailto:aggrep@mail.pci.gov,mailto:dmarc_reporting@mail.pci.gov;ruf=mailto:authfail@mail.pci.gov",
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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain to check. e.g. fbi.gov, google.com|None|
|nameservers|[]string|['1.1.1.1', '1.0.0.1']|True|Nameserver to check against. e.g ["1.1.1.1","1.0.0.1"]|None|
|timeout|float|6.0|True|Timeout in seconds for request. Default is 6 seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|report|False|Report|

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
         "record":"v=DMARC1;p=none;fo=1;pct=100;rua=mailto:aggrep@mail.pci.gov,mailto:dmarc_reporting@mail.pci.gov;ruf=mailto:authfail@mail.pci.gov",
         "valid":false,
         "location":"whitehouse.gov",
         "error":"mail.pci.gov does not indicate that it accepts DMARC reports about whitehouse.gov - Authorization record not found: whitehouse.gov._report._dmarc.mail.pci.gov IN TXT \"v=DMARC1\""
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

* 2.1.2 - New spec and help.md format for the Hub
* 2.1.1 - New spec and help.md format for the Hub
* 2.1.0 - Added action Check Domains Alternate Nameservers
* 2.0.0 - Added timeout to Check Domain
* 1.0.0 - Initial plugin

# Links

## References

* [Checkdmarc](https://domainaware.github.io/checkdmarc/)

