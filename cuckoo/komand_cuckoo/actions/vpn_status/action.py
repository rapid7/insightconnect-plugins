import komand
from .schema import VpnStatusInput, VpnStatusOutput
# Custom imports below
import json
import requests


class VpnStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='vpn_status',
                description='Returns VPN status',
                input=VpnStatusInput(),
                output=VpnStatusOutput())

    def run(self, params={}):
        server = self.connection.server
        endpoint = server + "/vpn/status"

        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            vpn_list = []
            for vpn in response["vpns"]:
                if response["vpns"][vpn] == True:
                    status = "Running"
                else:
                    status = "Not running"

                vpn_list.append({
                        "name": response["vpns"][vpn],
                        "status": status
                    })
            response["vpns"] = vpn_list
            return response

        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['vpns'] = [{'message':'Test passed'}]
        return out
