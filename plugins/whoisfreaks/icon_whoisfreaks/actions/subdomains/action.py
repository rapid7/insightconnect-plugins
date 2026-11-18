import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import SubdomainsInput, SubdomainsOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class Subdomains(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="subdomains",
            description=Component.DESCRIPTION,
            input=SubdomainsInput(),
            output=SubdomainsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        after = params.get(Input.AFTER)
        before = params.get(Input.BEFORE)
        domain = params.get(Input.DOMAIN)
        page = params.get(Input.PAGE)
        status = params.get(Input.STATUS)
        # END INPUT BINDING - DO NOT REMOVE

        after = validators.date(after, "After")
        before = validators.date(before, "Before")
        if after and before and after > before:
            raise validators.input_error(
                f"After {after} is later than Before {before}", "Set After to a date before Before"
            )
        params = {
            "domain": validators.domain(domain),
            "after": after,
            "before": before,
            "status": validators.optional_text(status),
            "page": validators.integer(page, "Page", 1, default=1),
        }
        result = self.connection.client.lookup("Subdomains", "GET", constants.PATH_SUBDOMAINS, params)
        return outputs.paged(result, "subdomains", ("total_records",), ("total_pages",), ("current_page",))
