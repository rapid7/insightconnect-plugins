import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import Component, Input, LookupIpInput, LookupIpOutput

# Custom imports below


class LookupIp(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_ip",
            description=Component.DESCRIPTION,
            input=LookupIpInput(),
            output=LookupIpOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        address = params.get(Input.ADDRESS)
        # END INPUT BINDING - DO NOT REMOVE
        self.logger.info(f"Looking up {address}")
        return self.connection.client.lookup(address)
