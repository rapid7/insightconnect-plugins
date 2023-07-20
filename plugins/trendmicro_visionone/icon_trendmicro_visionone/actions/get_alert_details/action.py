import insightconnect_plugin_runtime
from .schema import (
    GetAlertDetailsInput,
    GetAlertDetailsOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class GetAlertDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert_details",
            description=Component.DESCRIPTION,
            input=GetAlertDetailsInput(),
            output=GetAlertDetailsOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        alert_id = params.get(Input.ALERT_ID)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.get_alert_details(alert_id=alert_id)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting the alert details.",
                assistance="Please check the alert ID and try again.",
                data=response,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {
            Output.ETAG: response.response.etag,
            Output.ALERT_DETAILS: {"alert": response.response.alert.dict()},
        }
