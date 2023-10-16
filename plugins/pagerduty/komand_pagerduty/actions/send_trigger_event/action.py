import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SendTriggerEventInput, SendTriggerEventOutput, Input, Output, Component

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

        # required
        email = params.get(Input.EMAIL)
        title = params.get(Input.TITLE)
        service = params.get(Input.SERVICE, {})

        # optional

        escalation_policy = params.get(Input.ESCALATION_POLICY, {})
        assignments = params.get(Input.ASSIGNMENTS, [])

        dict_of_optional_fields = {
            "urgency": params.get(Input.URGENCY, ""),
            "incident_key": params.get(Input.INCIDENT_KEY, ""),
            "priority": params.get(Input.PRIORITY, {}),
            "escalation_policy": escalation_policy,
            "conference_bridge": params.get(Input.CONFERENCE_BRIDGE, {}),
            "body": params.get(Input.BODY, {}),
            "assignments": assignments,
        }

        if escalation_policy and assignments:
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

        return {Output.INCIDENT: response.get("incident")}
