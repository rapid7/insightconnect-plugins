import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import ReverseDnsInput, ReverseDnsOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class ReverseDns(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_dns",
            description=Component.DESCRIPTION,
            input=ReverseDnsInput(),
            output=ReverseDnsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        exact = params.get(Input.EXACT)
        page = params.get(Input.PAGE)
        record_type = params.get(Input.RECORD_TYPE)
        sort = params.get(Input.SORT)
        value = params.get(Input.VALUE)
        # END INPUT BINDING - DO NOT REMOVE

        record_type = (record_type or "a").lower()
        search_value = validators.optional_text(value)
        if not search_value:
            raise validators.input_error("Value is empty", "Provide the record value to search for")
        if record_type in ("a", "aaaa"):
            search_value, reason = validators.ip(search_value, "Value")
            if reason:
                return outputs.not_looked_up(reason)
        params = {
            "value": search_value,
            "type": record_type,
            "exact": exact if isinstance(exact, bool) else True,
            "sort": validators.optional_text(sort),
            "page": validators.integer(page, "Page", 1, default=1),
        }
        result = self.connection.client.lookup("Reverse DNS", "GET", constants.PATH_REVERSE_DNS, params)
        return outputs.paged(result, "reverseDnsRecords", ("totalRecords",), ("totalPages",), ("currentPage",))
