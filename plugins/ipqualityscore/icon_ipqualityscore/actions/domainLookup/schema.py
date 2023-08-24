# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Domain Reputation"


class Input:
    FAST = "fast"
    STRICTNESS = "strictness"
    URL = "url"


class Output:
    ADULT = "adult"
    CATEGORY = "category"
    DNS_VALID = "dns_valid"
    DOMAIN = "domain"
    DOMAIN_AGE = "domain_age"
    DOMAIN_RANK = "domain_rank"
    IP_ADDRESS = "ip_address"
    MALWARE = "malware"
    PARKING = "parking"
    PHISHING = "phishing"
    RISK_SCORE = "risk_score"
    SERVER = "server"
    SPAMMING = "spamming"
    SUSPICIOUS = "suspicious"
    UNSAFE = "unsafe"


class DomainLookupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fast": {
      "type": "boolean",
      "title": "Fast",
      "description": "When enabled, the API will provide quicker response times using lighter checks and analysis This setting defaults to False",
      "default": false,
      "order": 3
    },
    "strictness": {
      "type": "integer",
      "title": "Strictness",
      "description": "How strict should we scan this Domain? Stricter checks may provide a higher false-positive rate We recommend defaulting to level 0, the lowest strictness setting, and increasing to 1 or 2 depending on your levels of abuse",
      "default": 0,
      "enum": [
        0,
        1,
        2
      ],
      "order": 2
    },
    "url": {
      "type": "string",
      "title": "Domain",
      "description": "Domain",
      "order": 1
    }
  },
  "required": [
    "strictness",
    "url"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainLookupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "adult": {
      "type": "boolean",
      "title": "Adult",
      "description": "Is this URL or domain hosting dating or adult content?",
      "order": 12
    },
    "category": {
      "type": "string",
      "title": "Category",
      "description": "Website classification and category related to the content and industry of the site Over 70 categories are available including Video Streaming, Trackers, Gaming, Privacy, Advertising, Hacking, Malicious, Phishing, etc The value will be NA if unknown",
      "order": 14
    },
    "dns_valid": {
      "type": "boolean",
      "title": "DNS Valid",
      "description": "The domain has valid DNS records?",
      "order": 6
    },
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain name of the final destination URL of the scanned link, after following all redirects",
      "order": 2
    },
    "domain_age": {
      "type": "object",
      "title": "Domain Age",
      "description": "A human description of when this domain was registered",
      "order": 15
    },
    "domain_rank": {
      "type": "integer",
      "title": "Domain Rank",
      "description": "Estimated popularity rank of website globally Value is 0 if the domain is unranked or has low traffic",
      "order": 5
    },
    "ip_address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address For example nginx1 Value will be NA if unavailable",
      "order": 3
    },
    "malware": {
      "type": "boolean",
      "title": "Malware",
      "description": "Is this domain associated with malware or viruses?",
      "order": 9
    },
    "parking": {
      "type": "boolean",
      "title": "Parking",
      "description": "Is the domain currently parked with a for sale notice?",
      "order": 7
    },
    "phishing": {
      "type": "boolean",
      "title": "Phishing",
      "description": "Is this domain associated with malicious phishing behavior?",
      "order": 10
    },
    "risk_score": {
      "type": "integer",
      "title": "Risk Score",
      "description": "The IPQS risk score which estimates the confidence level for malicious URL detection Risk Scores 85+ are high risk, while Risk Scores = 100 are confirmed as accurate",
      "order": 13
    },
    "server": {
      "type": "string",
      "title": "Server",
      "description": "The server banner of the domain's IP address For example  nginx Value will be NA if unavailable",
      "order": 4
    },
    "spamming": {
      "type": "boolean",
      "title": "Spamming",
      "description": "Is the domain  associated with email SPAM or abusive email addresses?",
      "order": 8
    },
    "suspicious": {
      "type": "boolean",
      "title": "Suspicious",
      "description": "Is this URL suspected of being malicious or used for phishing or abuse? Use in conjunction with the risk_score as a confidence level",
      "order": 11
    },
    "unsafe": {
      "type": "boolean",
      "title": "Unsafe",
      "description": "Is this domain suspected of being unsafe due to phishing, malware, spamming, or abusive behavior? View the confidence level by analyzing the risk_score",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
