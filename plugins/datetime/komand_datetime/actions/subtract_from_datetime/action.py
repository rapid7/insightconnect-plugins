import insightconnect_plugin_runtime
import maya

from .schema import Input, Output, SubtractFromDatetimeInput, SubtractFromDatetimeOutput
from insightconnect_plugin_runtime.exceptions import PluginException


class SubtractFromDatetime(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="subtract_from_datetime",
            description="Subtract datetime units from a datetime",
            input=SubtractFromDatetimeInput(),
            output=SubtractFromDatetimeOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        base_time = params.get(Input.BASE_TIME)
        years = params.get(Input.YEARS)
        months = params.get(Input.MONTHS)
        days = params.get(Input.DAYS)
        hours = params.get(Input.HOURS)
        minutes = params.get(Input.MINUTES)
        seconds = params.get(Input.SECONDS)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            new_date = maya.MayaDT.from_rfc3339(base_time)
        except Exception as error:
            self.logger.error(f"Unknown error occurred. The error is: `{error}`")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        return {
            Output.DATE: new_date.subtract(
                years=years,
                months=months,
                days=days,
                hours=hours,
                minutes=minutes,
                seconds=seconds,
            ).rfc3339()
        }
