import insightconnect_plugin_runtime
from .schema import CveExtractorInput, CveExtractorOutput, Input, Output, Component

# Custom imports below

from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract


class CveExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="cve_extractor",
            description=Component.DESCRIPTION,
            input=CveExtractorInput(),
            output=CveExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.CVES: extract(Regex.CVE, params.get(Input.STR), params.get(Input.FILE))}
