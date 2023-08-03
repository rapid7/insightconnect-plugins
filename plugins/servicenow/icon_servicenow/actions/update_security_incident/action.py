import insightconnect_plugin_runtime
from .schema import UpdateSecurityIncidentInput, UpdateSecurityIncidentOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import return_non_empty
from icon_servicenow.util.security_incident_helper import remove_integer_fields_with_zero


class UpdateSecurityIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_security_incident",
            description=Component.DESCRIPTION,
            input=UpdateSecurityIncidentInput(),
            output=UpdateSecurityIncidentOutput(),
        )

    def run(self, params={}):
        json_data = remove_integer_fields_with_zero(params.copy())
        incident_sys_id = json_data.pop(Input.SYS_ID)
        json_data.update(json_data.pop(Input.ADDITIONAL_FIELDS, {}))
        response = (
            self.connection.request.make_request(
                endpoint=f"{self.connection.security_incident_url}/{incident_sys_id}",
                method="PATCH",
                payload=return_non_empty(json_data),
                params={"sysparm_fields": "sys_id,number"},
            )
            .get("resource", {})
            .get("result", {})
        )
        return {Output.SYSTEM_ID: response.get("sys_id"), Output.NUMBER: response.get("number")}
