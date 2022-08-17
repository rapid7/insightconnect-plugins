import insightconnect_plugin_runtime
from .schema import GetAssetsInput, GetAssetsOutput, Input, Output, Component

# Custom imports below


class GetAssets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_assets", description=Component.DESCRIPTION, input=GetAssetsInput(), output=GetAssetsOutput()
        )

    def run(self, params={}):
        score = params.get("state_score")
        parameters = {
            "asset_unique_id": params.get("asset_unique_id"),
            "asset_labels": params.get("asset_labels"),
            "asset_state": params.get("asset_state"),
            "asset_type": params.get("asset_type"),
            "cloud_provider_id": params.get("cloud_provider_id"),
            "compute.regions": params.get("compute_regions"),
            "compute.vpcs": params.get("compute_vpcs"),
            "internet_facing": params.get("internet_facing"),
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
