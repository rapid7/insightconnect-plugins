import komand
from .schema import ReputationInput, ReputationOutput
# Custom imports below
from komand_domaintools.util import util


class Reputation(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='reputation',
                description='Retrieves reputation score of specified domain name',
                input=ReputationInput(),
                output=ReputationOutput())

    def run(self, params={}):
        query = params.get('domain')
        include_reasons = params.get('include_reasons')
        response = utils.make_request(self.connection.api.reputation, query, include_reasons)
        return response

    def test(self):
        """TODO: Test action"""
        return {}
