# Description

Determine if a user, domain, or password has been leaked via data available in the Have I Been Pwned database

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
*This plugin does not contain any supported product versions.*

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|API key|None|None|
  
Example input:

```
{
  "api_key": {
    "secretKey": ""
  }
}
```

## Technical Details

### Actions


#### Lookup Domain
  
List domain breaches

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|False|Domain to check E.g. adobe.com, google.com etc. If left blank will return the full breach database. Warning: this is very large|None|None|
|include_unverified|boolean|False|True|If true will include breaches that are unverified|None|None|
|truncate_response|boolean|True|True|If true only name of breach will be shown|None|None|
  
Example input:

```
{
  "domain": "",
  "include_unverified": false,
  "truncate_response": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|breaches|[]domain|False|List of details for each breach found|None|
|found|boolean|True|Indicates whether or not a breach for the specified domain was found|None|
  
Example output:

```
{
  "breaches": [
    {
      "Added Date": {},
      "Breach Date": {},
      "Data Classes": [
        {}
      ],
      "Description": {},
      "Domain": {},
      "Is Active": {},
      "Is Fabricated": {},
      "Is Retired": {},
      "Is Sensitive": {},
      "Is Spam List": {},
      "Is Verified": "true",
      "Logo Type": {},
      "Modified Date": {},
      "Name": {},
      "Pwn Count": 0,
      "Title": ""
    }
  ],
  "found": true
}
```

#### Lookup Password
  
Lookup a password in list of known breached passwords

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|original_password_is_a_hash|boolean|None|True|Whether the password itself is a SHA1 hash|None|None|
|password|string|None|True|Password to check E.g. 'P@ssw0rd'|None|None|
  
Example input:

```
{
  "original_password_is_a_hash": true,
  "password": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|True|If true the password was found in the database|None|
  
Example output:

```
{
  "found": true
}
```

#### Lookup User
  
Check an email for compromise

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|breach|string|None|False|Breach Site to check e.g. adobe.com. If blank will check all known breaches|None|None|
|include_unverified|boolean|False|True|If true will include breaches that are unverified|None|None|
|truncate_response|boolean|True|True|If true only name of breach will be shown|None|None|
|user|string|None|True|Email to check|None|None|
  
Example input:

```
{
  "breach": "",
  "include_unverified": false,
  "truncate_response": true,
  "user": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|breaches|[]domain|False|List of details for each breach found or email|None|
|found|boolean|True|Found|None|
  
Example output:

```
{
  "breaches": [
    {
      "Added Date": {},
      "Breach Date": {},
      "Data Classes": [
        {}
      ],
      "Description": {},
      "Domain": {},
      "Is Active": {},
      "Is Fabricated": {},
      "Is Retired": {},
      "Is Sensitive": {},
      "Is Spam List": {},
      "Is Verified": "true",
      "Logo Type": {},
      "Modified Date": {},
      "Name": {},
      "Pwn Count": 0,
      "Title": ""
    }
  ],
  "found": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**domain**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Added Date|string|None|None|The date and time (precision to the minute) the breach was added to the system in ISO 8601 format|None|
|Breach Date|string|None|None|The date (with no time) the breach originally occurred on in ISO 8601 format|None|
|Data Classes|[]string|None|None|This attribute describes the nature of the data compromised in the breach and contains an alphabetically ordered string array of impacted data classes|None|
|Description|string|None|None|Contains an overview of the breach represented in HTML markup. The description may include markup such as emphasis and strong tags as well as hyperlinks|None|
|Domain|string|None|None|The domain of the primary website the breach occurred on|None|
|Is Active|boolean|None|None|Indicates if the breach investigation is ongoing.|None|
|Is Fabricated|boolean|None|None|Indicates that the breach is considered fabricated. A fabricated breach is unlikely to have been hacked from the indicated website and usually contains a large amount of manufactured data. However, it still contains legitimate email addresses and asserts that the account owners were compromised in the alleged breach|None|
|Is Retired|boolean|None|None|Indicates if the breach has been retired|None|
|Is Sensitive|boolean|None|None|Indicates if the breach is considered sensitive. The public API will not return any accounts for a breach flagged as sensitive|None|
|Is Spam List|boolean|None|None|Indicates if the breach is considered a spam list. This flag has no impact on any other attributes but it means that the data has not come as a result of a security compromise|None|
|Is Verified|boolean|None|None|Indicates that the breach is considered verified|None|
|Logo Type|string|None|None|Indicates what type of file the breach logo is|None|
|Modified Date|string|None|None|The date and time (precision to the minute) the breach was modified in ISO 8601 format|None|
|Name|string|None|None|A Pascal-cased name representing the breach which is unique across all other breaches|None|
|Pwn Count|integer|None|None|The total number of accounts loaded into the system|None|
|Title|string|None|None|A descriptive title for the breach suitable for displaying to end users|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History
  
*This plugin does not contain a version history.*

# Links


## References
  
*This plugin does not contain any references.*