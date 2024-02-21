import insightconnect_plugin_runtime
from .schema import DomainSearchInput, DomainSearchOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class DomainSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_search",
            description=Component.DESCRIPTION,
            input=DomainSearchInput(),
            output=DomainSearchOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = util.make_request(self.connection.api.domain_search, **params)
        return response
