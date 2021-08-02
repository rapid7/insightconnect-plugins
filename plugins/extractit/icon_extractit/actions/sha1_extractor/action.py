import insightconnect_plugin_runtime
from .schema import Sha1ExtractorInput, Sha1ExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract


class Sha1Extractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sha1_extractor",
            description=Component.DESCRIPTION,
            input=Sha1ExtractorInput(),
            output=Sha1ExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.SHA1: extract(Regex.SHA1, params.get(Input.STR), params.get(Input.FILE))}
