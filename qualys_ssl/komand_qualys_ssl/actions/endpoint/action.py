import komand
from .schema import EndpointInput, EndpointOutput
# Custom imports below
import requests


class Endpoint(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='endpoint',
                description='Retrieve detailed endpoint info',
                input=EndpointInput(),
                output=EndpointOutput())

    def run(self, params={}):
        try:
            url = "https://api.ssllabs.com/api/v2/getEndpointData"
            r = requests.get(url,
                             params={"host": params.get("host"), "s": params.get("ip"), "fromCache": "True"}).json()
            if "errors" in r:
                self.logger.error(r["errors"])
                raise Exception(r["errors"])

            return r

        except requests.exceptions.RequestException as e:
            self.logger.error(e)
            raise Exception(e)

    def test(self):
        try:
            url = "https://api.ssllabs.com/api/v2/info"
            r = requests.get(url)
            if r.ok:
                return {"progress": 1,
                        "delegation": 1,
                        "details": {},
                        "ipAddress": "True",
                        "statusMessage": "True",
                        "grade": "True",
                        "gradeTrustIgnored": "True",
                        "isExceptional": True,
                        "hasWarnings": True,
                        "duration": 1,
                        "eta": 1}
        except requests.exceptions.RequestException as e:
            raise Exception(e)

