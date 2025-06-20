import insightconnect_plugin_runtime
from .schema import LookupHashInput, LookupHashOutput, Input, Output

# Custom imports below
from copy import copy
from insightconnect_plugin_runtime.exceptions import PluginException


class LookupHash(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_hash",
            description="Lookup a file hash",
            input=LookupHashInput(),
            output=LookupHashOutput(),
        )

    def run(self, params={}):
        self.request = copy(self.connection.api.request)
        self.request.url, self.request.method = self.request.url + "/v2/intelligence", "GET"

        # Pagination flag and results placeholder
        self.continue_paging, self.results = True, []
        # Update the request with the supplied IP address, page size, and offset
        self.request.params.update({"md5": params.get(Input.HASH), "limit": 1000, "offset": 0})

        while self.continue_paging:
            response_data = self.connection.api.send(self.request)

            try:
                # Check pagination indicator. A "null" value means no more pages.
                if not response_data.get("meta", {}).get("next"):
                    self.continue_paging = False
            except KeyError:
                raise PluginException(
                    cause="The output did not contain expected keys.",
                    assistance="Contact support for help.",
                    data=response_data,
                )

            self.request.params["offset"] += 1000
            self.results.extend(response_data.get("objects"))

        self.results = insightconnect_plugin_runtime.helper.clean(self.results)

        return {Output.RESULTS: self.results}
