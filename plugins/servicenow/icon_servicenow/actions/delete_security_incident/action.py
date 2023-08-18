import insightconnect_plugin_runtime
from .schema import DeleteSecurityIncidentInput, DeleteSecurityIncidentOutput, Input, Output, Component

# Custom imports below
from icon_servicenow.util.request_helper import RequestHelper


class DeleteSecurityIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_security_incident",
            description=Component.DESCRIPTION,
            input=DeleteSecurityIncidentInput(),
            output=DeleteSecurityIncidentOutput(),
        )

    def run(self, params={}):
        self.connection.request.make_request(
            endpoint=f"{self.connection.security_incident_url}/{params.get(Input.SYS_ID)}", method="DELETE"
        )
        return {Output.SUCCESS: True}
