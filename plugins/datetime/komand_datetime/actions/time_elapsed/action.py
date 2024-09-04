import insightconnect_plugin_runtime
import maya

from .schema import Input, Output, TimeElapsedInput, TimeElapsedOutput
from insightconnect_plugin_runtime.exceptions import PluginException


class TimeElapsed(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="time_elapsed",
            description="Determine the elapsed time between two dates",
            input=TimeElapsedInput(),
            output=TimeElapsedOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        time1 = params.get(Input.FIRST_TIME)
        time2 = params.get(Input.SECOND_TIME)
        unit = params.get(Input.RESULT_UNIT)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            difference = int(
                maya.MayaInterval(
                    start=maya.MayaDT.from_rfc3339(time1), end=maya.MayaDT.from_rfc3339(time2)
                ).timedelta.total_seconds()
            )
        except Exception as error:
            self.logger.error(f"Unknown error occurred. The error is: `{error}`")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        if unit == "Minutes":
            difference = int(round(difference / 60))
        elif unit == "Hours":
            difference = int(round(difference / 3600))
        elif unit == "Days":
            difference = int(round(difference / 86400))
        elif unit == "Months":
            difference = int(round(difference / 2628000))
        elif unit == "Years":
            difference = int(round(difference / 31540000))

        return {Output.DIFFERENCE: difference, Output.TIME_UNIT: unit}
