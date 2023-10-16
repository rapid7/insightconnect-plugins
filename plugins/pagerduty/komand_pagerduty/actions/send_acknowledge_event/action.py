import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SendAcknowledgeEventInput, SendAcknowledgeEventOutput, Input, Output, Component

# Custom imports below


class SendAcknowledgeEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_acknowledge_event",
            description="Acknowledge an incident",
            input=SendAcknowledgeEventInput(),
            output=SendAcknowledgeEventOutput(),
        )

    def run(self, params={}):
        """Send acknowledge"""

        email = params.get(Input.EMAIL)
        incident_id = params.get(Input.INCIDENT_ID)

        response = self.connection.api.acknowledge_event(
            email=email,
            incident_id=incident_id,
        )

        return {Output.INCIDENT: response.get("incident")}
