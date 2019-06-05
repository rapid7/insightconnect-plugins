import komand
from .. import demo_test
from .schema import LookupDomainInput, LookupDomainOutput


class LookupDomain(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_domain',
                description='This action is used to return information about a specific domain entry',
                input=LookupDomainInput(),
                output=LookupDomainOutput())

    def run(self, params={}):
        try:
            domain = params.get("domain")
            domain_report = self.connection.client.lookup_domain(domain)
            return domain_report
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        return demo_test.demo_test(self.connection.token, self.logger)
