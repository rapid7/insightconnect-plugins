import insightconnect_plugin_runtime
from .schema import IpLookupInput, IpLookupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RateLimitError, RequestFailure


def _omit_none(value):
    if isinstance(value, dict):
        return {key: _omit_none(item) for key, item in value.items() if item is not None}
    if isinstance(value, list):
        return [_omit_none(item) for item in value if item is not None]
    return value


class IpLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_lookup",
            description=Component.DESCRIPTION,
            input=IpLookupInput(),
            output=IpLookupOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip_address = params.get(Input.IP_ADDRESS)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            resp = self.connection.gn_client.ip(ip_address)

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

        if not isinstance(resp, dict):
            resp = {}
        queried_ip = resp.get("ip") or ip_address
        output = {
            Output.IP: queried_ip,
            Output.VIZ_URL: f"https://viz.greynoise.io/ip/{queried_ip}",
        }
        scanner = resp.get("internet_scanner_intelligence")
        business = resp.get("business_service_intelligence")
        if isinstance(scanner, dict):
            output[Output.INTERNET_SCANNER_INTELLIGENCE] = _omit_none(scanner)
        if isinstance(business, dict):
            output[Output.BUSINESS_SERVICE_INTELLIGENCE] = _omit_none(business)
        return output
