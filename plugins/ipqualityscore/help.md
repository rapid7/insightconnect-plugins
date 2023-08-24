# Description
  
IPQS Fraud and Risk Scoring plugin provides enterprise grade fraud prevention, risk analysis, and threat detection Analyze IP Addresses, Email Addresses, Phones, URLs and Domains to identify sophisticated bad actors and high risk behavior.  

# Key Features

 * Get email address reputation.
 * Get IP address reputation.
 * Get domain reputation.
 * Get URL reputation.
 * Get phone number reputation.

# Requirements

* IPQualityScore API Key.

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|apiKey|credential_secret_key|None|True|IPQualityScore API Key|None|abcdef12345|
  
Example input:

```
{
  "apiKey": "abcdef12345"
}
```

## Technical Details

### Actions
  

#### Domain Reputation
  
This action is used to get domain reputation data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fast|boolean|False|False|When enabled, the API will provide quicker response times using lighter checks and analysis This setting defaults to False|None|False|
|strictness|integer|0|True|How strict should we scan this Domain? Stricter checks may provide a higher false-positive rate We recommend defaulting to level 0, the lowest strictness setting, and increasing to 1 or 2 depending on your levels of abuse|[0, 1, 2]|0|
|url|string|None|True|Domain|None|https://abc.com|
  
Example input:

