import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import UpdateItAssetInput, UpdateItAssetOutput, Input, Output, Component

# Custom imports below


class UpdateItAsset(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_it_asset",
            description=Component.DESCRIPTION,
            input=UpdateItAssetInput(),
            output=UpdateItAssetOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        expand = params.get(Input.EXPAND)
        id = params.get(Input.ID)
        record = params.get(Input.RECORD)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.IT_ASSET: self.connection.client.update_record("ITAssets", id, record, expand=expand)}
