import insightconnect_plugin_runtime
from .schema import UuidExtractorInput, UuidExtractorOutput, Input, Output, Component

# Custom imports below

from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract


class UuidExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="uuid_extractor",
            description=Component.DESCRIPTION,
            input=UuidExtractorInput(),
            output=UuidExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.UUIDS: extract(Regex.UUID, params.get(Input.STR), params.get(Input.FILE))}
