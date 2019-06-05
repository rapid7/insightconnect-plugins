import komand
from .schema import AddDomainInput, AddDomainOutput
# Custom imports below
from komand_crits.util import utils


class AddDomain(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_domain',
                description='Creates a new domain',
                input=AddDomainInput(),
                output=AddDomainOutput())

    def run(self, params={}):
        response = self.connection.crits.add_domain(
            domain=params['domain'],
            source=params['source'],
            params=params['params']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
