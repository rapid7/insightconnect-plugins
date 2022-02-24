import insightconnect_plugin_runtime

from icon_azure_sentinel.util.helpers import AzureSentinelClient
from .schema import ListAlertsInput, ListAlertsOutput, Input, Output, Component
# Custom imports below

class ListAlerts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_alerts',
                description=Component.DESCRIPTION,
                input=ListAlertsInput(),
                output=ListAlertsOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        filters = {
            Input.FILTER: params.get(Input.FILTER),
            Input.ORDERBY: params.get(Input.ORDERBY),
            Input.TOP: params.get(Input.TOP)
        }
        client = AzureSentinelClient(token, api_version, subscription_id)
        alerts = client.list_alerts(incident_id, resource_group_name, workspace_name, filters)
        return {Output.ALERTS: alerts}
