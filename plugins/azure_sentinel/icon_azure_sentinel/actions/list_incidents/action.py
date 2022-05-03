import insightconnect_plugin_runtime

from .schema import Component, Input, ListIncidentsInput, ListIncidentsOutput, Output
from icon_azure_sentinel.util.tools import map_output_for_list


class ListIncidents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_incidents",
            description=Component.DESCRIPTION,
            input=ListIncidentsInput(),
            output=ListIncidentsOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        filters = {
            Input.ORDERBY: params.get(Input.ORDERBY),
        }
        incidents = self.connection.api_client.list_incident(
            resource_group_name, workspace_name, filters, subscription_id
        )
        incidents = map_output_for_list(incidents)
        return {Output.INCIDENTS: incidents}
