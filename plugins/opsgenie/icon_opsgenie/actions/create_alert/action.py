import insightconnect_plugin_runtime
from .schema import CreateAlertInput, CreateAlertOutput, Input, Output, Component


class CreateAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_alert", description=Component.DESCRIPTION, input=CreateAlertInput(), output=CreateAlertOutput()
        )

    def run(self, params={}):
        data = {
            "message": params.get(Input.MESSAGE),
            "alias": params.get(Input.ALIAS),
            "description": params.get(Input.DESCRIPTION),
            "responders": params.get(Input.RESPONDERS),
            "visibleTo": params.get(Input.VISIBLETO),
            "actions": params.get(Input.ACTIONS),
            "tags": params.get(Input.TAGS),
            "details": params.get(Input.DETAILS),
            "entity": params.get(Input.ENTITY),
            "source": params.get(Input.SOURCE),
            "priority": params.get(Input.PRIORITY),
            "user": params.get(Input.USER),
            "note": params.get(Input.NOTE),
        }

        response = self.connection.client.create_alert(data)

        return {
            Output.RESULT: response.get("result"),
            Output.REQUESTID: response.get("requestId"),
            Output.ELAPSED_TIME: response.get("took"),
        }
