import insightconnect_plugin_runtime
from .schema import CreateAlertInput, CreateAlertOutput, Input, Output, Component


class CreateAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_alert", description=Component.DESCRIPTION, input=CreateAlertInput(), output=CreateAlertOutput()
        )

    def run(self, params={}):
        data = {
            "message": self.params.get(Input.MESSAGE),
            "alias": self.params.get(Input.ALIAS),
            "description": self.params.get(Input.DESCRIPTION),
            "responders": self.params.get(Input.RESPONDERS),
            "visibleTo": self.params.get(Input.VISIBLETO),
            "actions": self.params.get(Input.ACTIONS),
            "tags": self.params.get(Input.TAGS),
            "details": self.params.get(Input.DETAILS),
            "entity": self.params.get(Input.ENTITY),
            "source": self.params.get(Input.SOURCE),
            "priority": self.params.get(Input.PRIORITY),
            "user": self.params.get(Input.USER),
            "note": self.params.get(Input.NOTE),
        }

        results = self.connection.client.create_alert(data)

        return {
            Output.REQUESTID: results[Output.REQUESTID],
            Output.TOOK: results[Output.TOOK],
            Output.RESULT: results[Output.RESULT],
        }
