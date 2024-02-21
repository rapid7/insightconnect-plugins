import insightconnect_plugin_runtime
from .schema import ReputationInput, ReputationOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class Reputation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reputation",
            description=Component.DESCRIPTION,
            input=ReputationInput(),
            output=ReputationOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.DOMAIN)
        include_reasons = params.get(Input.INCLUDE_REASONS)
        response = util.make_request(self.connection.api.reputation, query, include_reasons)
        return response
