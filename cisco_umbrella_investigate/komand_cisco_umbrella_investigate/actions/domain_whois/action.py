import komand
from .schema import DomainWhoisInput, DomainWhoisOutput
# Custom imports below


class DomainWhois(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='domain_whois',
                description='A standard WHOIS response record for a single domain with all available WHOIS data returned in an array',
                input=DomainWhoisInput(),
                output=DomainWhoisOutput())

    def run(self, params={}):
        domain = params.get('domain')
        try:
            domain_whois = self.connection.investigate.domain_whois(domain)
        except Exception as e:
            self.logger.error("DomainWhois: Run: Problem with request")
            raise e

        return {"whois": [domain_whois]}

    def test(self):
        return {"whois": []}
