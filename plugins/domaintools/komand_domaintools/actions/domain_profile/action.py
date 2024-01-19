import insightconnect_plugin_runtime
from .schema import DomainProfileInput, DomainProfileOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class DomainProfile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_profile",
            description=Component.DESCRIPTION,
            input=DomainProfileInput(),
            output=DomainProfileOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.DOMAIN)
        response = util.make_request(self.connection.api.domain_profile, query)
        return self._cleanup_response(response)

    def _cleanup_response(self, response):
        # Workaround for integer fields that return NULL/empty values
        # As integer fields, this fails the validation test
        history = response.get("response", {}).get("history")
        if not history.get("name_server", {}).get("timespan_in_years"):
            history.get("name_server", {})["timespan_in_years"] = 0

        if not history.get("ip_address", {}).get("timespan_in_years"):
            history.get("ip_address", {})["timespan_in_years"] = 0

        response.get("response", {})["history"] = history
        return response
