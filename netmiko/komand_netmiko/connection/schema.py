# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CREDENTIALS = "credentials"
    DEVICE_TYPE = "device_type"
    HOST = "host"
    KEY = "key"
    PORT = "port"
    SECRET = "secret"
    VERBOSE = "verbose"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "Username and password to run commands as",
      "order": 2
    },
    "device_type": {
      "type": "string",
      "title": "Device Type",
      "description": "The type of device to connect",
      "enum": [
        "a10",
        "accedian",
        "alcatel_aos",
        "alcatel_sros",
        "arista_eos",
        "aruba_os",
        "avaya_ers",
        "avaya_vsp",
        "brocade_fastiron",
        "brocade_netiron",
        "brocade_nos",
        "brocade_vdx",
        "brocade_vyos",
        "checkpoint_gaia",
        "calix_b6",
        "ciena_saos",
        "cisco_asa",
        "cisco_ios",
        "cisco_nxos",
        "cisco_s300",
        "cisco_tp",
        "cisco_wlc",
        "cisco_xe",
        "cisco_xr",
        "coriant",
        "dell_force10",
        "dell_powerconnect",
        "eltex",
        "enterasys",
        "extreme",
        "extreme_wing",
        "f5_ltm",
        "fortinet",
        "generic_termserver",
        "hp_comware",
        "hp_procurve",
        "huawei",
        "juniper",
        "juniper_junos",
        "linux",
        "mellanox",
        "mrv_optiswitch",
        "netapp_cdot",
        "ovs_linux",
        "paloalto_panos",
        "pluribus",
        "quanta_mesh",
        "ruckus_fastiron",
        "ubiquiti_edge",
        "ubiquiti_edgeswitch",
        "vyatta_vyos",
        "vyos"
      ],
      "order": 1
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Remote Host",
      "order": 5
    },
    "key": {
      "$ref": "#/definitions/credential_asymmetric_key",
      "title": "Key",
      "description": "A base64 encoded SSH private key to use to authenticate to network device",
      "order": 4
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Remote port",
      "default": 22,
      "order": 6
    },
    "secret": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Secret",
      "description": "API seret key",
      "order": 3
    },
    "verbose": {
      "type": "boolean",
      "title": "Verbose",
      "description": "Additional messages to standard output",
      "default": false,
      "order": 7
    }
  },
  "required": [
    "credentials",
    "device_type",
    "host",
    "port",
    "verbose"
  ],
  "definitions": {
    "credential_asymmetric_key": {
      "id": "credential_asymmetric_key",
      "type": "object",
      "title": "Credential: Asymmetric Key",
      "description": "A shared key",
      "properties": {
        "privateKey": {
          "type": "string",
          "title": "Private Key",
          "displayType": "password",
          "description": "The private key",
          "format": "password"
        }
      },
      "required": [
        "privateKey"
      ]
    },
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    },
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password",
          "order": 2
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with",
          "order": 1
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
