import insightconnect_plugin_runtime
from .schema import DeleteIncidentInput, DeleteIncidentOutput, Input, Output, Component

# Custom imports below


class DeleteIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_incident",
            description=Component.DESCRIPTION,
            input=DeleteIncidentInput(),
            output=DeleteIncidentOutput(),
        )

    def run(self, params={}):
        incident_id = params.get("incident_id")

        try:
            self.connection.api.delete_incident(incident_id)
            success = True
        except Exception as e:
            self.logger.error("Incident deletion failed: {}".format(e))
            success = False

        return {"success": success}

    def test(self):
        return {"success": True}
