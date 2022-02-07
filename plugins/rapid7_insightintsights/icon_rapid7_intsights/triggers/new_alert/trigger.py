import insightconnect_plugin_runtime
import time
from .schema import NewAlertInput, NewAlertOutput, Input, Output, Component

# Custom imports below
from icon_rapid7_intsights.util.api import AlertParams


def current_milli_time():
    return round(time.time() * 1000)


class NewAlert(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_alert",
            description=Component.DESCRIPTION,
            input=NewAlertInput(),
            output=NewAlertOutput(),
        )

    def run(self, params={}):
        alert_params = AlertParams(
            alert_type=params.get(Input.ALERT_TYPE),
            severity=params.get(Input.SEVERITY),
            source_type=params.get(Input.SOURCE_TYPE),
            network_type=params.get(Input.NETWORK_TYPE),
            matched_asset_value=params.get(Input.MATCHED_ASSET_VALUE),
            remediation_status=params.get(Input.REMEDIATION_STATUS),
            source_date_from=params.get(Input.SOURCE_DATE_FROM),
            source_date_to=params.get(Input.SOURCE_DATE_TO),
            found_date_from=params.get(Input.FOUND_DATE_FROM),
            found_date_to=params.get(Input.FOUND_DATE_TO),
            assigned=params.get(Input.ASSIGNED),
            is_flagged=params.get(Input.IS_FLAGGED),
            is_closed=params.get(Input.IS_CLOSED),
            has_ioc=params.get(Input.HAS_INDICATORS),
        )

        while True:
            results = self.connection.client.get_alerts(alert_params)

            self.send({Output.ALERT_IDS: results})
            alert_params.found_date_from = current_milli_time()
            time.sleep(params.get(Input.FREQUENCY, 60))
