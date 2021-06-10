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
        include_vulns = params.get(Input.INCLUDE_VULNS)
        if include_vulns:
            params = {"includeSame": True}
            response = self.connection.ivm_cloud_api.call_api("assets/" + asset_id, "GET", params)
            return {Output.ASSET: response, Output.VULNERABILITIES: response.get("same")}
        else:
            response = self.connection.ivm_cloud_api.call_api("assets/" + asset_id, "GET")
            return {Output.ASSET: response}
