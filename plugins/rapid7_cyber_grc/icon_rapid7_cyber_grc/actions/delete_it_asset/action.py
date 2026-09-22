import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import DeleteItAssetInput, DeleteItAssetOutput, Input, Output, Component

# Custom imports below


class DeleteItAsset(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_it_asset",
            description=Component.DESCRIPTION,
            input=DeleteItAssetInput(),
            output=DeleteItAssetOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record_id = params.get(Input.ID)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.RESULT: self.connection.client.delete_record("ITAssets", record_id)}
