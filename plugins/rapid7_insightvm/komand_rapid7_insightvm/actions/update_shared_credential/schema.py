# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update shared credentials"


class Input:
    ACCOUNT = "account"
    DESCRIPTION = "description"
    HOST_RESTRICTION = "host_restriction"
    ID = "id"
    NAME = "name"
    PORT_RESTRICTION = "port_restriction"
    SITE_ASSIGNMENT = "site_assignment"
    SITES = "sites"


class Output:
    LINKS = "links"


class UpdateSharedCredentialInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account": {
      "$ref": "#/definitions/account",
      "title": "Account",
      "description": "Specify the type of service to authenticate as well as all of the information required by that service",
      "order": 1
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "The description of the credential",
      "order": 2
    },
    "host_restriction": {
      "type": "string",
      "title": "Host Restriction",
      "description": "The host name or IP address that you want to restrict the credentials to",
      "order": 3
    },
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "The identifier of the credential",
      "order": 4
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "The name of the credential",
      "order": 5
    },
    "port_restriction": {
      "type": "string",
      "title": "Port Restriction",
      "description": "Further restricts the credential to attempt to authenticate on a specific port. The port can only be restricted if the property hostRestriction is specified",
      "order": 6
    },
    "site_assignment": {
      "type": "string",
      "title": "Site Assignment",
      "description": "Assigns the shared scan credential either to be available to all sites or to a specific list of sites. All sites - The shared scan credential is assigned to all current and future sites. specific-sites - The shared scan credential is assigned to zero sites by default. Administrators must explicitly assign sites to the shared credential. Shared scan credentials assigned to a site can disabled within the site configuration, if needed",
      "enum": [
        "all-sites",
        "specific-sites"
      ],
      "order": 7
    },
    "sites": {
      "type": "array",
      "title": "Sites",
      "description": "List of site identifiers. These sites are explicitly assigned access to the shared scan credential, allowing the site to use the credential for authentication during a scan. This property can only be set if the value of property siteAssignment is set to \"specific-sites\". When the property siteAssignment is set to \"all-sites\", this property will be null",
      "items": {
        "type": "integer"
      },
      "order": 8
    }
  },
  "required": [
    "account",
    "name",
    "site_assignment"
  ],
  "definitions": {
    "account": {
      "type": "object",
      "title": "account",
      "properties": {
        "authentication_type": {
          "type": "string",
          "title": "Authentication Type",
          "description": "The authentication protocols available to use in SNMP v3",
          "default": "no-authentication",
          "enum": [
            "no-authentication",
            "md5",
            "sha"
          ],
          "order": 1
        },
        "community_name": {
          "type": "string",
          "title": "Community Name",
          "description": "The community name that will be used for authenticating",
          "order": 2
        },
        "database": {
          "type": "string",
          "title": "Database",
          "description": "The name of the database. If not specified, a default database name will be used during authentication",
          "order": 3
        },
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "The address of the domain. This property cannot be specified unless property useWindowsAuthentication is set to true",
          "order": 4
        },
        "enumerate_sids": {
          "type": "string",
          "title": "Enumerate SIDs",
          "description": "Boolean flag instructing the scan engine to attempt to enumerate SIDs from your environment. If set to true, set the Oracle Net Listener password in property oracleListenerPassword",
          "order": 5
        },
        "notes_id_password": {
          "type": "string",
          "title": "Notes ID Password",
          "description": "The password for the account that will be used for authenticating",
          "order": 6
        },
        "ntlm_hash": {
          "type": "string",
          "title": "NTLM Hash",
          "description": "The NTLM password hash",
          "order": 7
        },
        "oracle_listener_password": {
          "type": "string",
          "title": "Oracle Listener Password",
          "description": "The Oracle Net Listener password. Used to enumerate SIDs from your environment",
          "order": 8
        },
        "password": {
          "type": "string",
          "title": "Password",
          "description": "The password for the account that will be used for authenticating",
          "order": 9
        },
        "pem_key": {
          "type": "string",
          "title": "PEM Key",
          "description": "The PEM-format private key",
          "order": 10
        },
        "permission_elevation": {
          "type": "string",
          "title": "Permission Evaluation",
          "description": "Elevate scan engine permissions to administrative or root access, which is necessary to obtain certain data during the scan. Defaults to \"none\" if not specified",
          "default": "none",
          "enum": [
            "none",
            "sudo",
            "sudosu",
            "su",
            "pbrun",
            "privileged-exec"
          ],
          "order": 11
        },
        "permission_elevation_password": {
          "type": "string",
          "title": "Permission Elevation Password",
          "description": "The password for the account with elevated permissions. This property must not be specified when the property permissionElevation is set to either \"none\" or \"pbrun\"; otherwise the property is required",
          "order": 12
        },
        "permission_elevation_username": {
          "type": "string",
          "title": "Permission Elevation Username",
          "description": "The user name for the account with elevated permissions. This property must not be specified when the property permissionElevation is set to either \"none\" or \"pbrun\"; otherwise the property is required.",
          "order": 13
        },
        "privacy_password": {
          "type": "string",
          "title": "Privacy Password",
          "description": "The privacy password for the account that will be used for authenticating. Is required when the property authenticationType is set to valid value other than \"no-authentication\" and when the privacyType is set to a valid value other than code>\"no-privacy\"",
          "order": 14
        },
        "privacy_type": {
          "type": "string",
          "title": "Privacy Type",
          "description": "The privacy protocols available to use in SNMP v3",
          "default": "no-privacy",
          "enum": [
            "no-privacy",
            "des",
            "aes-128",
            "aes-192",
            "aes-192-with-3-des-key-extension",
            "aes-256",
            "aes-265-with-3-des-key-extension"
          ],
          "order": 15
        },
        "private_key_password": {
          "type": "string",
          "title": "Private Pey Password",
          "description": "The password for private key",
          "order": 16
        },
        "realm": {
          "type": "string",
          "title": "Realm",
          "description": "The realm",
          "order": 17
        },
        "service": {
          "type": "string",
          "title": "Service",
          "description": "Specify the type of service to authenticate",
          "enum": [
            "as400",
            "cifs",
            "cifshash",
            "cvs",
            "db2",
            "ftp",
            "http",
            "ms-sql",
            "mysql",
            "notes",
            "oracle",
            "pop",
            "postgresql",
            "remote-exec",
            "snmp",
            "snmpv3",
            "ssh",
            "ssh-key",
            "sybase",
            "telnet"
          ],
          "order": 18
        },
        "sid": {
          "type": "string",
          "title": "SID",
          "description": "The name of the database. If not specified, a default database name will be used during authentication",
          "order": 19
        },
        "use_windows_authentication": {
          "type": "boolean",
          "title": "Use Windows Authentication",
          "description": "Boolean flag signaling whether to connect to the database using Windows authentication. When set to true, Windows authentication is attempted; when set to false, SQL authentication is attempted",
          "order": 20
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The user name for the account that will be used for authenticating",
          "order": 21
        }
      },
      "required": [
        "service"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateSharedCredentialOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "links": {
      "type": "array",
      "title": "Links",
      "description": "Hypermedia links to corresponding or related resources",
      "items": {
        "$ref": "#/definitions/link"
      },
      "order": 1
    }
  },
  "required": [
    "links"
  ],
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
