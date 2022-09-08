import insightconnect_plugin_runtime
from .schema import GetAssetsInput, GetAssetsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetAssets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_assets", description=Component.DESCRIPTION, input=GetAssetsInput(), output=GetAssetsOutput()
        )

    def run(self, params={}):
        score = params.get("state_score")
        internet_facing = params.get("internet_facing").lower()
        if internet_facing and internet_facing not in ["true", "false"]:
            raise PluginException(
                cause=f"Invalid value '{internet_facing}' has been provided for the Internet Facing input.",
                assistance="Acceptable values for this input are 'true' or 'false'.",
            )
        parameters = {
            "asset_unique_id": params.get("asset_unique_id"),
            "asset_labels": params.get("asset_labels"),
            "asset_state": params.get("asset_state"),
            "asset_type": params.get("asset_type"),
            "cloud_provider_id": params.get("cloud_provider_id"),
            "compute.regions": params.get("compute_regions"),
            "compute.vpcs": params.get("compute_vpcs"),
            "internet_facing": internet_facing,
            "state.score": score if score else "",
            "state.severity": params.get("state_severity"),
        }
        response = self.connection.api.get_assets(insightconnect_plugin_runtime.helper.clean_dict(parameters))
        return {
            Output.ASSETS: response.get("data", []),
            Output.TOTAL_ITEMS: response.get("total_items", 0),
            Output.TOTAL_UNGROUPED_ITEMS: response.get("total_ungrouped_items", 0),
            Output.TOTAL_SUPPORTED_ITEMS: int(response.get("total_supported_items", 0)),
        }
