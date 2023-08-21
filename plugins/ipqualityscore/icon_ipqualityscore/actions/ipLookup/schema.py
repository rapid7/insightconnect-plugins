# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "IP Address Reputation"


class Input:
    ALLOW_PUBLIC_ACCESS_POINTS = "allow_public_access_points"
    FAST = "fast"
    IPADDRESS = "ipAddress"
    LIGHTER_PENALTIES = "lighter_penalties"
    MOBILE = "mobile"
    STRICTNESS = "strictness"
    USER_AGENT = "user_agent"
    USER_LANGUAGE = "user_language"


class Output:
    ABUSE_VELOCITY = "abuse_velocity"
    ACTIVE_TOR = "active_tor"
    ACTIVE_VPN = "active_vpn"
    ASN = "ASN"
    BOT_STATUS = "bot_status"
    CITY = "city"
    CONNECTION_TYPE = "connection_type"
    COUNTRY_CODE = "country_code"
    FRAUD_SCORE = "fraud_score"
    HOST = "host"
    IS_CRAWLER = "is_crawler"
    ISP = "ISP"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    MOBILE = "mobile"
    ORGANIZATION = "Organization"
    PROXY = "proxy"
    RECENT_ABUSE = "recent_abuse"
    REGION = "region"
    TIMEZONE = "timezone"
    TOR = "tor"
    VPN = "vpn"
    ZIP_CODE = "zip_code"


class IpLookupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "allow_public_access_points": {
      "type": "boolean",
      "title": "Allow Public Access Points",
      "description": "Bypasses certain checks for IP addresses from education and research institutions, schools, and some corporate connections to better accommodate audiences that frequently use public connections",
      "default": false,
      "order": 7
    },
    "fast": {
      "type": "boolean",
      "title": "Fast",
      "description": "When this parameter is enabled our API will not perform certain forensic checks that take longer to process Enabling this feature greatly increases the API speed without much impact on accuracy",
      "default": false,
      "order": 5
    },
    "ipAddress": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address for which information is desired",
      "order": 1
    },
    "lighter_penalties": {
      "type": "boolean",
      "title": "Lighter Penalties",
      "description": "Skip some blacklists which can cause false-positives for sensitive audiences",
      "default": false,
      "order": 8
    },
    "mobile": {
      "type": "boolean",
      "title": "Mobile",
      "description": "You can optionally specify that this lookup should be treated as a mobile device Recommended for mobile lookups that do not have a user agent attached to the request",
      "default": false,
      "order": 6
    },
    "strictness": {
      "type": "integer",
      "title": "Strictness",
      "description": "How in depth (strict) do you want this query to be? Higher values take longer to process and may provide a higher false-positive rate We recommend starting at 0, the lowest strictness setting, and increasing to 1 or 2 depending on your levels of fraud",
      "default": 0,
      "enum": [
        0,
        1,
        2
      ],
      "order": 2
    },
    "user_agent": {
      "type": "string",
      "title": "User Agent",
      "description": "You can optionally provide us with the user agent string (browser) This allows us to run additional checks to see if the user is a bot or running an invalid browser This allows us to evaluate the risk of the user as judged in the fraud_score",
      "order": 3
    },
    "user_language": {
      "type": "string",
      "title": "User Language",
      "description": "You can optionally provide us with the user's language header This allows us to evaluate the risk of the user as judged in the fraud_score",
      "order": 4
    }
  },
  "required": [
    "ipAddress",
    "strictness"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IpLookupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ASN": {
      "type": "integer",
      "title": "ASN",
      "description": "Autonomous System Number if one is known Null if nonexistent",
      "order": 7
    },
    "ISP": {
      "type": "string",
      "title": "ISP",
      "description": "ISP if one is known Otherwise NA",
      "order": 6
    },
    "Organization": {
      "type": "string",
      "title": "Organization",
      "description": "Organization if one is known Can be parent company or sub company of the listed ISP Otherwise NA",
      "order": 8
    },
    "abuse_velocity": {
      "type": "string",
      "title": "Abuse Velocity",
      "description": "Premium Account Feature - How frequently the IP address is engaging in abuse across the IPQS threat network Values can be high, medium, low, or none Can be used in combination with the Fraud Score to identify bad behavior",
      "order": 21
    },
    "active_tor": {
      "type": "boolean",
      "title": "Active TOR",
      "description": "Premium Account Feature - Identifies active TOR exits on the TOR network",
      "order": 17
    },
    "active_vpn": {
      "type": "boolean",
      "title": "Active VPN",
      "description": "Premium Account Feature - Identifies active VPN connections used by popular VPN services and private VPN servers",
      "order": 16
    },
    "bot_status": {
      "type": "boolean",
      "title": "Bot Status",
      "description": "Premium Account Feature - Indicates if bots or non-human traffic has recently used this IP address to engage in automated fraudulent behavior Provides stronger confidence that the IP address is suspicious",
      "order": 19
    },
    "city": {
      "type": "string",
      "title": "City",
      "description": "City of IP address if available or NA if unknown",
      "order": 4
    },
    "connection_type": {
      "type": "string",
      "title": "Connection Type",
      "description": "Classification of the IP address connection type as Residential, Corporate, Education, Mobile, or Data Center",
      "order": 20
    },
    "country_code": {
      "type": "string",
      "title": "Country Code",
      "description": "Two character country code of IP address or NA if unknown",
      "order": 2
    },
    "fraud_score": {
      "type": "integer",
      "title": "Fraud Score",
      "description": "The overall fraud score of the user based on the IP, user agent, language, and any other optionally passed variables Fraud Scores >= 75 are suspicious, but not necessarily fraudulent We recommend flagging or blocking traffic with Fraud Scores >= 85, but you may find it beneficial to use a higher or lower threshold",
      "order": 1
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Hostname of the IP address if one is available",
      "order": 12
    },
    "is_crawler": {
      "type": "boolean",
      "title": "Is Crawler",
      "description": "Is this IP associated with being a confirmed crawler from a mainstream search engine such as Googlebot, Bingbot, Yandex, etc based on hostname or IP address verification",
      "order": 9
    },
    "latitude": {
      "type": "number",
      "title": "Latitude",
      "description": "Latitude of IP address if available or NA if unknown",
      "order": 22
    },
    "longitude": {
      "type": "number",
      "title": "Longitude",
      "description": "Longitude of IP address if available or NA if unknown",
      "order": 23
    },
    "mobile": {
      "type": "boolean",
      "title": "Mobile",
      "description": "Is this user agent a mobile browser? (will always be false if the user agent is not passed in the API request)",
      "order": 11
    },
    "proxy": {
      "type": "boolean",
      "title": "Proxy",
      "description": "Is this IP address suspected to be a proxy? (SOCKS, Elite, Anonymous, VPN, Tor, etc)",
      "order": 13
    },
    "recent_abuse": {
      "type": "boolean",
      "title": "Recent Abuse",
      "description": "This value will indicate if there has been any recently verified abuse across our network for this IP address Abuse could be a confirmed chargeback, compromised device, fake app install, or similar malicious behavior within the past few days",
      "order": 18
    },
    "region": {
      "type": "string",
      "title": "Region",
      "description": "Region (state) of IP address if available or NA if unknown",
      "order": 3
    },
    "timezone": {
      "type": "string",
      "title": "Timezone",
      "description": "Timezone of IP address if available or NA if unknown",
      "order": 10
    },
    "tor": {
      "type": "boolean",
      "title": "TOR",
      "description": "Is this IP suspected of being a TOR connection? This can include previously active TOR nodes and exits which can become active TOR exits at any time The proxy status will always be true when this value is true",
      "order": 15
    },
    "vpn": {
      "type": "boolean",
      "title": "VPN",
      "description": "Is this IP suspected of being a VPN connection? This can include data center ranges which can become active VPNs at any time The proxy status will always be true when this value is true",
      "order": 14
    },
    "zip_code": {
      "type": "string",
      "title": "ZIP Code",
      "description": "ZIP or Postal code of the IP Address if available or NA if unknown",
      "order": 5
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)