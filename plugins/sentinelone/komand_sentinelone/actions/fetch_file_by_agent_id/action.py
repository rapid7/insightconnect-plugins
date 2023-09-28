import insightconnect_plugin_runtime
from .schema import FetchFileByAgentIdInput, FetchFileByAgentIdOutput, Input, Output, Component
from komand_sentinelone.util.helper import check_password_meets_requirements

# Custom imports below


class FetchFileByAgentId(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="fetch_file_by_agent_id",
            description=Component.DESCRIPTION,
            input=FetchFileByAgentIdInput(),
            output=FetchFileByAgentIdOutput(),
        )

    def run(self, params={}):
        password = params.get(Input.PASSWORD)
        check_password_meets_requirements(password)

        return {
            Output.SUCCESS: self.connection.client.fetch_file_by_agent_id(
                params.get(Input.AGENTID), params.get(Input.FILEPATH), password
            )
        }
