import insightconnect_plugin_runtime
from .schema import GetHistoryInput, GetHistoryOutput, Input, Output, Component
# Custom imports below


class GetHistory(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_history',
                description=Component.DESCRIPTION,
                input=GetHistoryInput(),
                output=GetHistoryOutput())

    def run(self, params={}):
        history = self.connection.any_run_api.get_history(
            params.get(Input.TEAM, False),
            params.get(Input.SKIP, 0),
            params.get(Input.LIMIT, 25)
        )
        return {
            Output.TASKS: history.get("data", {}).get('tasks', [])
        }
