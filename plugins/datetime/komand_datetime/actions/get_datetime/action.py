import time

import insightconnect_plugin_runtime
import maya

from .schema import GetDatetimeInput, GetDatetimeOutput, Input, Output


class GetDatetime(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_datetime",
            description="Gets the current datetime in a specified format",
            input=GetDatetimeInput(),
            output=GetDatetimeOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        format_string = params.get(Input.FORMAT_STRING, "%d %b %Y %H:%M:%S")
        use_rfc3339_format = params.get(Input.USE_RFC3339_FORMAT, False)
        # END INPUT BINDING - DO NOT REMOVE

        if not use_rfc3339_format:
            current_time = time.strftime(format_string)
        else:
            current_time = maya.now().rfc3339()

        return {Output.DATETIME: current_time, Output.EPOCH_TIMESTAMP: maya.now().epoch}
