import insightconnect_plugin_runtime
from .schema import SplitInput, SplitOutput, Component, Input, Output

# Custom imports below
import re
from icon_advanced_regex.util import shared


class Split(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="split",
            description=Component.DESCRIPTION,
            input=SplitInput(),
            output=SplitOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        regex = params.get(Input.IN_REGEX, "")
        input_string = params.get(Input.IN_STRING, "")
        max_split = params.get(Input.MAX_SPLIT)
        # END INPUT BINDING - DO NOT REMOVE

        split = re.split(
            regex,
            input_string,
            maxsplit=max_split,
            flags=shared.construct_flags(params),
        )
        return {Output.RESULT: split}
