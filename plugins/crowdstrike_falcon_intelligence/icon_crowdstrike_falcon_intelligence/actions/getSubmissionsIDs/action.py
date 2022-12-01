import insightconnect_plugin_runtime
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
        limit = params.get(Input.LIMIT, 5000)
        if limit > 5000:
            self.logger.warning(
                "Provided limit value is larger than 5000 but this action will return up to 5000 results."
            )
        return {
            Output.SUBMISSIONIDS: self.connection.api_client.get_submissions_ids(
                offset=params.get(Input.OFFSET), limit=limit, filter_query=params.get(Input.FILTER)
            )
        }
