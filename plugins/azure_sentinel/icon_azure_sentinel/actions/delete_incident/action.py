import insightconnect_plugin_runtime

from .schema import Component, DeleteIncidentInput, DeleteIncidentOutput, Input, Output


class DeleteIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_incident",
            description=Component.DESCRIPTION,
            input=DeleteIncidentInput(),
            output=DeleteIncidentOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)

        status_code = self.connection.api_client.delete_incident(
            incident_id, resource_group_name, workspace_name, subscription_id
        )
        return {Output.STATUS: status_code}
