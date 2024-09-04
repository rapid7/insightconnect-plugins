import insightconnect_plugin_runtime
import maya

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import EpochFromDateInput, EpochFromDateOutput, Input, Output


class EpochFromDate(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="epoch_from_date",
            description="Convert a datetime to an Epoch",
            input=EpochFromDateInput(),
            output=EpochFromDateOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        date = params.get(Input.DATETIME)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            return {Output.EPOCH: int(maya.MayaDT.from_rfc3339(date).epoch)}
        except TypeError:
            self.logger.error("Non-RFC3339 date provided, input datetime must be RFC3339")
            raise PluginException(
                cause="Non-RFC3339 date provided",
                assistance="Please make sure that provided datetime is in RFC3339 format and try again.",
            )
        except Exception as error:
            self.logger.error(f"Unknown error occurred. The error is: `{error}`")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
