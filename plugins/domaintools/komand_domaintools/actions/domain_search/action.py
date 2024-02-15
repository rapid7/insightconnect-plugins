import insightconnect_plugin_runtime

from .schema import DomainSearchInput, DomainSearchOutput
from ...util.util import make_request


class DomainSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_search",
            description="Searches for domain names that match your specific search string",
            input=DomainSearchInput(),
            output=DomainSearchOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = make_request(self.connection.api.domain_search, **params)
        return response
