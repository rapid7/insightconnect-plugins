import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetVendorInput, GetVendorOutput, Input, Output, Component

# Custom imports below


class GetVendor(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_vendor", description=Component.DESCRIPTION, input=GetVendorInput(), output=GetVendorOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        expand = params.get(Input.EXPAND)
        id = params.get(Input.ID)
        select = params.get(Input.SELECT)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.VENDOR: self.connection.client.get_record("Vendors", id, select=select, expand=expand)}
