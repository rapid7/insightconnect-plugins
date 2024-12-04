import insightconnect_plugin_runtime
from .schema import SimilarLookupInput, SimilarLookupOutput, Input, Output, Component

# Custom imports below


class SimilarLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="similar_lookup",
            description=Component.DESCRIPTION,
            input=SimilarLookupInput(),
            output=SimilarLookupOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip_address = params.get(Input.IP_ADDRESS)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            resp = self.connection.gn_client.similar(ip_address)

        except RequestFailure as error:
            raise PluginException(
                cause=f"API responded with ERROR: {error.args[0]} - {error.args[1]}.",
                assistance="Please check error and try again.",
            )

        except ValueError as error:
            raise PluginException(
                cause=f"Input does not appear to be valid: {ip_address}. Error Message: {error.args[0]}",
                assistance="Please provide a valid IPv4 Address.",
            )

        return {Output.IP: resp.get("ip"), Output.SIMILAR_IPS: resp.get("similar_ips"), Output.TOTAL: resp.get("total")}
