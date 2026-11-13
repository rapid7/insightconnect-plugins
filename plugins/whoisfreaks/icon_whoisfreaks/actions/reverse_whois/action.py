import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import ReverseWhoisInput, ReverseWhoisOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class ReverseWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_whois",
            description=Component.DESCRIPTION,
            input=ReverseWhoisInput(),
            output=ReverseWhoisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        company = params.get(Input.COMPANY)
        email = params.get(Input.EMAIL)
        exact = params.get(Input.EXACT)
        keyword = params.get(Input.KEYWORD)
        mode = params.get(Input.MODE)
        owner = params.get(Input.OWNER)
        page = params.get(Input.PAGE)
        # END INPUT BINDING - DO NOT REMOVE

        criteria = {
            "keyword": validators.optional_text(keyword),
            "email": validators.optional_text(email),
            "owner": validators.optional_text(owner),
            "company": validators.optional_text(company),
        }
        if not any(criteria.values()):
            raise validators.input_error(
                "Reverse WHOIS needs a search value", "Provide at least one of Keyword, Email, Owner or Company"
            )
        params = dict(
            criteria,
            mode=mode or "default",
            exact=bool(exact),
            page=validators.integer(page, "Page", 1, default=1),
        )
        result = self.connection.client.lookup("Reverse WHOIS", "GET", constants.PATH_REVERSE_WHOIS, params)
        return outputs.paged(
            result,
            "whois_domains_historical",
            ("total_Result", "Total_Result", "total_result", "total_records"),
            ("total_Pages", "Total_Pages", "total_pages"),
            ("current_Page", "Current_Page", "current_page"),
        )
