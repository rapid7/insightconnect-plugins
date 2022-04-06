import insightconnect_plugin_runtime
from icon_azure_sentinel.util.tools import map_output

from .schema import Component, GetIncidentInput, GetIncidentOutput, Input

# Custom imports below


class GetIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_incident", description=Component.DESCRIPTION, input=GetIncidentInput(), output=GetIncidentOutput()
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        data_dict = self.connection.api_client.get_incident(
            incident_id, resource_group_name, workspace_name, subscription_id
        )
        data_dict = map_output(data_dict)
        return data_dict
