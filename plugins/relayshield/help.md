# Description

RelayShield detects identity and crypto-asset attack signals while an attack is still forming -- credential breaches, SIM-swap fraud, lookalike/typosquat domains, and wallet/token risk -- rather than after an account has already been taken over

# Key Features

* Check an email address against known credential breaches
* Check a phone number for active/recent SIM-swap fraud
* Check a domain for lookalike/typosquat registrations
* Check a crypto wallet address (and optional token contract) for composite risk

# Requirements

* A RelayShield API key from api.relayshield.net/developers

# Supported Product Versions

* RelayShield API v1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_secret_key|None|True|API key from api.relayshield.net/developers|None|rs_live_abcdefghijklmnopqrstuvwxyz0123|None|None|

Example input:

```
{
  "credentials": "rs_live_abcdefghijklmnopqrstuvwxyz0123"
}
```

## Technical Details

### Actions


#### Check Email Breach

This action is used to check an email address against known credential breach databases

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|True|Email address to check|None|user@example.com|None|None|
  
Example input:

```
{
  "email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|breach_count|integer|False|Number of breaches this email was found in|2|
|breaches|[]breach_record|False|List of breaches this email was found in|[{"name": "Adobe", "domain": "adobe.com", "breach_date": "2013-10-04", "data_classes": ["Email addresses", "Passwords"], "is_verified": True}]|
|email|string|False|The email address that was checked|user@example.com|
  
Example output:

```
{
  "breach_count": 2,
  "breaches": [
    {
      "breach_date": "2013-10-04",
      "data_classes": [
        "Email addresses",
        "Passwords"
      ],
      "domain": "adobe.com",
      "is_verified": true,
      "name": "Adobe"
    }
  ],
  "email": "user@example.com"
}
```

#### Check Crypto Wallet Intel

This action is used to check a crypto wallet address (and optional token contract) for composite risk, combining 
address reputation and token-contract risk into a single score

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|EVM wallet address to check (0x + 40 hex characters)|None|0x1234567890123456789012345678901234567890|None|None|
|chain_id|string|1|False|EVM chain ID to check against (default is Ethereum mainnet)|None|1|None|None|
|token_address|string|None|False|Optional EVM token contract address to also check|None|0x0987654321098765432109876543210987654321|None|None|
  
Example input:

```
{
  "address": "0x1234567890123456789012345678901234567890",
  "chain_id": 1,
  "token_address": "0x0987654321098765432109876543210987654321"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address|string|False|The wallet address that was checked|0x1234567890123456789012345678901234567890|
|address_flags|[]string|False|Risk flags found on the wallet address|[]|
|chain_id|string|False|The chain ID that was checked against|1|
|composite_risk|string|False|Overall risk level -- LOW, MEDIUM, HIGH, or CRITICAL|LOW|
|correlation_advisories|[]string|False|Recommended follow-up checks based on the risk signals found|["No risk signals detected on this address. For complete protection, monitor the associated email via check_breach and phone via check_sim_swap."]|
|token_risk|token_risk|False|Risk details for the token contract, if one was supplied|{}|
  
Example output:

```
{
  "address": "0x1234567890123456789012345678901234567890",
  "address_flags": [],
  "chain_id": 1,
  "composite_risk": "LOW",
  "correlation_advisories": [
    "No risk signals detected on this address. For complete protection, monitor the associated email via check_breach and phone via check_sim_swap."
  ],
  "token_risk": {}
}
```

#### Check Domain Lookalikes

This action is used to check a domain for lookalike/typosquat registrations that may be used for phishing

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain to check for lookalikes (e.g. example.com)|None|example.com|None|None|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|domain|string|False|The domain that was checked|example.com|
|lookalikes|[]lookalike_domain|False|List of lookalike domains found|[{"domain": "exarnple.com", "gsb_flagged": False, "registration_age_days": 4, "cert_count": 1, "cert_recent": True, "latest_cert_issued": "2026-07-20T00:00:00Z"}]|
|lookalikes_found|integer|False|Number of lookalike domains found|1|
  
Example output:

```
{
  "domain": "example.com",
  "lookalikes": [
    {
      "cert_count": 1,
      "cert_recent": true,
      "domain": "exarnple.com",
      "gsb_flagged": false,
      "latest_cert_issued": "2026-07-20T00:00:00Z",
      "registration_age_days": 4
    }
  ],
  "lookalikes_found": 1
}
```

#### Check SIM Swap

This action is used to check a phone number for active or recent SIM-swap fraud at the carrier level

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|phone|string|None|True|Phone number in E.164 format (e.g. +14155551234)|None|+14155551234|None|None|
  
Example input:

```
{
  "phone": "+14155551234"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|carrier|string|False|Carrier name associated with the phone number|Verizon|
|phone|string|False|The phone number that was checked|+14155551234|
|swap_timestamp|string|False|Timestamp of the most recent SIM swap, if any|2026-07-20T00:00:00Z|
|swapped|boolean|False|Whether a SIM swap occurred within the lookback window|False|
  
Example output:

```
{
  "carrier": "Verizon",
  "phone": "+14155551234",
  "swap_timestamp": "2026-07-20T00:00:00Z",
  "swapped": false
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**breach_record**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Breach Date|string|None|False|Date the breach occurred|2013-10-04|
|Data Classes|[]string|None|False|Categories of data exposed in the breach|["Email addresses", "Passwords"]|
|Breach Domain|string|None|False|Domain associated with the breach|adobe.com|
|Verified|boolean|None|False|Whether the breach has been verified|True|
|Breach Name|string|None|False|Name of the breach source|Adobe|
  
**lookalike_domain**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Certificate Count|integer|None|False|Number of TLS certificates issued for the domain|1|
|Recent Certificate|boolean|None|False|Whether a TLS certificate was issued recently|True|
|Lookalike Domain|string|None|False|The lookalike/typosquat domain found|relayshie1d.net|
|Google Safe Browsing Flagged|boolean|None|False|Whether Google Safe Browsing has flagged this domain|False|
|Latest Certificate Issued|string|None|False|Timestamp of the most recent TLS certificate|2026-07-20T00:00:00Z|
|Registration Age (Days)|integer|None|False|Days since the lookalike domain was registered|4|
  
**token_risk**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Contract Address|string|None|False|The token contract address checked|0x1234567890123456789012345678901234567890|
|Critical Flags|[]string|None|False|Critical risk indicators found on the token contract|["honeypot"]|
|Token Name|string|None|False|Name of the token|Example Token|
|Token Symbol|string|None|False|Symbol of the token|EXT|
|Warning Flags|[]string|None|False|Warning-level risk indicators found on the token contract|["mintable supply"]|


## Troubleshooting


# Version History

* 1.0.0 - Initial plugin.

# Links

* [RelayShield](https://relayshield.net)

## References

* [RelayShield Developer Docs](https://api.relayshield.net/developers)