import insightconnect_plugin_runtime
from .schema import GetAlertsInput, GetAlertsOutput, Input, Output, Component

# Custom imports below


class GetAlerts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alerts", description=Component.DESCRIPTION, input=GetAlertsInput(), output=GetAlertsOutput()
        )

    def run(self, params={}):
        filters = params.get(Input.FILTERS)
        limit = params.get(Input.LIMIT)
        filters["limit"] = limit if limit else 20
        return {
            Output.ALERTS: self.connection.api.get_alerts(insightconnect_plugin_runtime.helper.clean_dict(filters)).get(
                "data", []
            )
        }
