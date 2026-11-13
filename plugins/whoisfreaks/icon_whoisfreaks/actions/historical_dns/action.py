import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import HistoricalDnsInput, HistoricalDnsOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class HistoricalDns(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="historical_dns",
            description=Component.DESCRIPTION,
            input=HistoricalDnsInput(),
            output=HistoricalDnsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN)
        page = params.get(Input.PAGE)
        record_types = params.get(Input.RECORD_TYPES)
        # END INPUT BINDING - DO NOT REMOVE

        params = {
            "domainName": validators.domain(domain),
            "type": validators.record_types(record_types, allow_ptr=False),
            "page": validators.integer(page, "Page", 1, default=1),
        }
        result = self.connection.client.lookup("Historical DNS", "GET", constants.PATH_HISTORICAL_DNS, params)
        return outputs.paged(result, "historicalDnsRecords", ("totalRecords",), ("totalPages",), ("currentPage",))
