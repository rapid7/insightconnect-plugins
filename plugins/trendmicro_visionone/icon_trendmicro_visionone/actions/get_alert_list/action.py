import insightconnect_plugin_runtime
from .schema import GetAlertListInput, GetAlertListOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import json


class GetAlertList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert_list",
            description=Component.DESCRIPTION,
            input=GetAlertListInput(),
            output=GetAlertListOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        start_date_time = params.get(Input.START_DATE_TIME)
        end_date_time = params.get(Input.END_DATE_TIME)
        new_alerts = []
        # Make Action API Call
        self.logger.info("Creating alert list...")
        response = client.alert.consume(
            lambda alert: new_alerts.append(json.loads(alert.model_dump_json())),
            start_time=start_date_time,
            end_time=end_date_time,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while trying to get the alert list.",
                assistance="Please check the provided parameters and try again.",
                data=response.error,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.TOTAL_COUNT: len(new_alerts), Output.ALERTS: new_alerts}
