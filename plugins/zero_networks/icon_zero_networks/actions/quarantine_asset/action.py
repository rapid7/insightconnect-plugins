import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import QuarantineAssetInput, QuarantineAssetOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class QuarantineAsset(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine_asset",
            description=Component.DESCRIPTION,
            input=QuarantineAssetInput(),
            output=QuarantineAssetOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        asset_id = params.get(Input.ASSET_ID)
        quarantine = params.get(Input.QUARANTINE)
        # END INPUT BINDING - DO NOT REMOVE

        asset_id = (asset_id or "").strip()
        if not asset_id:
            raise PluginException(
                cause="No asset ID was provided.",
                assistance="Provide the asset ID returned by the Search Asset action, for example a:a:JF2xro6g.",
            )

        self.logger.info(f"Setting quarantine to {quarantine} for asset {asset_id}")
        self.connection.api.set_asset_quarantine(asset_id, quarantine)

        return {Output.SUCCESS: True}
