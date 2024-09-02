import insightconnect_plugin_runtime
from .schema import GetFutureTimeInput, GetFutureTimeOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from datetime import datetime, timedelta
import maya


class GetFutureTime(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_future_time",
            description=Component.DESCRIPTION,
            input=GetFutureTimeInput(),
            output=GetFutureTimeOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        base_timestamp = params.get(Input.BASE_TIMESTAMP)
        time_unit = params.get(Input.TIME_UNIT)
        time_amount = params.get(Input.TIME_AMOUNT)
        # END INPUT BINDING - DO NOT REMOVE

        if not base_timestamp:
            new_timestamp = maya.MayaDT.from_rfc3339(datetime.now())
        else:
            try:
                new_timestamp = maya.MayaDT.from_rfc3339(params.get(Input.BASE_TIMESTAMP))
            except Exception as error:
                self.logger.error(f"Unknown error occurred. The error is: `{error}`")
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        if time_unit == "Months":
            new_timestamp = new_timestamp + timedelta(days=30 * time_amount)
        elif time_unit == "Weeks":
            new_timestamp = new_timestamp + timedelta(weeks=time_amount)
        elif time_unit == "Days":
            new_timestamp = new_timestamp + timedelta(days=time_amount)
        elif time_unit == "Hours":
            new_timestamp = new_timestamp + timedelta(hours=time_amount)
        elif time_unit == "Minutes":
            new_timestamp = new_timestamp + timedelta(minutes=time_amount)
        else:
            new_timestamp = new_timestamp + timedelta(seconds=time_amount)
        return {
            Output.TIMESTAMP: maya.MayaDT.from_datetime(
                new_timestamp.datetime(to_timezone=params.get(Input.TIME_ZONE), naive=True)
            ).rfc3339()
        }
