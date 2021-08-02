import insightconnect_plugin_runtime
from .schema import UrlExtractorInput, UrlExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract, clear_urls


class UrlExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="url_extractor",
            description=Component.DESCRIPTION,
            input=UrlExtractorInput(),
            output=UrlExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.URLS: clear_urls(extract(Regex.URL, params.get(Input.STR), params.get(Input.FILE)))}
