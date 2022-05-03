import insightconnect_plugin_runtime
from .schema import ListAlertsInput, ListAlertsOutput

# Custom imports below


class ListAlerts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_alerts",
            description="List Carbon BlackLi alerts with given parameters",
            input=ListAlertsInput(),
            output=ListAlertsOutput(),
        )

    def run(self, params={}):
        query_params = [
            ("q", params.get("query", "")),
            ("rows", params.get("rows", 10)),
            ("start", params.get("start", 0)),
        ]
        try:
            results = self.connection.carbon_black.get_object("/api/v1/alert", query_parameters=query_params)["results"]
        except Exception as ex:
            self.logger.error("Failed to get alerts: %s", ex)
            raise ex

        results = insightconnect_plugin_runtime.helper.clean(results)

        return {"alerts": results}

    def test(self):
        if self.connection.test():
            return {}
