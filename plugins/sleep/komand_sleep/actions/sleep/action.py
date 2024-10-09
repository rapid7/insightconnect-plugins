import time

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import Component, Input, Output, SleepInput, SleepOutput


class Sleep(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sleep",
            description=Component.DESCRIPTION,
            input=SleepInput(),
            output=SleepOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        interval = params.get(Input.INTERVAL)
        # END INPUT BINDING - DO NOT REMOVE

        if int(interval) < 0:
            raise PluginException(
                cause="Wrong input",
                assistance=f"{Input.INTERVAL.capitalize()} should not be less than zero",
            )
        time.sleep(interval)
        return {Output.SLEPT: interval}
