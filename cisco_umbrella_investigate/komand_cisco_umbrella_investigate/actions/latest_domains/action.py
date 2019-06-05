import komand
from .schema import LatestDomainsInput, LatestDomainsOutput
# Custom imports below
from IPy import IP as IP_Validate


class LatestDomains(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='latest_domains',
                description='Return associated malicious domains for an IP address',
                input=LatestDomainsInput(),
                output=LatestDomainsOutput())

    def run(self, params={}):
        IP = params.get('IP')
        try:
            IP_Validate(IP)
        except Exception as e:
            self.logger.error("LatestDomains: Run: Wrong IP format")
            raise e

        try:
            latest_domains = self.connection.investigate.latest_domains(IP)
        except Exception as e:
            self.logger.error("LatestDomains: Run: Problem with request")
            raise e
        return {"domains": latest_domains}

    def test(self):
        return {"domains": []}
