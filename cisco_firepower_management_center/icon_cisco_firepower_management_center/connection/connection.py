import komand
from .schema import ConnectionSchema, Input
from komand.exceptions import PluginException
# Custom imports below
from cisco_firepower_management_center.util.api import CiscoAsaAPI
import fmcapi


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        username, password = params["username_and_password"]["username"], params["username_and_password"]["password"]
        self.username = username
        self.password = password
        self.host = params.get('server')
        self.cisco_firepower_api = 

    def test(self):
        # TODO: Get log contents to pass to ConnectionTestException
        with fmcapi.FMC(
            host=self.host,
            username=self.username,
            password=self.password,
            autodeploy=True,
            limit=10
        ) as fmc1:
            acp = fmcapi.AccessPolicies(fmc=fmc1)
            policy = acp.get()
            if policy:
                return
            else:
                raise ConnectionTestException(cause='Unable to connect to Cisco Firepower Management Center.',
                                      assistance='Please check the log for more information.')

