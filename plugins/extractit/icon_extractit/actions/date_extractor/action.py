import insightconnect_plugin_runtime
from .schema import DateExtractorInput, DateExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.extractor import (
    extract,
    extract_all_date_formats,
    parse_time,
    parse_time_all_date_formats,
    define_date_time_regex,
)


class DateExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="date_extractor",
            description=Component.DESCRIPTION,
            input=DateExtractorInput(),
            output=DateExtractorOutput(),
        )

    def run(self, params={}):
        if params.get(Input.DATE_FORMAT) == "All Formats":
            return {
                Output.DATES: parse_time_all_date_formats(
                    extract_all_date_formats(
                        params.get(Input.STR),
                        params.get(Input.FILE),
                    )
                )
            }
        return {
            Output.DATES: parse_time(
                extract(
                    define_date_time_regex(params.get(Input.DATE_FORMAT)),
                    params.get(Input.STR),
                    params.get(Input.FILE),
                ),
                params.get(Input.DATE_FORMAT),
            )
        }
