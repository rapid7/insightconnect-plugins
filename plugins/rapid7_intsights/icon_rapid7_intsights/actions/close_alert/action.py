import insightconnect_plugin_runtime
from .schema import CloseAlertInput, CloseAlertOutput, Input, Output, Component

# Custom imports below
from icon_rapid7_intsights.util.constants import closing_ticket_reasons
from icon_rapid7_intsights.util.helpers import clean


class CloseAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_alert", description=Component.DESCRIPTION, input=CloseAlertInput(), output=CloseAlertOutput()
        )

    def run(self, params={}):
        alert_id = params.get(Input.ALERTID)
        json_data = {
            "Reason": closing_ticket_reasons.get(params.get(Input.REASON)),
            "FreeText": params.get(Input.FREETEXT),
            "IsHidden": params.get(Input.ISHIDDEN),
            "Rate": params.get(Input.RATE),
        }
        self.logger.info(f"Closing alert with ID: {alert_id}")
        return {Output.SUCCESS: self.connection.client.close_alert(alert_id, clean(json_data))}
