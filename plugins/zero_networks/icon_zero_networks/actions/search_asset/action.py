import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import SearchAssetInput, SearchAssetOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SearchAsset(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_asset",
            description=Component.DESCRIPTION,
            input=SearchAssetInput(),
            output=SearchAssetOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        fqdn = params.get(Input.FQDN)
        # END INPUT BINDING - DO NOT REMOVE

        fqdn = (fqdn or "").strip()
        if not fqdn:
            raise PluginException(
                cause="No fully qualified domain name was provided.",
                assistance="Provide the FQDN of the asset to search for, for example server.domain.local.",
            )

        asset_id = self.connection.api.search_asset_id(fqdn)
        if not asset_id:
            self.logger.info(f"No asset matched the FQDN {fqdn}")
            return {Output.FOUND: False, Output.ASSET_ID: ""}

        return {Output.FOUND: True, Output.ASSET_ID: asset_id}
