import insightconnect_plugin_runtime
from .schema import DateExtractorInput, DateExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.extractor import extract, parse_time, define_date_time_regex


class DateExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="date_extractor",
            description=Component.DESCRIPTION,
            input=DateExtractorInput(),
            output=DateExtractorOutput(),
        )

    def run(self, params={}):
        return {Output.DATES: parse_time(extract(define_date_time_regex(Input.DATE_FORMAT), params.get(Input.STR), params.get(Input.FILE),Input.DATE_FORMAT))}

