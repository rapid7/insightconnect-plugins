import insightconnect_plugin_runtime

from .schema import Component, Input, IpInput, IpOutput, Output

# Custom imports below


class Ip(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip",
            description=Component.DESCRIPTION,
            input=IpInput(),
            output=IpOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query_type = params.get(Input.QUERY_TYPE, "")
        address = params.get(Input.ADDRESS, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.ip_lookup(address, query_type)}
