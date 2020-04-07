import insightconnect_plugin_runtime
from .schema import DataExtractionInput, DataExtractionOutput, Component, Input, Output
# Custom imports below
import re
from icon_advanced_regex.util import shared


class DataExtraction(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='data_extraction',
                description=Component.DESCRIPTION,
                input=DataExtractionInput(),
                output=DataExtractionOutput())

    def run(self, params={}):
        flags = shared.constructFlags(params)
        regex = "(" + params.get(Input.IN_REGEX) + ")"
        findall = re.findall(regex, params.get(Input.IN_STRING), flags=flags)
        matches = []
        for match in findall:
            if isinstance(match, str):
                matches.append([match])
            else:
                matches.append(list(match))
        return {Output.MATCHES: matches}
