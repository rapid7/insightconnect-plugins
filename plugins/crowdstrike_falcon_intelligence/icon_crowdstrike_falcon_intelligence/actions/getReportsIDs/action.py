import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_crowdstrike_falcon_intelligence.util.constants import FilterParameters
from .schema import GetReportsIDsInput, GetReportsIDsOutput, Input, Output, Component

# Custom imports below


class GetReportsIDs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getReportsIDs",
            description=Component.DESCRIPTION,
            input=GetReportsIDsInput(),
            output=GetReportsIDsOutput(),
        )

    def run(self, params: dict = None):
        limit = params.get(Input.LIMIT, FilterParameters.MAX_RESULTS)
        if limit > FilterParameters.MAX_RESULTS:
            raise PluginException(
                cause=f"Limit value is larger than {FilterParameters.MAX_RESULTS}.",
                assistance=f"Please provide `Limit` value less or equal to {FilterParameters.MAX_RESULTS}",
            )
        return {
            Output.REPORTIDS: self.connection.api_client.get_reports_ids(
                offset=params.get(Input.OFFSET), limit=limit, filter_query=params.get(Input.FILTER)
            )
        }
