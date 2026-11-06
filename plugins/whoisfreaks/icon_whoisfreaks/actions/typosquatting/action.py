import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import TyposquattingInput, TyposquattingOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class Typosquatting(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="typosquatting",
            description=Component.DESCRIPTION,
            input=TyposquattingInput(),
            output=TyposquattingOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        fetch_size = params.get(Input.FETCH_SIZE)
        keyword = params.get(Input.KEYWORD)
        page_token = params.get(Input.PAGE_TOKEN)
        pattern = params.get(Input.PATTERN)
        # END INPUT BINDING - DO NOT REMOVE

        keyword = validators.optional_text(keyword)
        pattern = validators.optional_text(pattern)
        if bool(keyword) == bool(pattern):
            raise validators.input_error(
                "Typosquatting needs exactly one of Keyword or Pattern", "Provide either Keyword or Pattern, not both"
            )
        params = {
            "keyword": keyword,
            "pattern": pattern,
            "pageToken": validators.optional_text(page_token),
            "fetch_size": validators.integer(fetch_size, "Fetch Size", 1, 100, default=100),
        }
        result = self.connection.client.lookup("Typosquatting", "GET", constants.PATH_TYPOSQUATTING, params)
        output = outputs.paged(result, "domains", ("totalRecords",), ("totalPages",), ("currentPage",))
        data = result.data_dict
        output.update(
            outputs.compact(
                {
                    Output.HAS_NEXT_PAGE: outputs.to_bool(data.get("hasNextPage")),
                    Output.NEXT_PAGE_TOKEN: outputs.to_str(data.get("nextPageToken")),
                }
            )
        )
        return output
