import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import UpdateVendorInput, UpdateVendorOutput, Input, Output, Component

# Custom imports below


class UpdateVendor(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_vendor",
            description=Component.DESCRIPTION,
            input=UpdateVendorInput(),
            output=UpdateVendorOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record_id = params.get(Input.ID)
        record = params.get(Input.RECORD)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.VENDOR: self.connection.client.update_record("Vendors", record_id, record)}
