import insightconnect_plugin_runtime
from .schema import GetAssetInput, GetAssetOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import requests


class GetAsset(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset",
            description=Component.DESCRIPTION,
            input=GetAssetInput(),
            output=GetAssetOutput(),
        )

    def run(self, params={}):
        asset_id = params.get(Input.ID)

        try:
            response = self.connection.ivm_cloud_api.call_api("assets/" + asset_id, "GET")
            return {Output.ASSET: response[1]}
        except requests.RequestException as e:
            self.logger.error(e)
            raise PluginException(
                cause=f"Failed to get a valid response from InsightVM with given asset ID '{asset_id}'.",
                assistance=f"Response was {response[1].request.body}",
                data=response[1].status_code,
            )
