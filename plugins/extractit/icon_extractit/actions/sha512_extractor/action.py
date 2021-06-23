import insightconnect_plugin_runtime
from .schema import Sha512ExtractorInput, Sha512ExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex, Extractor


class Sha512Extractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sha512_extractor",
            description=Component.DESCRIPTION,
            input=Sha512ExtractorInput(),
            output=Sha512ExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.SHA512: Extractor.extract(Regex.SHA512, params.get(Input.STR), params.get(Input.FILE))}
