import insightconnect_plugin_runtime
from .schema import LookupUrlInput, LookupUrlOutput

# Custom imports below
from copy import copy
from insightconnect_plugin_runtime.exceptions import PluginException
from json.decoder import JSONDecodeError


class LookupUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_url",
            description="Lookup a URL",
            input=LookupUrlInput(),
            output=LookupUrlOutput(),
        )

    def run(self, params={}):
        # Copy and update the base request to avoid mutating the original
        self.request = copy(self.connection.request)
        self.request.url, self.request.method = self.request.url + "/intelligence", "GET"

        # Pagination flag and results placeholder
        self.continue_paging, self.results = True, list()
        # Update the request with the supplied domain, page size, and offset
        self.request.params.update({"url": "{url}".format(url=params.get("url")), "limit": 1000, "offset": 0})

        while self.continue_paging:
            response_data = self.connection.send(self.request)

            try:
                # Check pagination indicator. A "null" value means no more pages.
                if not response_data["meta"]["next"]:
                    self.continue_paging = False
            except KeyError:
                raise PluginException(
                    cause="The output did not contain expected keys.",
                    assistance="Contact support for help.",
                    data=response_data,
                )

            self.request.params["offset"] += 1000
            self.results.extend(response_data["objects"])

        self.results = insightconnect_plugin_runtime.helper.clean(self.results)
        return {"results": self.results}

    def test(self):
        # TODO: Implement test function
        return {}
