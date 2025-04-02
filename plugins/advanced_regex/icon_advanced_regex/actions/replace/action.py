import insightconnect_plugin_runtime
from .schema import ReplaceInput, ReplaceOutput, Component, Input, Output

# Custom imports below
import re
from icon_advanced_regex.util import shared


class Replace(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="replace",
            description=Component.DESCRIPTION,
            input=ReplaceInput(),
            output=ReplaceOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        regex = params.get(Input.IN_REGEX, "")
        input_string = params.get(Input.IN_STRING, "")
        replace_string = params.get(Input.REPLACE_STRING, "")
        replace_number = params.get(Input.MAX_REPLACE)
        # END INPUT BINDING - DO NOT REMOVE

        replaced = re.sub(
            regex,
            replace_string,
            input_string,
            count=replace_number,
            flags=shared.construct_flags(params),
        )
        return {Output.RESULT: replaced}
