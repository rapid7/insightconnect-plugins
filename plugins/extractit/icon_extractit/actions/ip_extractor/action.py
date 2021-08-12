import insightconnect_plugin_runtime
from .schema import IpExtractorInput, IpExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract


class IpExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_extractor", description=Component.DESCRIPTION, input=IpExtractorInput(), output=IpExtractorOutput()
        )

    def run(self, params={}):
        matches = []
        matches.extend(extract(Regex.IPv4, params.get(Input.STR), params.get(Input.FILE)))
        matches.extend(extract(Regex.IPv6, params.get(Input.STR), params.get(Input.FILE)))
        return {Output.IP_ADDRS: matches}
