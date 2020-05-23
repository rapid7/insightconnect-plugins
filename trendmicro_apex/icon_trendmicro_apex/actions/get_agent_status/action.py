import komand
from .schema import GetAgentStatusInput, GetAgentStatusOutput, Input, Output, Component
# Custom imports below
from ...util import util


class GetAgentStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent_status',
                description=Component.DESCRIPTION,
                input=GetAgentStatusInput(),
                output=GetAgentStatusOutput())

    def run(self, params={}):
        agents = self.connection.api.execute(
            "put",
            "/WebApp/OSCE_iES/OsceIes/ApiEntry",
            {
                "Payload": {
                    "pagination": {"offset": 0, "limit": 50}
                },
                "filter": [{"type": 1, "value": params.get(Input.AGENT_GUID)}],
                "TaskType": util.TaskType.value_of(util.DEFAULT_TASK_TYPE),
                "Url": "V1/Task/ShowAgentList"
            }
        )

        if not agents:
            return {}

        content = agents.get("Data", {}).get("Data", {}).get("content", [])
        if len(content) > 0 and len(content[0].get("content", {}).get("agentEntity", [])) > 0:
            return {
                Output.AGENTENTITY: content[0].get("content").get("agentEntity")[0],
                Output.AGENTQUERYSTATUS: content[0].get("content").get("agentQueryStatus")
            }

        return {}
