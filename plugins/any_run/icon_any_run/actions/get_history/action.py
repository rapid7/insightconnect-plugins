import insightconnect_plugin_runtime
from .schema import GetHistoryInput, GetHistoryOutput, Input, Output, Component

# Custom imports below


class GetHistory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_history",
            description=Component.DESCRIPTION,
            input=GetHistoryInput(),
            output=GetHistoryOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        team = params.get(Input.TEAM, False)
        skip = params.get(Input.SKIP, 0)
        limit = params.get(Input.LIMIT, 25)
        # END INPUT BINDING - DO NOT REMOVE

        # Get history from API and return
        history = self.connection.any_run_api.get_history(team, skip, limit)
        return {Output.TASKS: history.get("data", {}).get("tasks", [])}
