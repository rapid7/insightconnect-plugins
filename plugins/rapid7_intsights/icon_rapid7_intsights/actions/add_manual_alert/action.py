import insightconnect_plugin_runtime
from .schema import AddManualAlertInput, AddManualAlertOutput, Input, Output, Component

# Custom imports below
from icon_rapid7_intsights.util.api import ManualAlertParams


class AddManualAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_manual_alert",
            description=Component.DESCRIPTION,
            input=AddManualAlertInput(),
            output=AddManualAlertOutput(),
        )

    def run(self, params={}):
        return {
            Output.ALERT_ID: self.connection.client.add_manual_alert(
                ManualAlertParams(
                    title=params.get(Input.TITLE),
                    found_date=params.get(Input.FOUND_DATE),
                    description=params.get(Input.DESCRIPTION),
                    type=params.get(Input.TYPE),
                    sub_type=params.get(Input.SUB_TYPE),
                    severity=params.get(Input.SEVERITY),
                    source_type=params.get(Input.SOURCE_TYPE),
                    source_network_type=params.get(Input.SOURCE_NETWORK_TYPE),
                    source_url=params.get(Input.SOURCE_URL),
                    source_date=params.get(Input.SOURCE_DATE),
                    images=params.get(Input.IMAGES),
                )
            )
        }
