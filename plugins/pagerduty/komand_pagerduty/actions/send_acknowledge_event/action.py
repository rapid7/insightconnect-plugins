import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SendAcknowledgeEventInput, SendAcknowledgeEventOutput

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

        email = params.get("email")
        incident_id = params.get("incident_id")

        if email is None or incident_id is None:
            self.logger.warning("Please ensure a valid 'email' and 'incident_id' is provided")
            raise PluginException(
                cause="Missing required paramaters",
                assistance="Please ensure a valid 'email' and 'incident_id' is provided",
            )

        response = self.connection.api.acknowledge_event(
            email=email,
            incident_id=incident_id,
        )

        return response
