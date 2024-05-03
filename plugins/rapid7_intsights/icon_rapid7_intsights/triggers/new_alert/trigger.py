import insightconnect_plugin_runtime
import time
from .schema import NewAlertInput, NewAlertOutput, Input, Output, Component

# Custom imports below
from icon_rapid7_intsights.util.api import AlertParams
from icon_rapid7_intsights.util.api import current_milli_time, subtract_day, subtract_hour, subtract_week
from insightconnect_plugin_runtime.exceptions import PluginException


class NewAlert(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_alert",
            description=Component.DESCRIPTION,
            input=NewAlertInput(),
            output=NewAlertOutput(),
        )

    def run(self, params={}):
        SOURCE_FROM_ENUM = params.get(Input.SOURCE_DATE_FROM_ENUM, "")
        SOURCE_FROM_STRING = params.get(Input.SOURCE_DATE_FROM, "")
        source_date = ""

        # If both are present - throw error
        if SOURCE_FROM_STRING and SOURCE_FROM_ENUM:
            raise PluginException(
                cause="You cannot have both enum and string.", assistance="Ensure only enum or string is selected"
            )

        # If source date normal is empty - use enum
        if SOURCE_FROM_ENUM:
            if SOURCE_FROM_ENUM == "Hour":
                source_date = subtract_hour(current_milli_time())
            elif SOURCE_FROM_ENUM == "Day":
                source_date = subtract_day(current_milli_time())
            elif SOURCE_FROM_ENUM == "Week":
                source_date = subtract_week(current_milli_time())

        # If source date from enum empty - use regular one
        if SOURCE_FROM_STRING:
            source_date = SOURCE_FROM_STRING

        alert_params = AlertParams(
            alert_type=params.get(Input.ALERT_TYPE),
            severity=params.get(Input.SEVERITY),
            source_type=params.get(Input.SOURCE_TYPE),
            network_type=params.get(Input.NETWORK_TYPE),
            matched_asset_value=params.get(Input.MATCHED_ASSET_VALUE),
            remediation_status=params.get(Input.REMEDIATION_STATUS),
            source_date_from=source_date,
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

            if results:
                self.send({Output.ALERT_IDS: results})
            alert_params.found_date_from = current_milli_time()
            time.sleep(params.get(Input.FREQUENCY, 60))
