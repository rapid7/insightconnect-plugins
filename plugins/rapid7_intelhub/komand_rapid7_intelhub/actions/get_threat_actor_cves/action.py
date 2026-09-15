import insightconnect_plugin_runtime
from .schema import GetThreatActorCvesInput, GetThreatActorCvesOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from komand_rapid7_intelhub.util.api import IntelHubAPI


class GetThreatActorCves(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_threat_actor_cves",
            description=Component.DESCRIPTION,
            input=GetThreatActorCvesInput(),
            output=GetThreatActorCvesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        uuid = params.get(Input.UUID)
        page = params.get(Input.PAGE, 1)
        page_size = params.get(Input.PAGE_SIZE, 10)
        # END INPUT BINDING - DO NOT REMOVE

        api = IntelHubAPI(self.connection, self.logger)

        try:
            response = api.get_threat_actor_cves(
                uuid=uuid,
                page=page,
                page_size=page_size,
            )

            cves = response.get("data", [])
            pagination = {
                "page": response.get("page", page),
                "page_size": response.get("page_size", page_size),
                "total_count": response.get("total_count", 0),
                "total_pages": (response.get("total_count", 0) + page_size - 1) // page_size if page_size > 0 else 0,
            }

            return {
                Output.CVES: cves,
                Output.PAGINATION: pagination,
            }

        except Exception as e:
            raise PluginException(
                cause="Failed to get threat actor CVEs.",
                assistance=f"Error: {str(e)}",
            )
