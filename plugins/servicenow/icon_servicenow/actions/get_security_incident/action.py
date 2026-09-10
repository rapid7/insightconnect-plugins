import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetSecurityIncidentInput, GetSecurityIncidentOutput, Input, Output, Component

# Custom imports below
from icon_servicenow.util.security_incident_helper import convert_security_incident_fields
from icon_servicenow.util.validators import validate_record_identifier
from insightconnect_plugin_runtime.helper import return_non_empty


class GetSecurityIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_security_incident",
            description=Component.DESCRIPTION,
            input=GetSecurityIncidentInput(),
            output=GetSecurityIncidentOutput(),
        )

    def run(self, params={}):
        sys_id = validate_record_identifier(params.get(Input.SYS_ID), "system ID")

        response = self.connection.request.make_request(
            endpoint=f"{self.connection.security_incident_url}/{sys_id}", method="GET"
        )
        try:
            result = response.get("resource", {}).get("result", {})
        except AttributeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        return {Output.SECURITY_INCIDENT: convert_security_incident_fields(return_non_empty(result))}
