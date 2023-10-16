import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SendResolveEventInput, SendResolveEventOutput, Input, Output, Component

# Custom imports below


class SendResolveEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_resolve_event",
            description="Resolve an incident",
            input=SendResolveEventInput(),
            output=SendResolveEventOutput(),
        )

    def run(self, params={}):

        email = params.get(Input.EMAIL)
        incident_id = params.get(Input.INCIDENT_ID)

        response = self.connection.api.resolve_event(
            email=email,
            incident_id=incident_id,
        )

        return {Output.INCIDENT: response.get("incident")}
