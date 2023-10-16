import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SendResolveEventInput, SendResolveEventOutput

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
        """Resolve event"""

        email = params.get("email")
        incident_id = params.get("incident_id")

        if email is None or incident_id is None:
            self.logger.warning("Please ensure a valid 'email' and 'incident_id'is provided")
            raise PluginException(
                cause="Missing required paramaters",
                assistance="Please ensure a valid 'email' and 'incident_id' is provided",
            )

        response = self.connection.api.resolve_event(email=email, incident_id=incident_id)

        return response
