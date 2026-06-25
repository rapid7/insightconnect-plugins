import insightconnect_plugin_runtime
from .schema import SearchThreatActorsInput, SearchThreatActorsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from komand_rapid7_intelhub.util.api import IntelHubAPI


class SearchThreatActors(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_threat_actors",
            description=Component.DESCRIPTION,
            input=SearchThreatActorsInput(),
            output=SearchThreatActorsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        search = params.get(Input.SEARCH, "")
        page = params.get(Input.PAGE, 1)
        page_size = params.get(Input.PAGE_SIZE, 10)
        # END INPUT BINDING - DO NOT REMOVE

        api = IntelHubAPI(self.connection, self.logger)

        try:
            response = api.search_threat_actors(
                search=search,
                page=page,
                page_size=page_size,
            )

            threat_actors = response.get("data", [])
            pagination = {
                "page": response.get("page", page),
                "page_size": response.get("page_size", page_size),
                "total_count": response.get("total_count", 0),
                "total_pages": (response.get("total_count", 0) + page_size - 1) // page_size if page_size > 0 else 0,
            }

            return {
                Output.THREAT_ACTORS: threat_actors,
                Output.PAGINATION: pagination,
            }

        except Exception as e:
            raise PluginException(
                cause="Failed to search threat actors.",
                assistance=f"Error: {str(e)}",
            )
