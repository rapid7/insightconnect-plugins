import insightconnect_plugin_runtime
from .schema import ToUtcInput, ToUtcOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from maya.core import parse
import maya


class ToUtc(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="to_utc",
            description=Component.DESCRIPTION,
            input=ToUtcInput(),
            output=ToUtcOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        base_time = params.get(Input.BASE_TIME)
        timezone = params.get(Input.TIMEZONE)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            converted_date = maya.MayaDT.from_datetime(parse(base_time, timezone=timezone).datetime()).rfc3339()
        except Exception as error:
            self.logger.error(f"Unknown error occurred. The error is: `{error}`")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        return {Output.CONVERTED_DATE: converted_date}
