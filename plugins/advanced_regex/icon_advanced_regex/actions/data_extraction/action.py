import insightconnect_plugin_runtime
from .schema import DataExtractionInput, DataExtractionOutput, Component, Input, Output

# Custom imports below
import re
from icon_advanced_regex.util import shared


class DataExtraction(insightconnect_plugin_runtime.Action):
    def __init__(self) -> None:
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
        matches = [{"value": [match] if isinstance(match, str) else list(match)} for match in findall]
        return {Output.MATCHES: matches}
