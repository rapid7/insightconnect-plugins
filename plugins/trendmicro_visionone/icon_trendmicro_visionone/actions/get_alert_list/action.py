import insightconnect_plugin_runtime
from .schema import GetAlertListInput, GetAlertListOutput, Input, Output, Component

# Custom imports below
import pytmv1
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
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        start_date_time = params.get(Input.START_DATE_TIME)
        end_date_time = params.get(Input.END_DATE_TIME)
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        new_alerts = []
        # Make Action API Call
        self.logger.info("Creating alert list...")
        try:
            client.consume_alert_list(
                lambda alert: new_alerts.append(alert.json()),
                start_time=start_date_time,
                end_time=end_date_time,
            )
        except Exception as e:
            self.logger.info("Consume Alert List failed with following exception:")
            return e
        # Load json objects to list
        alert_list = []
        for i in new_alerts:
            alert_list.append(json.loads(i))
        self.logger.info("Returning Results...")
        return {Output.TOTAL_COUNT: len(new_alerts), Output.ALERTS: alert_list}
