import insightconnect_plugin_runtime
from .schema import Sha256ExtractorInput, Sha256ExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract


class Sha256Extractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sha256_extractor",
            description=Component.DESCRIPTION,
            input=Sha256ExtractorInput(),
            output=Sha256ExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.SHA256: extract(Regex.SHA256, params.get(Input.STR), params.get(Input.FILE))}
