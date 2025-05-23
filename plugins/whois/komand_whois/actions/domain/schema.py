# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to retrieve data about a domain name"


class Input:
    DOMAIN = "domain"


class Output:
    CREATION_DATE = "creation_date"
    DNSSEC = "dnssec"
    DOMAIN_STATUS = "domain_status"
    EXPIRATION_DATE = "expiration_date"
    LAST_UPDATED = "last_updated"
    NAME = "name"
    NAME_SERVERS = "name_servers"
    REGISTRANT_CC = "registrant_cc"
    REGISTRANT_NAME = "registrant_name"
    REGISTRAR = "registrar"
    REGISTRAR_ABUSE_CONTACT_EMAIL = "registrar_abuse_contact_email"
    REGISTRAR_ABUSE_CONTACT_PHONE = "registrar_abuse_contact_phone"
    REGISTRAR_IANA_ID = "registrar_iana_id"
    REGISTRAR_URL = "registrar_url"
    REGISTRAR_WHOIS_SERVER = "registrar_whois_server"
    REGISTRY_DOMAIN_ID = "registry_domain_id"


class DomainInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain name to lookup",
      "order": 1
    }
  },
  "required": [
    "domain"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "creation_date": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Creation Date",
      "description": "Creation date",
      "order": 5
    },
    "dnssec": {
      "type": "string",
      "title": "DNSSEC",
      "description": "DNSSEC",
      "order": 16
    },
    "domain_status": {
      "type": "array",
      "title": "Domain Status",
      "description": "Domain status",
      "items": {
        "type": "string"
      },
      "order": 15
    },
    "expiration_date": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Expiration Date",
      "description": "Expiration date",
      "order": 6
    },
    "last_updated": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Last Updated Date",
      "description": "Last updated date",
      "order": 7
    },
    "name": {
      "type": "string",
      "title": "Domain Name",
      "description": "Domain name",
      "order": 1
    },
    "name_servers": {
      "type": "array",
      "title": "Nameservers",
      "description": "Nameservers",
      "items": {
        "type": "string"
      },
      "order": 8
    },
    "registrant_cc": {
      "type": "string",
      "title": "Registrant Country",
      "description": "Registrant country",
      "order": 4
    },
    "registrant_name": {
      "type": "string",
      "title": "Registrant Name",
      "description": "Registrant name",
      "order": 3
    },
    "registrar": {
      "type": "string",
      "title": "Domain Registrar",
      "description": "Domain registrar",
      "order": 2
    },
    "registrar_abuse_contact_email": {
      "type": "string",
      "title": "Registrar Abuse Contact Email",
      "description": "Registrar abuse contact email",
      "order": 13
    },
    "registrar_abuse_contact_phone": {
      "type": "string",
      "title": "Registrar Abuse Contact Phone",
      "description": "Registrar abuse Contact phone",
      "order": 14
    },
    "registrar_iana_id": {
      "type": "string",
      "title": "Registrar IANA ID",
      "description": "Registrar IANA ID",
      "order": 12
    },
    "registrar_url": {
      "type": "string",
      "title": "Registrar URL",
      "description": "Registrar URL",
      "order": 11
    },
    "registrar_whois_server": {
      "type": "string",
      "title": "Registrar WHOIS Server",
      "description": "Registrar WHOIS server",
      "order": 10
    },
    "registry_domain_id": {
      "type": "string",
      "title": "Registry Domain ID",
      "description": "Registry domain ID",
      "order": 9
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
