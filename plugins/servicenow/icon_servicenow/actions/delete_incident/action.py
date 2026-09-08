import insightconnect_plugin_runtime
from .schema import DeleteIncidentInput, DeleteIncidentOutput, Input, Output, Component

# Custom imports below
from icon_servicenow.util.validators import validate_record_identifier


class DeleteIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_incident",
            description=Component.DESCRIPTION,
            input=DeleteIncidentInput(),
            output=DeleteIncidentOutput(),
        )

    def run(self, params={}):
        system_id = validate_record_identifier(params.get(Input.SYSTEM_ID), "system ID")
        url = f"{self.connection.incident_url}/{system_id}"
        method = "delete"

        response = self.connection.request.make_request(url, method)

        if response.get("status", 0) in range(200, 299):
            success = True
        else:
            success = False

        return {Output.SUCCESS: success}
