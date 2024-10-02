import insightconnect_plugin_runtime
from .schema import DataExtractionInput, DataExtractionOutput, Component, Input, Output

# Custom imports below
import re
from icon_advanced_regex.util import shared


class DataExtraction(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="data_extraction",
            description=Component.DESCRIPTION,
            input=DataExtractionInput(),
            output=DataExtractionOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        regex = f"({params.get(Input.IN_REGEX, '')})"
        input_string = params.get(Input.IN_STRING, "")
        # END INPUT BINDING - DO NOT REMOVE

        findall = re.findall(regex, input_string, flags=shared.construct_flags(params))
        matches = []
        for match in findall:
            if isinstance(match, str):
                matches.append([match])
            else:
                matches.append(list(match))
        return {Output.MATCHES: matches}
