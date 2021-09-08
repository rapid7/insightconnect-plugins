import insightconnect_plugin_runtime
from .schema import MacExtractorInput, MacExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract


class MacExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="mac_extractor",
            description=Component.DESCRIPTION,
            input=MacExtractorInput(),
            output=MacExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.MAC_ADDRS: extract(Regex.MACAddress, params.get(Input.STR), params.get(Input.FILE))}
