import insightconnect_plugin_runtime
from .schema import GetIncidentInput, GetIncidentOutput, Input, Component
from icon_azure_sentinel.util.helpers import AzureSentinelClient
from icon_azure_sentinel.util.tools import return_non_empty
# Custom imports below

class GetIncident(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_incident',
                description=Component.DESCRIPTION,
                input=GetIncidentInput(),
                output=GetIncidentOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
    
        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.get_incident(incident_id, resource_group_name, workspace_name)

        return return_non_empty(data_dict)
