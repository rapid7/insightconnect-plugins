import insightconnect_plugin_runtime
from .schema import (
    GetAlertDetailsInput,
    GetAlertDetailsOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import pytmv1


class GetAlertDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert_details",
            description=Component.DESCRIPTION,
            input=GetAlertDetailsInput(),
            output=GetAlertDetailsOutput(),
        )

    def run(self, params={}):
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        alert_id = params.get(Input.ALERT_ID)
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.get_alert_details(alert_id=alert_id)
        if "error" in response.result_code.lower():
            return response
        else:
            self.logger.info("Returning Results...")
            return {
                Output.ETAG: response.response.etag,
                Output.ALERT_DETAILS: {"alert": response.response.alert.json()},
            }
