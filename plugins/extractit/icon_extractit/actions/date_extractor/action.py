import insightconnect_plugin_runtime
from .schema import DateExtractorInput, DateExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex, Extractor


class DateExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="date_extractor",
            description=Component.DESCRIPTION,
            input=DateExtractorInput(),
            output=DateExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.DATES: Extractor.extract(Regex.Date, params.get(Input.STR), params.get(Input.FILE))}
