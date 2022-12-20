import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_crowdstrike_falcon_intelligence.util.constants import FilterParameters
from .schema import GetSubmissionsIDsInput, GetSubmissionsIDsOutput, Input, Output, Component

# Custom imports below


class GetSubmissionsIDs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getSubmissionsIDs",
            description=Component.DESCRIPTION,
            input=GetSubmissionsIDsInput(),
            output=GetSubmissionsIDsOutput(),
        )

    def run(self, params: dict = None):
        limit = params.get(Input.LIMIT, FilterParameters.MAX_RESULTS)
        if limit > FilterParameters.MAX_RESULTS:
            raise PluginException(
                cause=f"Limit value is larger than {FilterParameters.MAX_RESULTS}.",
                assistance=f"Please provide `Limit` value less or equal to {FilterParameters.MAX_RESULTS}",
            )
        return {
            Output.SUBMISSIONIDS: self.connection.api_client.get_submissions_ids(
                offset=params.get(Input.OFFSET), limit=limit, filter_query=params.get(Input.FILTER)
            )
        }
