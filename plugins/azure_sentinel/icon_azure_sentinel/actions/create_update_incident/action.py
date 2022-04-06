import insightconnect_plugin_runtime
from icon_azure_sentinel.util.tools import return_non_empty, map_output

from .schema import Component, CreateUpdateIncidentInput, CreateUpdateIncidentOutput, Input


class CreateUpdateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_update_incident",
            description=Component.DESCRIPTION,
            input=CreateUpdateIncidentInput(),
            output=CreateUpdateIncidentOutput(),
        )

    def run(self, params={}):
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        incident_id = params.pop(Input.INCIDENTID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)

        data_dict = self.connection.api_client.create_incident(
            incident_id, resource_group_name, workspace_name, subscription_id, **params
        )
        data_dict = map_output(data_dict)
        return return_non_empty(data_dict)
