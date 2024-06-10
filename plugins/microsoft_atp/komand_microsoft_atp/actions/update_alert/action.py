import insightconnect_plugin_runtime
from .schema import UpdateAlertInput, UpdateAlertOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class UpdateAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_alert", description=Component.DESCRIPTION, input=UpdateAlertInput(), output=UpdateAlertOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        alert_fields = params.get(Input.ALERT_FIELDS)
        alert_id = params.get(Input.ALERT_ID)
        # END INPUT BINDING - DO NOT REMOVE
        self.logger.info("Running...")
        self.logger.info(f"alert_id: {alert_id}")
        self.logger.info(f"payload: {alert_fields}")

        return {
            Output.ALERT: self.connection.client.update_alert(alert_id, payload=alert_fields),
        }
