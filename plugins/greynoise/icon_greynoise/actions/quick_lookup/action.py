import insightconnect_plugin_runtime
from .schema import QuickLookupInput, QuickLookupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RateLimitError, RequestFailure


def _omit_none(value):
    if isinstance(value, dict):
        return {key: _omit_none(item) for key, item in value.items() if item is not None}
    if isinstance(value, list):
        return [_omit_none(item) for item in value if item is not None]
    return value


class QuickLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quick_lookup", description=Component.DESCRIPTION, input=QuickLookupInput(), output=QuickLookupOutput()
        )

    def run(self, params={}):
        ip_address = params.get(Input.IP_ADDRESS)
        try:
            resp = self.connection.gn_client.quick(ip_address)

        except RateLimitError as error:
            raise PluginException(
                cause="GreyNoise API rate limit exceeded.",
                assistance="Wait and try again.",
                data=str(error),
            )

        except RequestFailure as error:
            raise PluginException(
                cause=f"API responded with ERROR: {error.args[0]} - {error.args[1]}.",
                assistance="Please check error and try again.",
            )

        except ValueError as error:
            raise PluginException(
                cause=f"Input does not appear to be valid: {ip_address}. Error Message: {error.args[0]}",
                assistance="Please provide a valid public IPv4 address.",
            )

        if not isinstance(resp, list) or not resp or not isinstance(resp[0], dict):
            raise PluginException(
                cause=f"Input does not appear to be valid: {ip_address}.",
                assistance="Please provide a valid public IPv4 address.",
            )

        item = resp[0]
        output = {Output.IP: item.get("ip") or ip_address}
        scanner = item.get("internet_scanner_intelligence")
        business = item.get("business_service_intelligence")
        if isinstance(scanner, dict):
            output[Output.INTERNET_SCANNER_INTELLIGENCE] = _omit_none(scanner)
        if isinstance(business, dict):
            output[Output.BUSINESS_SERVICE_INTELLIGENCE] = _omit_none(business)
        return output