```
{
  "fast": false,
  "strictness": 0,
  "url": "https://abc.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|adult|boolean|False|Is this URL or domain hosting dating or adult content?|False|
|category|string|False|Website classification and category related to the content and industry of the site Over 70 categories are available including Video Streaming, Trackers, Gaming, Privacy, Advertising, Hacking, Malicious, Phishing, etc The value will be NA if unknown|Search Engines|
|dns_valid|boolean|False|The domain has valid DNS records?|False|
|domain|string|False|Domain name of the final destination URL of the scanned link, after following all redirects|https://abc.com|
|domain_age|object|False|A human description of when this domain was registered|{"human": "26 years ago", "timestamp": 874296000,"iso": "1997-09-15T00:00:00-04:00"}|
|domain_rank|integer|False|Estimated popularity rank of website globally Value is 0 if the domain is unranked or has low traffic|0|
|ip_address|string|False|IP address For example nginx1 Value will be NA if unavailable|1.1.1.1|
|malware|boolean|False|Is this domain associated with malware or viruses?|False|
|parking|boolean|False|Is the domain currently parked with a for sale notice?|False|
|phishing|boolean|False|Is this domain associated with malicious phishing behavior?|False|
|risk_score|integer|False|The IPQS risk score which estimates the confidence level for malicious URL detection Risk Scores 85+ are high risk, while Risk Scores = 100 are confirmed as accurate|0|
|server|string|False|The server banner of the domain's IP address For example  nginx Value will be NA if unavailable|nginx/1.16.0|
|spamming|boolean|False|Is the domain  associated with email SPAM or abusive email addresses?|False|
|suspicious|boolean|False|Is this URL suspected of being malicious or used for phishing or abuse? Use in conjunction with the risk_score as a confidence level|False|
|unsafe|boolean|False|Is this domain suspected of being unsafe due to phishing, malware, spamming, or abusive behavior? View the confidence level by analyzing the risk_score|False|
  
Example output:

```
{
  "adult": false,
  "category": "Search Engines",
  "dns_valid": false,
  "domain": "https://abc.com",
  "domain_age": {
    "human": "26 years ago",
    "iso": "1997-09-15T00:00:00-04:00",
    "timestamp": 874296000
  },
  "domain_rank": 0,
  "ip_address": "1.1.1.1",
  "malware": false,
  "parking": false,
  "phishing": false,
  "risk_score": 0,
  "server": "nginx/1.16.0",
  "spamming": false,
  "suspicious": false,
  "unsafe": false
}
```

#### Email Address Reputation
  
This action is used to get email address reputation data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|abuse_strictness|integer|0|True|Set the strictness level for machine learning pattern recognition of abusive email addresses with the recent_abuse data point|[0, 1, 2]|0|
|emailAddress|string|None|True|Email address for which information is desired|None|user@example.com|
|fast|boolean|False|False|When this parameter is enabled our API will not perform an SMTP check with the mail service provider, which greatly increases the API speed|None|False|
|suggest_domain|boolean|False|False|Force analyze if the email addresses domain has a typo and should be corrected to a popular mail service|None|False|
|timeout|integer|None|False|Maximum number of seconds to wait for a reply from a mail service provider If your implementation requirements do not need an immediate response, we recommend bumping this value to 20|None|5|
  
Example input:

```
{
  "abuse_strictness": 0,
  "emailAddress": "user@example.com",
  "fast": false,
  "suggest_domain": false,
  "timeout": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|catch_all|boolean|False|Is this email likely to be a catch all where the mail server verifies all emails tested against it as valid? It is difficult to determine if the address is truly valid in these scenarios, since the email's server will not confirm the account's status|False|
|common|boolean|False|Is this email from a common email provider?|False|
|deliverability|string|False|How likely is this email to be delivered to the user and land in their mailbox Values can be high, medium, or low|high|
|disposable|boolean|False|Is this email suspected of belonging to a temporary or disposable mail service? Usually associated with fraudsters and scammers|False|
|dns_valid|boolean|False|Does the email's hostname have valid DNS entries? Partial indication of a valid email|False|
|domain_age|object|False|A human description of when this domain was registered|{"human": "26 years ago", "timestamp": 874296000,"iso": "1997-09-15T00:00:00-04:00"}|
|first_name|string|False|Suspected first name based on email Returns CORPORATE if the email is suspected of being a generic company email Returns UNKNOWN if the first name was not determinable|CORPORATE|
|first_seen|object|False|A human description of the email address age, using an estimation of the email creation date when IPQS first discovered this email address|{"human": "26 years ago", "timestamp": 874296000,"iso": "1997-09-15T00:00:00-04:00"}|
|fraud_score|integer|False|The overall Fraud Score of the user based on the email's reputation and recent behavior across the IPQS threat network Fraud Scores >= 75 are suspicious, but not necessarily fraudulent|0|
|frequent_complainer|boolean|False|Indicates if this email frequently unsubscribes from marketing lists or reports email as SPAM|False|
|generic|boolean|False|Is this email suspected as being a catch all or shared email for a domain? (admin@, webmaster@, newsletter@, sales@, contact@, etc)|False|
|honeypot|boolean|False|Is this email believed to be a honeypot or SPAM trap? Bulk mail sent to these emails increases your risk of being blacklisted by large ISPs & ending up in the spam folder|False|
|leaked|boolean|False|Was this email address associated with a recent database leak from a third party? Leaked accounts pose a risk as they may have become compromised during a database breach|False|
|overall_score|integer|False|Overall email validity score Range is 0 - 4 Scores above 1 can be associated with a valid email 0 = invalid email address 1 = DNS valid, unreachable mail server 2 = DNS valid, temporary mail rejection error 3 = DNS valid, accepts all mail 4 = DNS valid, verified email exists|0|
|recent_abuse|boolean|False|This value will indicate if there has been any recently verified abuse across our network for this email address Abuse could be a confirmed chargeback, fake signup, compromised device, fake app install, or similar malicious behavior within the past few days|False|
|sanitized_email|string|False|Sanitized email address with all aliases and masking removed, such as multiple periods for Gmail|user@example.com|
|smtp_score|integer|False|Validity score of email server's SMTP setup Range is -1 - 3 Scores above -1 can be associated with a valid email -1 = invalid email address 0 = mail server exists, but is rejecting all mail 1 = mail server exists, but is showing a temporary error 2 = mail server exists, but accepts all email 3 = mail server exists and has verified the email address|1|
|spam_trap_score|string|False|Confidence level of the email address being an active SPAM trap Values can be high, medium, low, or none We recommend scrubbing emails with high or medium statuses Avoid low emails whenever possible for any promotional mailings|high|
|suggested_domain|string|False|Default value is NA Indicates if this email's domain should in fact be corrected to a popular mail service This field is useful for catching user typos For example, an email address with gmail, would display a suggested domain of gmail his feature supports all major mail service providers|NA|
|suspect|boolean|False|This value indicates if the mail server is currently replying with a temporary error and unable to verify the email address This status will also be true for catch all email addresses as defined below If this value is true, then we suspect the valid result may be cotaminated and there is not a guarantee that the email address is truly valid|False|
|timed_out|boolean|False|Did the connection to the mail service provider timeout during the verification? If so, we recommend increasing the timeout variable above the default 7 second value Lookups that timeout with a valid result as false are most likely false and should be not be trusted|False|
|valid|boolean|False|Does this email address appear valid?|False|
  
Example output:

```
{
  "catch_all": false,
  "common": false,
  "deliverability": "high",
  "disposable": false,
  "dns_valid": false,
  "domain_age": {
    "human": "26 years ago",
    "iso": "1997-09-15T00:00:00-04:00",
    "timestamp": 874296000
  },
  "first_name": "CORPORATE",
  "first_seen": {
    "human": "26 years ago",
    "iso": "1997-09-15T00:00:00-04:00",
    "timestamp": 874296000
  },
  "fraud_score": 0,
  "frequent_complainer": false,
  "generic": false,
  "honeypot": false,
  "leaked": false,
  "overall_score": 0,
  "recent_abuse": false,
  "sanitized_email": "user@example.com",
  "smtp_score": 1,
  "spam_trap_score": "high",
  "suggested_domain": "NA",
  "suspect": false,
  "timed_out": false,
  "valid": false
}
```

#### IP Address Reputation
  
This action is used to get IP address reputation data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|allow_public_access_points|boolean|False|False|Bypasses certain checks for IP addresses from education and research institutions, schools, and some corporate connections to better accommodate audiences that frequently use public connections|None|False|
|fast|boolean|False|False|When this parameter is enabled our API will not perform certain forensic checks that take longer to process Enabling this feature greatly increases the API speed without much impact on accuracy|None|False|
|ipAddress|string|None|True|IP address for which information is desired|None|1.1.1.1|
|lighter_penalties|boolean|False|False|Skip some blacklists which can cause false-positives for sensitive audiences|None|False|
|mobile|boolean|False|False|You can optionally specify that this lookup should be treated as a mobile device Recommended for mobile lookups that do not have a user agent attached to the request|None|False|
|strictness|integer|0|True|How in depth (strict) do you want this query to be? Higher values take longer to process and may provide a higher false-positive rate We recommend starting at 0, the lowest strictness setting, and increasing to 1 or 2 depending on your levels of fraud|[0, 1, 2]|0|
|user_agent|string|None|False|You can optionally provide us with the user agent string (browser) This allows us to run additional checks to see if the user is a bot or running an invalid browser This allows us to evaluate the risk of the user as judged in the fraud_score|None|Browser|
|user_language|string|None|False|You can optionally provide us with the user's language header This allows us to evaluate the risk of the user as judged in the fraud_score|None|English|
  
Example input:

```
{
  "allow_public_access_points": false,
  "fast": false,
  "ipAddress": "1.1.1.1",
  "lighter_penalties": false,
  "mobile": false,
  "strictness": 0,
  "user_agent": "Browser",
  "user_language": "English"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ASN|integer|False|Autonomous System Number if one is known Null if nonexistent|15169|
|ISP|string|False|ISP if one is known Otherwise NA|Google|
|Organization|string|False|Organization if one is known Can be parent company or sub company of the listed ISP Otherwise NA|Google|
|abuse_velocity|string|False|Premium Account Feature - How frequently the IP address is engaging in abuse across the IPQS threat network Values can be high, medium, low, or none Can be used in combination with the Fraud Score to identify bad behavior|none|
|active_tor|boolean|False|Premium Account Feature - Identifies active TOR exits on the TOR network|False|
|active_vpn|boolean|False|Premium Account Feature - Identifies active VPN connections used by popular VPN services and private VPN servers|False|
|bot_status|boolean|False|Premium Account Feature - Indicates if bots or non-human traffic has recently used this IP address to engage in automated fraudulent behavior Provides stronger confidence that the IP address is suspicious|False|
|city|string|False|City of IP address if available or NA if unknown|Delhi|
|connection_type|string|False|Classification of the IP address connection type as Residential, Corporate, Education, Mobile, or Data Center|Data Center|
|country_code|string|False|Two character country code of IP address or NA if unknown|0|
|fraud_score|integer|False|The overall fraud score of the user based on the IP, user agent, language, and any other optionally passed variables Fraud Scores >= 75 are suspicious, but not necessarily fraudulent We recommend flagging or blocking traffic with Fraud Scores >= 85, but you may find it beneficial to use a higher or lower threshold|0|
|host|string|False|Hostname of the IP address if one is available|dns.google|
|is_crawler|boolean|False|Is this IP associated with being a confirmed crawler from a mainstream search engine such as Googlebot, Bingbot, Yandex, etc based on hostname or IP address verification|False|
|latitude|float|False|Latitude of IP address if available or NA if unknown|34.0544014|
|longitude|float|False|Longitude of IP address if available or NA if unknown|-118.24410248|
|mobile|boolean|False|Is this user agent a mobile browser? (will always be false if the user agent is not passed in the API request)|False|
|proxy|boolean|False|Is this IP address suspected to be a proxy? (SOCKS, Elite, Anonymous, VPN, Tor, etc)|False|
|recent_abuse|boolean|False|This value will indicate if there has been any recently verified abuse across our network for this IP address Abuse could be a confirmed chargeback, compromised device, fake app install, or similar malicious behavior within the past few days|False|
|region|string|False|Region (state) of IP address if available or NA if unknown|India|
|timezone|string|False|Timezone of IP address if available or NA if unknown|America/Los_Angeles|
|tor|boolean|False|Is this IP suspected of being a TOR connection? This can include previously active TOR nodes and exits which can become active TOR exits at any time The proxy status will always be true when this value is true|False|
|vpn|boolean|False|Is this IP suspected of being a VPN connection? This can include data center ranges which can become active VPNs at any time The proxy status will always be true when this value is true|False|
|zip_code|string|False|ZIP or Postal code of the IP Address if available or NA if unknown|505001|
  
Example output:

```
{
  "ASN": 15169,
  "ISP": "Google",
  "Organization": "Google",
  "abuse_velocity": "none",
  "active_tor": false,
  "active_vpn": false,
  "bot_status": false,
  "city": "Delhi",
  "connection_type": "Data Center",
  "country_code": 0,
  "fraud_score": 0,
  "host": "dns.google",
  "is_crawler": false,
  "latitude": 34.0544014,
  "longitude": -118.24410248,
  "mobile": false,
  "proxy": false,
  "recent_abuse": false,
  "region": "India",
  "timezone": "America/Los_Angeles",
  "tor": false,
  "vpn": false,
  "zip_code": 505001
}
```

#### Phone Reputation
  
This action is used to get phone number reputation data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|country|string|None|False|You can optionally provide us with the default country or countries(comma separated) this phone number is suspected to be associated with Our system will prefer to use a country on this list for verification or will require a country to be specified in the event the phone number is less than 10 digits|None|US|
|phone|string|None|True|Phone for which information is desired|None|+918765433210|
|strictness|integer|0|True|How in depth (strict) do you want this query to be? Higher values take longer to process and may provide a higher false-positive rate We recommend starting at 0, the lowest strictness setting, and increasing to 1 or 2 depending on your levels of fraud|[0, 1, 2]|0|
  
Example input:

```
{
  "country": "US",
  "phone": "+918765433210",
  "strictness": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|VOIP|boolean|False|Is this phone number a Voice Over Internet Protocol (VOIP) or digital phone number?|False|
|active|boolean|False|Is this phone number a live usable phone number that is currently active?|False|
|active_status|string|False|Additional details on the status of the subscriber connection when enhanced active line checks are enabled These values can be Active Line, Disconnected Line, Phone Turned Off, Inconclusive Status, or NA if unknown|Disconnected Line|
|carrier|string|False|The carrier (service provider) this phone number has been assigned to or NA if unknown|airtel|
|city|string|False|City of the phone number if available or NA if unknown|Delhi|
|country|string|False|The two character country code for this phone number|IN|
|dialing_code|integer|False|The 1 to 4 digit dialing code for this phone number or null if unknown|0|
|do_not_call|boolean|False|Indicates if the phone number is listed on any Do Not Call (DNC) lists Only supported in US and CA This data may not be 100% up to date with the latest DNC blacklists|False|
|formatted|string|False|The phone number formatted in the international dialing code NA if not formattable|+917133457890|
|fraud_score|integer|False|The IPQS risk score which estimates how likely a phone number is to be fraudulent Scores 85+ are high risk|0|
|leaked|boolean|False|Was this phone number associated with a recent database leak from a third party? Leaked accounts pose a risk as they may have become compromised during a database breach|False|
|line_type|string|False|The type of line this phone number is associated with (Toll Free, Mobile, Landline, Satellite, VOIP, Premium Rate, Pager, etc) or NA if unknown|Wireless|
|local_format|string|False|The phone number formatted in the country's local routing rules with area code NA if not formattable|+91|
|name|string|False|The owner name of the phone number such as the first or last name or business name assigned to the phone number Multiple names will be returned in comma separated format Value is NA if unknown|Jhon|
|prepaid|boolean|False|Is this phone number associated with a prepaid service plan?|False|
|recent_abuse|boolean|False|Has this phone number been associated with recent or ongoing fraud?|False|
|region|string|False|Region (state) of the phone number if available or NA if unknown|India|
|risky|boolean|False|Is this phone number associated with fraudulent activity, scams, robo calls, fake accounts, or other unfriendly behavior?|False|
|timezone|string|False|Timezone of the phone number if available or NA if unknown|Asia/Kolkata|
|valid|boolean|False|Is the phone number properly formatted and considered valid based on assigned phone numbers available to carriers in that country?|False|
|zip_code|string|False|ZIP or Postal code of the phone number if available or NA if unknown|500081|
  
Example output:

```
{
  "VOIP": false,
  "active": false,
  "active_status": "Disconnected Line",
  "carrier": "airtel",
  "city": "Delhi",
  "country": "IN",
  "dialing_code": 0,
  "do_not_call": false,
  "formatted": "+917133457890",
  "fraud_score": 0,
  "leaked": false,
  "line_type": "Wireless",
  "local_format": "+91",
  "name": "Jhon",
  "prepaid": false,
  "recent_abuse": false,
  "region": "India",
  "risky": false,
  "timezone": "Asia/Kolkata",
  "valid": false,
  "zip_code": 500081
}
```

#### URL Reputation
  
This action is used to get URL reputation data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fast|boolean|False|False|When enabled, the API will provide quicker response times using lighter checks and analysis This setting defaults to False|None|False|
|strictness|integer|0|True|How strict should we scan this URL? Stricter checks may provide a higher false-positive rate We recommend defaulting to level 0, the lowest strictness setting, and increasing to 1 or 2 depending on your levels of abuse|[0, 1, 2]|0|
|url|string|None|True|URL for which information is desired|None|https://abc.com|
  
Example input:

```
{
  "fast": false,
  "strictness": 0,
  "url": "https://abc.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|adult|boolean|False|Is this URL or domain hosting dating or adult content?|False|
|category|string|False|Website classification and category related to the content and industry of the site Over 70 categories are available including Video Streaming, Trackers, Gaming, Privacy, Advertising, Hacking, Malicious, Phishing, etc The value will be NA if unknown|Search Engines|
|dns_valid|boolean|False|The domain of the URL has valid DNS records|False|
|domain|string|False|Domain name of the final destination URL of the scanned link, after following all redirects|https://abc.com|
|domain_age|object|False|A human description of when this domain was registered|{"human": "26 years ago", "timestamp": 874296000,"iso": "1997-09-15T00:00:00-04:00"}|
|domain_rank|integer|False|Estimated popularity rank of website globally Value is 0 if the domain is unranked or has low traffic|0|
|ip_address|string|False|IP address For example nginx Value will be NA if unavailable|1.1.1.1|
|malware|boolean|False|Is this URL associated with malware or viruses?|False|
|parking|boolean|False|Is the domain of this URL currently parked with a for sale notice?|False|
|phishing|boolean|False|Is this URL associated with malicious phishing behavior?|False|
|risk_score|integer|False|The IPQS risk score which estimates the confidence level for malicious URL detection Risk Scores 85+ are high risk, while Risk Scores = 100 are confirmed as accurate|0|
|server|string|False|The server banner of the domain's IP address For example  nginx Value will be NA if unavailable|nginx/1.16.0|
|spamming|boolean|False|Is the domain of this URL associated with email SPAM or abusive email addresses?|False|
|suspicious|boolean|False|Is this URL suspected of being malicious or used for phishing or abuse? Use in conjunction with the risk_score as a confidence level|False|
|unsafe|boolean|False|Is this domain suspected of being unsafe due to phishing, malware, spamming, or abusive behavior? View the confidence level by analyzing the risk_score|False|
  
Example output:

```
{
  "adult": false,
  "category": "Search Engines",
  "dns_valid": false,
  "domain": "https://abc.com",
  "domain_age": {
    "human": "26 years ago",
    "iso": "1997-09-15T00:00:00-04:00",
    "timestamp": 874296000
  },
  "domain_rank": 0,
  "ip_address": "1.1.1.1",
  "malware": false,
  "parking": false,
  "phishing": false,
  "risk_score": 0,
  "server": "nginx/1.16.0",
  "spamming": false,
  "suspicious": false,
  "unsafe": false
}
```
### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

* [IPQS Fraud and Risk Scoring](https://www.ipqualityscore.com/)

## References

* [IPQS Fraud and Risk Scoring](https://www.ipqualityscore.com/)
