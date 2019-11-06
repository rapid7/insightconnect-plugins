# Description

[Barracuda Web Application Firewall](https://campus.barracuda.com/product/webapplicationfirewall/) is the a solution for organizations looking to protect web applications from data breaches and defacement. With the Barracuda Web Application Firewall, administrators do not need to wait for clean code or even know how an application works to secure their applications.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|False|Enter address to Barracuda waf|None|
|credentials|credential_username_password|None|True|Username and password|None|

## Technical Details

### Actions

#### All Vsites

Lists all Vsites.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|false|Vsite ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|vsites|[]vsite|true|All info about vsite|

Example output:

```

{
  "vsites": [
    {
      "service_group": [
        "default"
      ],
      "service_groups": [
        {
          "virtual_services": [
            {
              "status": "enable",
              "name": "test-v6-virtual-service",
              "enable_access_logs": "yes",
              "servers": [
                []
              ],
              "mask": "255.255.255.255",
              "ip_address": "192.168.14.1",
              "group": "default",
              "advanced_configuration": {
                "ntlm_ignore_extra_data": null,
                "keepalive_requests": "64",
                "enable_web_application_firewall": "yes"
              },
              "website_profiles": {
                "mode": "passive",
                "allowed_domains": [],
                "use_profile": "yes",
                "exclude_url_patterns": [
                  "*.jpg",
                  "*.png",
                  "*.gif",
                  "*.tiff",
                  "/images/*",
                  "*.ico",
                  "*.img",
                  "*.swf",
                  "*.jpeg",
                  "*.js",
                  "*.css"
                ],
                "strict_profile_check": "no",
                "include_url_patterns": []
              },
              "type": "HTTP",
              "address_version": "ipv4",
              "load_balance": {
                "persistence_cookie_path": null,
                "algorithm": "round_robin",
                "failover_method": "load_balance",
                "persistence_idle_timeout": "600",
                "cookie_age": null,
                "persistence_method": "none",
                "source_ip_netmask": null,
                "parameter_name": null,
                "header_name": null,
                "persistence_cookie_domain": null,
                "persistence_cookie_name": "persistence"
              },
              "port": "8080",
              "session_timeout": "60",
              "ssl_offloading": {
                "sni_ecdsa_certificate": "",
                "status": "off",
                "selected_ciphers": "ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-RSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-SHA256,ECDHE-RSA-AES128-SHA256,AES256-GCM-SHA384,AES128-GCM-SHA256,AES256-SHA256,AES128-SHA256,ECDHE-ECDSA-AES256-SHA,ECDHE-RSA-AES256-SHA,ECDHE-ECDSA-DES-CBC3-SHA,ECDHE-RSA-DES-CBC3-SHA,ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,AES256-SHA,DHE-RSA-AES256-GCM-SHA384,DHE-RSA-AES256-SHA256,DHE-RSA-AES256-SHA,DHE-RSA-CAMELLIA256-SHA,DHE-RSA-AES128-GCM-SHA256,DHE-RSA-AES128-SHA256,DHE-RSA-AES128-SHA,DHE-RSA-CAMELLIA128-SHA,EDH-RSA-DES-CBC3-SHA,CAMELLIA256-SHA,DES-CBC3-SHA,AES128-SHA,CAMELLIA128-SHA",
                "enable_pfs": "no",
                "override_ciphers_ssl3": null,
                "domain": "",
                "trusted_certificates": [],
                "enable_ssl_3": "no",
                "sni_certificate": "",
                "client_authentication_rules": [],
                "override_ciphers_tls_1": null,
                "client_authentication_rule_count": "0",
                "enable_sni": "no",
                "ciphers": "default",
                "enable_tls_1": "yes",
                "enable_tls_1_2": "enable",
                "enable_strict_sni_check": null,
                "enable_tls_1_1": "enable",
                "enforce_client_certificate": "yes",
                "override_ciphers_tls_1_1": null,
                "enable_client_authentication": "disable"
              },
              "id": "test-v6-virtual-service",
              "comments": null,
              "security": {
                "trusted_hosts_group": "",
                "mode": "passive",
                "rate_control_pool": "NONE",
                "web_firewall_policy": "default",
                "ignore_case": "yes",
                "client_ip_addr_header": null,
                "trusted_hosts_action": "default",
                "rate_control_status": "off",
                "ftp_attack_prevention_status": null,
                "web_firewall_log_level": "5-notice"
              },
              "content_rules": [
                {
                  "status": "on",
                  "mode": "passive",
                  "servers": [
                    []
                  ],
                  "host_match": "test-v8.example.com",
                  "extended_match_sequence": "1",
                  "url_match": "/",
                  "load_balance": {
                    "lb_algorithm": "round_robin",
                    "failover_method": "load_balance",
                    "persistence_method": "none"
                  },
                  "extended_match": "*",
                  "name": "test-v6-content-rule",
                  "id": "test-v6-content-rule",
                  "service_name": "test-v6-virtual-service",
                  "comments": null,
                  "web_firewall_policy": "owa"
                }
              ],
              "service_hostname": [
                "test"
              ],
              "instant_ssl": {
                "secure_site_domain": [
                  "test"
                ],
                "status": "off",
                "sharepoint_rewrite_support": "off"
              }
            },
            {
              "status": "enable",
              "name": "test-v11-virtual-service",
              "enable_access_logs": "yes",
              "servers": [
                []
              ],
              "mask": "255.255.255.255",
              "ip_address": "192.168.16.1",
              "group": "default",
              "advanced_configuration": {
                "ntlm_ignore_extra_data": null,
                "keepalive_requests": "64",
                "enable_web_application_firewall": "yes"
              },
              "website_profiles": {
                "mode": "passive",
                "allowed_domains": [],
                "use_profile": "yes",
                "exclude_url_patterns": [
                  "*.jpg",
                  "*.png",
                  "*.gif",
                  "*.tiff",
                  "/images/*",
                  "*.ico",
                  "*.img",
                  "*.swf",
                  "*.jpeg",
                  "*.js",
                  "*.css"
                ],
                "strict_profile_check": "no",
                "include_url_patterns": []
              },
              "type": "HTTP",
              "address_version": "ipv4",
              "load_balance": {
                "persistence_cookie_path": null,
                "algorithm": "round_robin",
                "failover_method": "load_balance",
                "persistence_idle_timeout": "600",
                "cookie_age": null,
                "persistence_method": "none",
                "source_ip_netmask": null,
                "parameter_name": null,
                "header_name": null,
                "persistence_cookie_domain": null,
                "persistence_cookie_name": "persistence"
              },
              "port": "8080",
              "session_timeout": "60",
              "ssl_offloading": {
                "sni_ecdsa_certificate": "",
                "status": "off",
                "selected_ciphers": "ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-RSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-SHA256,ECDHE-RSA-AES128-SHA256,AES256-GCM-SHA384,AES128-GCM-SHA256,AES256-SHA256,AES128-SHA256,ECDHE-ECDSA-AES256-SHA,ECDHE-RSA-AES256-SHA,ECDHE-ECDSA-DES-CBC3-SHA,ECDHE-RSA-DES-CBC3-SHA,ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,AES256-SHA,DHE-RSA-AES256-GCM-SHA384,DHE-RSA-AES256-SHA256,DHE-RSA-AES256-SHA,DHE-RSA-CAMELLIA256-SHA,DHE-RSA-AES128-GCM-SHA256,DHE-RSA-AES128-SHA256,DHE-RSA-AES128-SHA,DHE-RSA-CAMELLIA128-SHA,EDH-RSA-DES-CBC3-SHA,CAMELLIA256-SHA,DES-CBC3-SHA,AES128-SHA,CAMELLIA128-SHA",
                "enable_pfs": "no",
                "override_ciphers_ssl3": null,
                "domain": "",
                "trusted_certificates": [],
                "enable_ssl_3": "no",
                "sni_certificate": "",
                "client_authentication_rules": [],
                "override_ciphers_tls_1": null,
                "client_authentication_rule_count": "0",
                "enable_sni": "no",
                "ciphers": "default",
                "enable_tls_1": "yes",
                "enable_tls_1_2": "enable",
                "enable_strict_sni_check": null,
                "enable_tls_1_1": "enable",
                "enforce_client_certificate": "yes",
                "override_ciphers_tls_1_1": null,
                "enable_client_authentication": "disable"
              },
              "id": "test-v11-virtual-service",
              "comments": null,
              "security": {
                "trusted_hosts_group": "",
                "mode": "passive",
                "rate_control_pool": "NONE",
                "web_firewall_policy": "default",
                "ignore_case": "yes",
                "client_ip_addr_header": null,
                "trusted_hosts_action": "default",
                "rate_control_status": "off",
                "ftp_attack_prevention_status": null,
                "web_firewall_log_level": "5-notice"
              },
              "content_rules": [
                {
                  "status": "on",
                  "mode": "passive",
                  "servers": [
                    []
                  ],
                  "host_match": "test-v11-test.example.com",
                  "extended_match_sequence": "1",
                  "url_match": "/",
                  "load_balance": {
                    "lb_algorithm": "round_robin",
                    "failover_method": "load_balance",
                    "persistence_method": "none"
                  },
                  "extended_match": "*",
                  "name": "test-v11-content-rule",
                  "id": "test-v11-content-rule",
                  "service_name": "test-v11-virtual-service",
                  "comments": null,
                  "web_firewall_policy": "owa"
                }
              ],
              "service_hostname": [
                "test"
              ],
              "instant_ssl": {
                "secure_site_domain": [
                  "test"
                ],
                "status": "off",
                "sharepoint_rewrite_support": "off"
              }
            },
            {
              "status": "enable",
              "name": "test-v14-virtual-service",
              "enable_access_logs": "yes",
              "servers": [
                []
              ],
              "mask": "255.255.255.255",
              "ip_address": "192.168.19.1",
              "group": "default",
              "advanced_configuration": {
                "ntlm_ignore_extra_data": null,
                "keepalive_requests": "64",
                "enable_web_application_firewall": "yes"
              },
              "website_profiles": {
                "mode": "passive",
                "allowed_domains": [],
                "use_profile": "yes",
                "exclude_url_patterns": [
                  "*.jpg",
                  "*.png",
                  "*.gif",
                  "*.tiff",
                  "/images/*",
                  "*.ico",
                  "*.img",
                  "*.swf",
                  "*.jpeg",
                  "*.js",
                  "*.css"
                ],
                "strict_profile_check": "no",
                "include_url_patterns": []
              },
              "type": "HTTP",
              "address_version": "ipv4",
              "load_balance": {
                "persistence_cookie_path": null,
                "algorithm": "round_robin",
                "failover_method": "load_balance",
                "persistence_idle_timeout": "600",
                "cookie_age": null,
                "persistence_method": "none",
                "source_ip_netmask": null,
                "parameter_name": null,
                "header_name": null,
                "persistence_cookie_domain": null,
                "persistence_cookie_name": "persistence"
              },
              "port": "8080",
              "session_timeout": "60",
              "ssl_offloading": {
                "sni_ecdsa_certificate": "",
                "status": "off",
                "selected_ciphers": "ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-RSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-SHA256,ECDHE-RSA-AES128-SHA256,AES256-GCM-SHA384,AES128-GCM-SHA256,AES256-SHA256,AES128-SHA256,ECDHE-ECDSA-AES256-SHA,ECDHE-RSA-AES256-SHA,ECDHE-ECDSA-DES-CBC3-SHA,ECDHE-RSA-DES-CBC3-SHA,ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,AES256-SHA,DHE-RSA-AES256-GCM-SHA384,DHE-RSA-AES256-SHA256,DHE-RSA-AES256-SHA,DHE-RSA-CAMELLIA256-SHA,DHE-RSA-AES128-GCM-SHA256,DHE-RSA-AES128-SHA256,DHE-RSA-AES128-SHA,DHE-RSA-CAMELLIA128-SHA,EDH-RSA-DES-CBC3-SHA,CAMELLIA256-SHA,DES-CBC3-SHA,AES128-SHA,CAMELLIA128-SHA",
                "enable_pfs": "no",
                "override_ciphers_ssl3": null,
                "domain": "",
                "trusted_certificates": [],
                "enable_ssl_3": "no",
                "sni_certificate": "",
                "client_authentication_rules": [],
                "override_ciphers_tls_1": null,
                "client_authentication_rule_count": "0",
                "enable_sni": "no",
                "ciphers": "default",
                "enable_tls_1": "yes",
                "enable_tls_1_2": "enable",
                "enable_strict_sni_check": null,
                "enable_tls_1_1": "enable",
                "enforce_client_certificate": "yes",
                "override_ciphers_tls_1_1": null,
                "enable_client_authentication": "disable"
              },
              "id": "test-v14-virtual-service",
              "comments": null,
              "security": {
                "trusted_hosts_group": "",
                "mode": "passive",
                "rate_control_pool": "NONE",
                "web_firewall_policy": "default",
                "ignore_case": "yes",
                "client_ip_addr_header": null,
                "trusted_hosts_action": "default",
                "rate_control_status": "off",
                "ftp_attack_prevention_status": null,
                "web_firewall_log_level": "5-notice"
              },
              "content_rules": [
                {
                  "status": "on",
                  "mode": "passive",
                  "servers": [
                    []
                  ],
                  "host_match": "test-v14-test.example.com",
                  "extended_match_sequence": "1",
                  "url_match": "/",
                  "load_balance": {
                    "lb_algorithm": "round_robin",
                    "failover_method": "load_balance",
                    "persistence_method": "none"
                  },
                  "extended_match": "*",
                  "name": "test-v14-content-rule",
                  "id": "test-v14-content-rule",
                  "service_name": "test-v14-virtual-service",
                  "comments": null,
                  "web_firewall_policy": "owa"
                }
              ],
              "service_hostname": [
                "test"
              ],
              "instant_ssl": {
                "secure_site_domain": [
                  "test"
                ],
                "status": "off",
                "sharepoint_rewrite_support": "off"
              }
            }
          ],
          "name": "default",
          "id": "default"
        }
      ],
      "name": "default",
      "id": "default",
      "active_on": 990015,
      "comments": []
    }
  ]
}

```

#### Delete Vsite

Deletes the given Vsite.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|true|vsite ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|true|Is delete was success|

Example output:

```

{
  "status": false
}

```

#### Create Virtual Service

Creates a virtual service with the given values.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|true|The name of the new service|None|
|address|string|None|true|The virtual IP address that will be used for accessing this application|None|
|port|integer|None|true|The port number on which your web server responds|None|
|type|string|None|true|The type of the service you want to create|[http,https,ftp,ftpssl,custom,customssl,instantssl,redirect]|
|address_version|string|None|true|The internet protocol version of the service|[ipv4,ipv6]|
|vsite|string|None|false|The name of the vsite under which the service needs to be created|None|
|group|string|None|false|The name of the service group under which the service needs to be created|None|
|certificate|string|None|false|The certificate that needs to be presented to the browser when accessing this Service|None|
|service_hostname|string|None|false|The domain name to identify and rewrite HTTP requests to HTTPS|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|The name of the service that got created|

Example output:

```

{
  "id": "test-v14-virtual-service"
}

```

#### Retrieve Virtual Service

Lists virtual service with service ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|false|Virtual service ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|ID|
|load_balance|array|true|Load balance|
|comments|array|true|Comments|
|group|string|true|Group|
|address|string|true|Ipv4 or Ipv6 address|
|ssl_off_loading|array|true|SSL offloading|
|enable|boolean|true|Is enabled|
|name|string|true|Name of virtual service|
|enable_accessLog|boolean|true|Name of virtual service|
|port|integer|None|true|The port number on which your web server responds|
|address_version|string|None|true|The internet protocol version of the service|
|security|array|true|Information about security|
|servers|array|true|List of servers|
|content_rules|array|true|List of content rules|

Example output:

```

[
  {
    "type": "HTTP",
    "comments": null,
    "ip_address": "192.168.19.1",
    "content_rules": [
      {
        "comments": null,
        "status": "on",
        "extended_match": "*",
        "extended_match_sequence": "1",
        "host_match": "test-v14-test.example.com",
        "id": "test-v14-content-rule",
        "load_balance": {
          "failover_method": "load_balance",
          "lb_algorithm": "round_robin",
          "persistence_method": "none"
        },
        "service_name": "test-v14-virtual-service",
        "mode": "passive",
        "servers": [
          []
        ],
        "web_firewall_policy": "owa",
        "name": "test-v14-content-rule",
        "url_match": "/"
      }
    ],
    "token": "eyJldCI6IjE1MTEyOTU1MDMiLCJwYXNzd29yZCI6ImJlMGNlZGU1ZTdjYzlhNDc3Y2JjNDMyZjFh\nYmI2ZWE1IiwidXNlciI6ImFkbWluIn0=\n",
    "status": "enable",
    "enable_access_logs": "yes",
    "mask": "255.255.255.255",
    "advanced_configuration": {
      "ntlm_ignore_extra_data": null,
      "enable_web_application_firewall": "yes",
      "keepalive_requests": "64"
    },
    "security": {
      "web_firewall_log_level": "5-notice",
      "ftp_attack_prevention_status": null,
      "client_ip_addr_header": null,
      "web_firewall_policy": "default",
      "mode": "passive",
      "trusted_hosts_group": "",
      "trusted_hosts_action": "default",
      "ignore_case": "yes",
      "rate_control_pool": "NONE",
      "rate_control_status": "off"
    },
    "address_version": "ipv4",
    "instant_ssl": {
      "secure_site_domain": [
        "test"
      ],
      "sharepoint_rewrite_support": "off",
      "status": "off"
    },
    "session_timeout": "60",
    "port": "8080",
    "website_profiles": {
      "include_url_patterns": [],
      "strict_profile_check": "no",
      "mode": "passive",
      "exclude_url_patterns": [
        "*.jpg",
        "*.png",
        "*.gif",
        "*.tiff",
        "/images/*",
        "*.ico",
        "*.img",
        "*.swf",
        "*.jpeg",
        "*.js",
        "*.css"
      ],
      "use_profile": "yes",
      "allowed_domains": []
    },
    "ssl_offloading": {
      "enforce_client_certificate": "yes",
      "selected_ciphers": "ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-RSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-SHA256,ECDHE-RSA-AES128-SHA256,AES256-GCM-SHA384,AES128-GCM-SHA256,AES256-SHA256,AES128-SHA256,ECDHE-ECDSA-AES256-SHA,ECDHE-RSA-AES256-SHA,ECDHE-ECDSA-DES-CBC3-SHA,ECDHE-RSA-DES-CBC3-SHA,ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,AES256-SHA,DHE-RSA-AES256-GCM-SHA384,DHE-RSA-AES256-SHA256,DHE-RSA-AES256-SHA,DHE-RSA-CAMELLIA256-SHA,DHE-RSA-AES128-GCM-SHA256,DHE-RSA-AES128-SHA256,DHE-RSA-AES128-SHA,DHE-RSA-CAMELLIA128-SHA,EDH-RSA-DES-CBC3-SHA,CAMELLIA256-SHA,DES-CBC3-SHA,AES128-SHA,CAMELLIA128-SHA",
      "enable_tls_1_1": "enable",
      "enable_strict_sni_check": null,
      "sni_ecdsa_certificate": "",
      "enable_sni": "no",
      "enable_tls_1_2": "enable",
      "trusted_certificates": [],
      "override_ciphers_tls_1_1": null,
      "ciphers": "default",
      "client_authentication_rule_count": "0",
      "domain": "",
      "sni_certificate": "",
      "status": "off",
      "enable_client_authentication": "disable",
      "enable_tls_1": "yes",
      "override_ciphers_ssl3": null,
      "client_authentication_rules": [],
      "enable_pfs": "no",
      "override_ciphers_tls_1": null,
      "enable_ssl_3": "no"
    },
    "id": "test-v14-virtual-service",
    "load_balance": {
      "parameter_name": null,
      "header_name": null,
      "persistence_cookie_path": null,
      "persistence_cookie_name": "persistence",
      "persistence_method": "none",
      "source_ip_netmask": null,
      "failover_method": "load_balance",
      "algorithm": "round_robin",
      "persistence_cookie_domain": null,
      "persistence_idle_timeout": "600",
      "cookie_age": null
    },
    "service_hostname": [
      "test"
    ],
    "servers": [
      []
    ],
    "name": "test-v14-virtual-service",
    "group": "default"
  }
]

```

#### Delete Virtual Service

Delete virtual service with service ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|true|Virtual Service ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|true|Is delete was success|

Example output:

```

{
  "msg": "Successfully deleted"
}

```

#### Create Security Policy

Creates a security policy with the default values.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|true|The name of the security policy that needs to be created|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|ID of the new policy|

Example output:

```

{
  "id": "test-v14-policy"
}

```

#### Retrieve Security Policies

Lists all security policies.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|ID|
|character|string|true|Default character set|
|cloaking|cloaking|true||
|apply_double_decoding|string|true|Apply double decoding|
|data_theft_protection|array|true|Data theft protection|
|url_protection_status|integer|true|URL protection status|
|allowed_acls|integer|true|Allowed ACLs|
|request_limit|request_limits|true|Request limits|
|parameter_protection|parameter_protection|true|Parameter protection|
|url_protection|url_protection|true|URL protection configuration|
|cookie_security|cookie_security|true|Cookie security|
|url_normalization|url_normalization|true|URL normalization|
|cookie_protection|string|true|Cookie protection|
|limit_checks|boolean|true|Limit checks|
|name|string|true|Name of security policies|
|parameter_protection_status|string|true|parameter protection status|
|disallowed_acls|integer|true|Disallowed ACLs|

Example output:

```

{
  "policies": [
    {
      "double_decoding": "yes",
      "request_limits": {
        "max_query_length": "2",
        "max_cookie_value_length": "2",
        "enable": "yes",
        "max_cookie_name_length": "2",
        "max_number_of_headers": "2",
        "max_request_line_length": "2",
        "max_request_length": "2",
        "max_header_value_length": "512",
        "max_url_length": "2",
        "max_header_name_length": "2",
        "max_number_of_cookies": "2"
      },
      "url_protection_status": "yes",
      "parameter_protection_status": "yes",
      "allowed_acls": 1,
      "parameter_protection": {
        "file_upload_extensions": [
          "JPG",
          "GIF",
          "PDF"
        ],
        "enable": "yes",
        "file_upload_mime_types": [
          "image/jpeg",
          "image/gif",
          "application/pdf"
        ],
        "allowed_file_upload_type": "extensions",
        "denied_metacharacters": "",
        "blocked_attack_types": [],
        "ignore_parameters": [],
        "custom_blocked_attack_types": [],
        "base64_decode_parameter_value": "no",
        "exception_patterns": [],
        "maximum_parameter_value_length": "2",
        "maximum_instances": "0",
        "maximum_upload_file_size": "0"
      },
      "default_character_set": "GBK",
      "cookie_security": {
        "allow_unrecognized_cookies": "custom",
        "tamper_proof_mode": "signed",
        "cookie_max_age": "0",
        "cookie_replay_protection_type": "none",
        "http_only": "yes",
        "days_allowed": "7",
        "custom_headers": [],
        "secure_cookie": "yes",
        "cookies_exempted": [
          "__utma",
          "__utmc",
          "__utmz",
          "__utmb",
          "AuthSuccessURL",
          "CTSESSION",
          "SMSESSION",
          "SMCHALLENGE"
        ]
      },
      "id": "test-v14-policy",
      "name": "test-v14-policy",
      "data_theft_protection": [
        "credit-cards",
        "ssn",
        "directory-indexing",
        "test-v14-data-theft"
      ],
      "token": "eyJldCI6IjE1MTEyOTU0OTciLCJwYXNzd29yZCI6IjU1MTY1OTg2OTQ3MDhlYTE3YjMxNTRkOTZm\nMTExNzY0IiwidXNlciI6ImFkbWluIn0=\n",
      "limit_checks": true,
      "url_normalization": {
        "apply_double_decoding": "yes",
        "parameter_separators": "ampersand",
        "detect_response_charset": "yes",
        "default_charset": "GBK"
      },
      "disallowed_acls": 8,
      "cookie_protection": "signed",
      "cloaking": {
        "filter_response_header": "yes",
        "return_codes_to_exempt": [],
        "suppress_return_code": "yes",
        "headers_to_filter": [
          "Server",
          "X-Powered-By",
          "X-AspNet-Version"
        ]
      },
      "url_protection": {
        "allowed_content_types": [
          "application/x-www-form-urlencoded",
          "multipart/form-data",
          "text/xml",
          "application/json"
        ],
        "maximum_parameter_name_length": "2",
        "enable": "yes",
        "max_content_length": "0",
        "max_parameters": "0",
        "exception_patterns": [],
        "maximum_upload_files": "0",
        "custom_blocked_attack_types": [],
        "allowed_methods": [
          "GET",
          "POST",
          "HEAD"
        ],
        "blocked_attack_types": [],
        "csrf_prevention": "none"
      }
    }
  ]
}

```

#### Update Security Policy

Updates a security policy with the given values.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|request_limits|request_limits|None|false|Configuration of requests|None|
|cookie_security|cookie_security|None|false|Configuration of cookies security|None|
|url_protection|url_protection|None|false|Configuration of url protection|None|
|parameter_protection|parameter_protection|None|false|Configuration of requests|None|
|cloaking|cloaking|None|false|Configuration of cloaking|None|
|url_normalization|url_normalization|None|false|Configuration of requests|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|true|Message of update|

Example output:

```

{
  "msg": "Configuration Updated"
}

```

#### Delete Security Policy

Deletes the given security policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|true|ID of security policy|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|true|Message of update|

Example output:

```

{
  "msg": "Successfully deleted"
}

```

#### Create Data Theft Element

Adds a data theft element with the given values.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|name|string|None|true|A name for this data theft element|None|
|enabled|string|None|true|Use this data theft element to be matched in the server response pages|None|
|identity_theft_type|string|None|true|The identity theft pattern to which the element mentioned in "name" belongs to. The enumerated values include|None|
|custom_identity_theft_type|string|None|true|The identity theft pattern defined on the ADVANCED > Libraries page (if any)|None|
|action|string|None|true|The action to be enforced on any page sent by the server containing this data type|['cloack', 'block']|
|initial_characters_to_keep|string|None|true|The number of initial characters to be displayed to the user|None|
|trailing_characters_to_keep|string|None|true|The number of trailing characters to be displayed to the user|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|Data theft element ID|

Example output:

```

{
  "id": "test-v14-data-theft"
}

```

#### Retrieve Data Theft Element

Lists data theft element by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|id|string|None|true|ID of security policy|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|enabled|string|None|true|Use this data theft element to be matched in the server response pages|
|identity_theft_type|string|None|true|The identity theft pattern to which the element mentioned in "name" belongs to|
|custom_identity_theft_type|string|None|true|The identity theft pattern defined on the ADVANCED > Libraries page (if any)|
|action|string|None|true|The action to be enforced on any page sent by the server containing this data type|
|initial_characters_to_keep|string|None|true|The number of initial characters to be displayed to the user|
|trailing_characters_to_keep|string|None|true|The number of trailing characters to be displayed to the user|

Example output:

```

[
  {
    "name": "test-v14-data-theft",
    "enabled": "yes",
    "initial_characters_to_keep": "0",
    "trailing_characters_to_keep": "0",
    "token": "eyJldCI6IjE1MTEyOTU0ODUiLCJwYXNzd29yZCI6IjViNTIxMWY5YjI5YzRkOTYyMTNiMGZjMWI5\nMWE2MGU0IiwidXNlciI6ImFkbWluIn0=\n",
    "action": "cloak",
    "identity_theft_type": "custom",
    "id": "test-v14-data-theft",
    "custom_identity_theft_type": "test"
  }
]

```

#### Update Data Theft Element

Updates the values of given parameters in the given data theft element.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|id|string|None|false|ID of a Data Theft Element|None|
|enabled|string|None|false|Use this data theft element to be matched in the server response pages|None|
|identity_theft_type|string|None|false|The identity theft pattern to which the element mentioned in "name" belongs to|None|
|custom_identity_theft_type|string|None|false|The identity theft pattern defined on the ADVANCED > Libraries page (if any)|None|
|action|string|None|false|The action to be enforced on any page sent by the server containing this data type|None|
|initial_characters_to_keep|string|None|false|The number of initial characters to be displayed to the user|None|
|trailing_characters_to_keep|string|None|false|The number of trailing characters to be displayed to the user|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|None|true|ID of a Data Theft Element|

Example output:

```

{
  "id": "test-v14-data-theft"
}

```

#### Delete Data Theft Element

Deletes the given data theft element.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|id|string|None|false|ID of a Data Theft Element|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|true|Message of delete|

Example output:

```

{
  "msg": "Successfully deleted"
}

```

#### Retrieve Attack Groups

Lists all attack groups.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|action_policy|[]action_policy|true|Attack groups information|

Example output:

```

{
  "action_policy": [
    {
      "followUpActionTime": 0,
      "denyResponse": "",
      "redirectUrl": "",
      "action": "",
      "responsePage": "",
      "followUpAction": ""
    }
  ]
}

```

#### Retrieve Attack Groups by ID

Lists all attack groups with attack group ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|attack_group_id|string|None|true|Attack group ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|action_policy|[]action_policy|true|Attack groups information|

Example output:

```

{
  "action_policy": [
    {
      "responsePage": "",
      "action": "",
      "redirectUrl": "",
      "followUpAction": "",
      "followUpActionTime": 0,
      "denyResponse": ""
    }
  ]
}

```

#### Retrieve Attack Actions

Lists all attack actions.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|attack_group_id|string|None|true|Attack group ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|action_policy|[]action_policy|true|Attack groups information|

Example output:

```

{
  "action_policy": [
     {
       "follow_up_action": "none",
       "redirect_url": "",
       "numeric_id": "directory_traversal_beyond_root",
       "deny_response": "send_response",
       "response_page": "default",
       "id": "directory-traversal-beyond-root",
       "name": "directory-traversal-beyond-root",
       "action": "protect_and_log",
       "follow_up_action_time": 60,
       "attack_group": "protocol-violations"
     },
     {
       "follow_up_action": "none",
       "redirect_url": "",
       "numeric_id": "malformed_content_length",
       "deny_response": "send_response",
       "response_page": "default",
       "id": "malformed-content-length",
       "name": "malformed-content-length",
       "action": "protect_and_log",
       "follow_up_action_time": 60,
       "attack_group": "protocol-violations"
     },
     ...
   ]
}

```

#### Retrieve Attack Actions by ID

Lists all attack actions for the given attack group with actionID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|attack_group_id|string|None|true|Attack group ID|None|
|action_id|string|None|true|Attack group ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|action_policy|action_policy|true|Attack groups information|

Example output:

```

{
  "action_policy": [
   {
     "follow_up_action_time": "60",
     "name": "directory-traversal-beyond-root",
     "deny_response": "send_response",
     "id": "directory-traversal-beyond-root",
     "redirect_url": "",
     "attack_group": "protocol-violations",
     "action": "protect_and_log",
     "numeric_id": "directory_traversal_beyond_root",
     "follow_up_action": "none",
     "response_page": "default"
   },
   {
     "follow_up_action_time": "60",
     "name": "post-request-without-content-length",
     "deny_response": "send_response",
     "id": "post-request-without-content-length",
     "redirect_url": "",
     "attack_group": "protocol-violations",
     "action": "protect_and_log",
     "numeric_id": "post_without_content_length",
     "follow_up_action": "none",
     "response_page": "default"
   },
   ...
  ]
}

```

#### Update an Action Policy

Updates the values of given parameters in the given action policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|attack_group_id|string|None|true|Attack group ID|None|
|action_id|string|None|true|Attack group ID|None|
|action_policy|action_policy|true|Attack groups information|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|true|Message of update|

Example output:

```

{
  "msg": "Configuration Updated"
}

```

#### Create Global ACL Rule

Adds a global ACL rule with the given values.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|global_acl|globalACL|None|true|Global ACL object|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|true|Message of update|

Example output:

```

{
  "id": "test-v14-global-acl-rule"
}

```

#### Retrieve Global ACL Rules

Lists all global ACL rules with global ACL ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|global_acl_id|integer|None|true|Global ACL ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|extended_match_sequence|number|true|A number to indicate the order in which the extended match rule must be evaluated in the requests|
|name|string|true|Global ACL name|
|comments|array|true|Description about the global ACL rule|
|extended_match|string|true|An expression that consists of a combination of HTTP headers and/or query string parameters|
|url_match|string|true|The URL to be matched to the URL in the request. The URL should start with a "/" and can have at most one " * " anywhere in the URL|
|action|string|true|The action to be taken on the request matching this URL|
|redirect_url|string|true|A URL to which a user should be redirected if action is temporary_redirect or permanent_redirect|
|id|string|true|ID of global ACL|

Example output:

```

[
  {
    "redirect_url": "",
    "response_page": "default",
    "extended_match_sequence": "0",
    "token": "eyJldCI6IjE1MTEyOTU0OTEiLCJwYXNzd29yZCI6ImI4ODAxNGQ3YTg2M2NmYzJlYThhOTM5ZjAy\nNzUzOTY2IiwidXNlciI6ImFkbWluIn0=\n",
    "comments": "",
    "enable_url_acl": "yes",
    "name": "test-v14-global-acl-rule",
    "id": "test-v14-global-acl-rule",
    "deny_response": "reset",
    "extended_match": "*",
    "action": "process",
    "url_match": "/"
  }
]

```

#### Update Global ACL Rule

Updates the values of given parameters in the given global ACL rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|global_acl_id|integer|None|true|Global ACL ID|None|
|enable_url_acl|boolean|false|Enforce this URL ACL rule for all the Services configured on the Barracuda Web Application Firewall or not|None|
|url_match|string|false|The URL to be matched to the URL in the request.  The URL should start with a "/" and can have at most one " * " anywhere in the URL. A value of "/*" means that the access control rule (ACL) applies for all URLs in that domain|None|
|extended_match|string|false|An expression that consists of a combination of HTTP headers and/or query string parameters. Updating extended match parameters value is shown in the example below|None|
|extended_match_sequence|integer|false|A number to indicate the order in which the extended match rule must be evaluated in the requests|None|
|action|string|false|The action to be taken on the request matching this URL|['process','allow','deny_and_log','deny_with_no_log','temporary_redirect','permanent_redirect']|
|deny_response|string|false|The response to be sent to the client if the request is denied|['reset','response_page','temporary_redirect','permanent_redirect']|
|response_page|string|false|The response page to be sent to the client|['default','default-virus','default-error-resp','default-captcha-tries-error-page','default-captcha-sessions-error-page','default-suspected-activity-error-page','default-captcha-response-page']|
|redirect_url|string|false|A URL to which a user should be redirected if action is temporary_redirect or permanent_redirect|
|comments|string|false|Description about the global ACL rule|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|ID of global ACL|

Example output:

```

{
  "id": "test-v14-global-acl-rule"
}

```

#### Delete Global ACL Rule

Deletes the given global ACL rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_id|string|None|true|ID of security policy|None|
|global_acl_id|integer|None|true|Global ACL ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|true|Message of deleted|

Example output:

```

{
  "msg": "Successfully deleted"
}

```

#### Create Host Group

Creates a trusted host group with the given name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|true|A name for the trusted host group that needs to be created|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|Name of trusted host group|

Example output:

```

{
  "id": "test-v14-group"
}

```

#### Delete Host Group

Deletes the given service group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|true|A name of trusted host group|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|true|Message of deleted|

Example output:

```

{
  "msg": "Successfully deleted"
}

```

#### Create Host in Group

Creates a trusted host with the given name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group_name|string|None|true|Name for the trusted host group|None|
|name|string|None|true|Name for the trusted host|None|
|address_version|string|None|true|Internet protocol version for the trusted host|None|
|address|string|None|true|IP address of the trusted host|None|
|mask|string|None|true|Associated subnet mask|None|
|comments|string|None|false|Description about the trusted host|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|ID of created trusted host group|

Example output:

```

{
  "id": "test-v14-group"
}

```

#### Update Trusted Host

Updates the values of given parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group_name|string|None|true|Name for the trusted host group|None|
|name|string|None|true|Name for the trusted host|None|
|address|string|None|true|IP address of the trusted host|None|
|mask|string|None|true|Associated subnet mask|None|
|comments|string|None|false|Description about the trusted host|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|ID of created trusted host group|

Example output:

```

{
  "id": "test-v14-trusted-host"
}

```

#### Delete Trusted Host

Deletes the given trusted host.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group_name|string|None|true|Name for the trusted host group|None|
|name|string|None|true|Name for the trusted host|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|true|Message of deleted|

Example output:

```

{
  "msg": "Successfully deleted"
}

```

#### Create Content Rule

Creates a content rule for the given service.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|virtual_service_id|string|None|true|Virtual Service ID|None|
|name|string|None|true|A name for the content rule|None|
|status|string|None|true|The status of the content rule|['on',of]|
|web_firewall_policy|string|None|true|A web firewall policy to be associated with the content rule|['default','sharepoint','sharepoint2013','owa','owa2010','owa2013','oracle']|
|host_match|string|None|true|A host name to be matched against the host in the request header|None|
|url_match|string|None|true|A URL to be matched to the URL in the request header|None|
|extended_match|string|None|true|An expression that consists of a combination of HTTP headers and/or query string parameters|None|
|extended_match_sequence|integer|None|true|A number to indicate the order in which the extended match rule must be evaluated in the requests|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|ID of content rule|

Example output:

```

{
  "id": "test-v14-content-rule"
}

```

#### Retrieve Content Rules

Lists all content rules.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|virtual_service_id|string|None|true|Virtual Service ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|ID content rule|
|lb_algorithm|string|true|The algorithm to be used for load balancing|
|extended_match_sequence|integer|true|The number to indicate the order in which the extended match rule must be evaluated in the requests|
|name|string|true|Name of content rule|
|host_match|string|true|The host name to be matched against the host in the request header|
|comments|string|true|Description about the content rule|
|extended_match|string|true|The expression that consists of a combination of HTTP headers and/or query string parameters|
|service_name|string|true|Service name|
|url_match|string|true|The URL to be matched to the URL in the request header|
|servers|array|true|Servers info|
|persistence_method|string|true|The Persistence Method to be used to maintain the connection between a client and the first server that it connects to, even when the system is load balancing traffic|

Example output:

```

[
  {
    "comments": null,
    "name": "test-v14-content-rule",
    "status": "on",
    "servers": [
      []
    ],
    "mode": "passive",
    "url_match": "/",
    "id": "test-v14-content-rule",
    "web_firewall_policy": "owa",
    "service_name": "test-v14-virtual-service",
    "extended_match_sequence": "1",
    "host_match": "test-v14-test.example.com",
    "extended_match": "*",
    "load_balance": {
      "lb_algorithm": "round_robin",
      "persistence_method": "none",
      "failover_method": "load_balance"
    }
  }
]

```

#### Retrieve Content Rules by ID

Lists all content rules with rule ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|true|Content rule ID|None|
|virtual_service_id|string|None|true|Virtual Service ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|ID content rule|
|lb_algorithm|string|true|The algorithm to be used for load balancing|
|extended_match_sequence|integer|true|The number to indicate the order in which the extended match rule must be evaluated in the requests|
|name|string|true|Name of content rule|
|host_match|string|true|The host name to be matched against the host in the request header|
|comments|string|true|Description about the content rule|
|extended_match|string|true|The expression that consists of a combination of HTTP headers and/or query string parameters|
|service_name|string|true|Service name|
|url_match|string|true|The URL to be matched to the URL in the request header|
|servers|array|true|Servers info|
|persistence_method|string|true|The Persistence Method to be used to maintain the connection between a client and the first server that it connects to, even when the system is load balancing traffic|

Example output:

```

[
  {
    "host_match": "test-v14-test.example.com",
    "web_firewall_policy": "owa",
    "url_match": "/",
    "name": "test-v14-content-rule",
    "service_name": "test-v14-virtual-service",
    "extended_match_sequence": "1",
    "mode": "passive",
    "servers": [
      []
    ],
    "load_balance": {
      "lb_algorithm": "round_robin",
      "failover_method": "load_balance",
      "persistence_method": "none"
    },
    "id": "test-v14-content-rule",
    "comments": null,
    "status": "on",
    "extended_match": "*"
  }
]

```

#### Delete Content Rule

Deletes the given content rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|true|Content rule ID|None|
|virtual_service_id|string|None|true|Virtual Service ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|true|Message of deleted|

Example output:

```

{
  "msg": "Successfully deleted"
}

```

#### Update Content Rule

Updates the values of given parameters in the given content rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|true|Content rule ID|None|
|virtual_service_id|string|None|true|Virtual Service ID|None|
|status|string|None|false|The status of the content rule|['on','off']|
|web_firewall_policy|string|None|false|A web firewall policy to be associated with the content rule|['default','sharepoint','sharepoint2013','owa','owa2010','owa2013','oracle']|
|host_match|string|None|false|A host name to be matched against the host in the request header|None|
|url_match|string|None|false|A URL to be matched to the URL in the request header|None|
|extended_match|string|None|false|An expression that consists of a combination of HTTP headers and/or query string parameters|None|
|extended_match_sequence|integer|None|false|A number to indicate the order in which the extended match rule must be evaluated in the requests|None|
|lb_algorithm|string|false|The algorithm to be used for load balancing|['round_robin','weighted_round_robin','least_requests']
|persistence_method|string|false|The Persistence Method to be used to maintain the connection between a client and the first server that it connects to, even when the system is load balancing traffic|
|failover_method|string|None|false|The failover method to be used when responding to a request which is persistent, but the server that must serve the request is failed or set to "Out-of-Service"|['load_balance','error']|
|persistence_idle_timeout|integer|None|false|The maximum idle time (in seconds) for a persistent connection. A client is directed to the same Real Server unless the connection is inactive for more than the specified number of seconds|None|
|source_ip_netmask|integer|None|false|A subnet mask to make subsequent connections from clients, from the same subnet go to the same Real Server|None|
|persistence_cookie_name|string|None|false|The name of the cookie that will be used for persistence|None|
|persistence_cookie_path|string|None|false|The path property of the persistency cookie|None|
|persistence_cookie_domain|string|None|false|The domain name of the server of a persistency cookie|None|
|cookie_age|integer|None|false|The expiry age of the persistence cookie in minutes|None|
|header_name|string|None|false|The name of the header for which the value needs to be checked in the HTTP requests|None|
|parameter_name|string|None|false|The name of the parameter for which the value needs to be checked in the URL|None|
|comments|string|None|false|Description about the content rule|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|true|Content rule ID|

Example output:

```

{
  "id": "test-v14-content-rule"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Barracuda Web Application Firewall](https://campus.barracuda.com/product/webapplicationfirewall/)
* [REST API](https://campus.barracuda.com/product/webapplicationfirewall/doc/73698476/rest-api-version-1-v1/)
* [Action policy attack names](https://campus.barracuda.com/product/webapplicationfirewall/doc/45026391/action-policy/)

