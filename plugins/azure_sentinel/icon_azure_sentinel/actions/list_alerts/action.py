import insightconnect_plugin_runtime

from .schema import Component, Input, ListAlertsInput, ListAlertsOutput, Output


class ListAlerts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_alerts", description=Component.DESCRIPTION, input=ListAlertsInput(), output=ListAlertsOutput()
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        alerts = self.connection.api_client.list_alerts(
            incident_id, resource_group_name, workspace_name, subscription_id
        )
        return {Output.ALERTS: alerts}
