import komand
from .schema import ConnectionSchema
# Custom imports below
import sys
import threatconnect


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.threat_connect = None

    def connect(self, params):
        self.logger.info("Connect: Connecting..")

        try:
            api_access_id = int(params.get('api_access_id'))
            api_default_org = params.get('api_default_org')
            api_secret_key = params.get('api_secret_key').get("secretKey")
            api_base_url = params.get('api_base_url')
        except Exception:
            self.logger.info("Connect: Connection Failed")
            sys.exit(1)

        self.threat_connect = threatconnect.ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)
        self.threat_connect.set_tcl_console_level('debug')

