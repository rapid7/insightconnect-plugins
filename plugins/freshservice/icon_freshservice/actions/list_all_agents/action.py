import insightconnect_plugin_runtime
from .schema import ListAllAgentsInput, ListAllAgentsOutput, Input, Output, Component

# Custom imports below
from icon_freshservice.util.helpers import process_list


class ListAllAgents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_all_agents",
            description=Component.DESCRIPTION,
            input=ListAllAgentsInput(),
            output=ListAllAgentsOutput(),
        )

    def run(self, params={}):
        email = params.get(Input.EMAIL)
        mobile_phone_number = params.get(Input.MOBILEPHONENUMBER)
        work_phone_number = params.get(Input.WORKPHONENUMBER)
        active = params.get(Input.ACTIVE)
        state = params.get(Input.STATE)
        parameters = {
            "email": email if email else None,
            "mobile_phone_number": mobile_phone_number if mobile_phone_number else None,
            "work_phone_number": work_phone_number if work_phone_number else None,
            "active": active if active != "all" else None,
            "state": state if state != "all" else None,
        }
        return {Output.AGENTS: process_list(self.connection.api.list_all_agents(parameters).get("agents", []))}
