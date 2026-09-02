import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CreateItAssetInput, CreateItAssetOutput, Input, Output, Component

# Custom imports below


class CreateItAsset(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_it_asset",
            description=Component.DESCRIPTION,
            input=CreateItAssetInput(),
            output=CreateItAssetOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        expand = params.get(Input.EXPAND)
        record = params.get(Input.RECORD)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.IT_ASSET: self.connection.client.create_record("ITAssets", record, expand=expand)}
