import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CreateAlertInput, CreateAlertOutput, Input, Output, Component

# Custom imports below


class CreateAlert(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_alert", description=Component.DESCRIPTION, input=CreateAlertInput(), output=CreateAlertOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
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
        # END INPUT BINDING - DO NOT REMOVE
        token = self.connection.api.encode_basic_auth()

        response = self.connection.api.create_alert(
            token=token,
            data=data,
        )

        return {
            Output.RESULT: response.get("result"),
            Output.REQUESTID: response.get("requestId"),
            Output.ELAPSED_TIME: response.get("took"),
            Output.ALERTID: response.get("alertId"),
        }
