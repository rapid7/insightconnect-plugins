import komand
from .schema import AgentListInput, AgentListOutput, Input, Component
# Custom imports below
from ...util import util


class AgentList(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='agent_list',
            description=Component.DESCRIPTION,
            input=AgentListInput(),
            output=AgentListOutput())

    def run(self, params={}):
        return self.connection.api.execute(
            "put",
            "/WebApp/OSCE_iES/OsceIes/ApiEntry",
            {
                "Payload": self._get_payload(params),
                "filter": params.get(Input.FILTER),
                "TaskType": util.TaskType.value_of(params.get(Input.TASK_TYPE)),
                "Url": "V1/Task/ShowAgentList"
            }
        )

    @staticmethod
    def _get_payload(params):
        payload = {}
        if params.get(Input.PAGINATION):
            payload["pagination"] = {
                "offset": params.get(Input.PAGINATION).get("offset", 0),
                "limit": params.get(Input.PAGINATION).get("limit", 50)
            }
        else:
            payload["pagination"] = {"offset": 0, "limit": 50}

        return payload
