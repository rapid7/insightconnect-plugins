import insightconnect_plugin_runtime
from .schema import FilepathExtractorInput, FilepathExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract_filepath


class FilepathExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="filepath_extractor",
            description=Component.DESCRIPTION,
            input=FilepathExtractorInput(),
            output=FilepathExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.FILEPATHS: extract_filepath(Regex.FilePath, params.get(Input.STR), params.get(Input.FILE))}
