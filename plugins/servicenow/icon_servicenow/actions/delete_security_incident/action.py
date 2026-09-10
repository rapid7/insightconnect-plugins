import insightconnect_plugin_runtime
from .schema import DeleteSecurityIncidentInput, DeleteSecurityIncidentOutput, Input, Output, Component

# Custom imports below
from icon_servicenow.util.request_helper import RequestHelper
from icon_servicenow.util.validators import validate_record_identifier


class DeleteSecurityIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_security_incident",
            description=Component.DESCRIPTION,
            input=DeleteSecurityIncidentInput(),
            output=DeleteSecurityIncidentOutput(),
        )

    def run(self, params={}):
        sys_id = validate_record_identifier(params.get(Input.SYS_ID), "system ID")
        self.connection.request.make_request(
            endpoint=f"{self.connection.security_incident_url}/{sys_id}", method="DELETE"
        )
        return {Output.SUCCESS: True}
