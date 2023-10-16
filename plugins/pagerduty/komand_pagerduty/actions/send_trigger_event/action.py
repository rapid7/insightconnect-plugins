import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SendTriggerEventInput, SendTriggerEventOutput

# Custom import below


class SendTriggerEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_trigger_event",
            description="Trigger an incident",
            input=SendTriggerEventInput(),
            output=SendTriggerEventOutput(),
        )

    def run(self, params={}):
        """Trigger event"""

        # required
        email = params.get("email")
        title = params.get("title")
        service = params.get("service", {})

        # optional
        dict_of_optional_fields = {
            "urgency": params.get("urgency", ""),
            "incident_key": params.get("incident_key", ""),
            "priority": params.get("priority", {}),
            "escalation_policy": params.get("escalation_policy", {}),
            "conference_bridge": params.get("conference_bridge", {}),
            "body": params.get("body", {}),
            "assignments": params.get("assignments", []),
        }

        if email is None or title is None or service is None:
            self.logger.warning("Please ensure a valid 'email', 'tile' and 'service' is provided")
            raise PluginException(
                cause="Missing required paramaters",
                assistance="Please ensure a valid 'email' and 'incident_id' is provided",
            )

        if params.get("escalation_policy", {}) and params.get("assignments", []):
            self.logger.warning(
                "Invalid input only one of 'escalation_policy' or 'assignments' can be used at one time"
            )
            raise PluginException(
                cause="Invalid paramaters",
                assistance="Invalid input only one of 'escalation_policy' or 'assignments' can be used at one time",
            )

        response = self.connection.api.trigger_event(
            email=email, title=title, service=service, dict_of_optional_fields=dict_of_optional_fields
        )

        return response
