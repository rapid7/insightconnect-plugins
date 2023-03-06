import insightconnect_plugin_runtime
from .schema import FetchFileByAgentIdInput, FetchFileByAgentIdOutput, Input, Output, Component

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
        agent_id = params.get(Input.AGENT_ID, None)
        password = params.get(Input.PASSWORD)
        file_path = params.get(Input.FILE_PATH)

        if len(password) <= 10 or " " in password:
            raise PluginException(
                cause="Invalid password.",
                assistance="Password must have more than 10 characters and cannot contain whitespace.",
            )

        response = self.connection.fetch_file_by_agent_id(agent_id, file_path, password)

        return {Output.SUCCESS: response}
