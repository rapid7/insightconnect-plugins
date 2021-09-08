import insightconnect_plugin_runtime
from .schema import Md5ExtractorInput, Md5ExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract


class Md5Extractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="md5_extractor",
            description=Component.DESCRIPTION,
            input=Md5ExtractorInput(),
            output=Md5ExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.MD5: extract(Regex.MD5, params.get(Input.STR), params.get(Input.FILE))}
