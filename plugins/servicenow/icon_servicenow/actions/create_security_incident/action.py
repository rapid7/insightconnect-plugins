import insightconnect_plugin_runtime
from .schema import CreateSecurityIncidentInput, CreateSecurityIncidentOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import return_non_empty
from icon_servicenow.util.security_incident_helper import remove_integer_fields_with_zero


class CreateSecurityIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_security_incident",
            description=Component.DESCRIPTION,
            input=CreateSecurityIncidentInput(),
            output=CreateSecurityIncidentOutput(),
        )

    def run(self, params={}):
        json_data = remove_integer_fields_with_zero(params.copy())
        assigned_to = params.get(Input.ASSIGNED_TO)
        if assigned_to and not params.get(Input.ASSIGNMENT_GROUP):
            raise PluginException(
                cause=f"An attempt was made to assign the user {assigned_to} responsible for this incident, but the "
                f"assignment group was not provided.",
                assistance="To assign a user responsible for a given incident, the assignment group must also be "
                "provided.",
            )
        json_data.update(json_data.pop(Input.ADDITIONAL_FIELDS, {}))
        response = self.connection.request.make_request(
            endpoint=self.connection.security_incident_url,
            method="POST",
            payload=return_non_empty(json_data),
            params={"sysparm_fields": "sys_id,number"},
        )

        try:
            result = response.get("resource", {}).get("result", {})
        except AttributeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response)
        return {Output.SYSTEM_ID: result.get("sys_id"), Output.NUMBER: result.get("number")}
