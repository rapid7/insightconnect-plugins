import insightconnect_plugin_runtime

from .schema import ReputationInput, ReputationOutput
from ...util.util import make_request


class Reputation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reputation",
            description="Retrieves reputation score of specified domain name",
            input=ReputationInput(),
            output=ReputationOutput(),
        )

    def run(self, params={}):
        query = params.get("domain")
        include_reasons = params.get("include_reasons")
        response = make_request(self.connection.api.reputation, query, include_reasons)
        return response
