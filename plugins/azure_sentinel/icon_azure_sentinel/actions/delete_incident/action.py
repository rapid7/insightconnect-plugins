import insightconnect_plugin_runtime
from .schema import DeleteIncidentInput, DeleteIncidentOutput, Input, Output, Component
# Custom imports below
from icon_azure_sentinel.util.helpers import AzureSentinelClient


class DeleteIncident(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_incident',
                description=Component.DESCRIPTION,
                input=DeleteIncidentInput(),
                output=DeleteIncidentOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)

        client = AzureSentinelClient(token, api_version, subscription_id)
        status_code = client.delete_incident(incident_id, resource_group_name, workspace_name)
        return {"status": status_code}

