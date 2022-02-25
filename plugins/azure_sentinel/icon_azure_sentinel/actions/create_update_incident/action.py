import insightconnect_plugin_runtime
from .schema import CreateUpdateIncidentInput, CreateUpdateIncidentOutput, Input, Component

from icon_azure_sentinel.util.helpers import AzureSentinelClient
from icon_azure_sentinel.util.tools import return_non_empty


class CreateUpdateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_update_incident",
            description=Component.DESCRIPTION,
            input=CreateUpdateIncidentInput(),
            output=CreateUpdateIncidentOutput(),
        )

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.pop(Input.APIVERSION)
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        incident_id = params.pop(Input.INCIDENTID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)

        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.create_incident(incident_id, resource_group_name, workspace_name, **params)
        return return_non_empty(data_dict)
