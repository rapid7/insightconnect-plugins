import insightconnect_plugin_runtime
from .schema import GetSecurityIncidentInput, GetSecurityIncidentOutput, Input, Output, Component

# Custom imports below
from icon_servicenow.util.security_incident_helper import convert_security_incident_fields
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
        return {
            Output.SECURITY_INCIDENT: convert_security_incident_fields(
                return_non_empty(
                    self.connection.request.make_request(
                        endpoint=f"{self.connection.security_incident_url}/{params.get(Input.SYS_ID)}", method="GET"
                    )
                    .get("resource", {})
                    .get("result", {})
                )
            )
        }
