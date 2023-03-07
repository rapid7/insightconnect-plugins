from typing import Dict, Any

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import AssetSearchInput, AssetSearchOutput, Input, Output, Component


class AssetSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="asset_search", description=Component.DESCRIPTION, input=AssetSearchInput(), output=AssetSearchOutput()
        )

    def run(self, params={}):
        body = clean(
            {"asset": params.pop(Input.ASSET_CRITERIA, None), "vulnerability": params.pop(Input.VULN_CRITERIA, None)}
        )
        parameters = {
            Input.SIZE: self._get_size(params),
            "currentTime": params.get(Input.CURRENT_TIME),
            "comparisonTime": params.get(Input.COMPARISON_TIME),
        }
        for key, value in params.get("sort_criteria", {}).items():
            parameters["sort"] = f"{key},{value}"

        parameters = clean(parameters)
        resources = self.connection.ivm_cloud_api.call_api("assets", "POST", parameters, body)

        assets = resources.get("data", [])
        return {Output.ASSETS: assets}

    def _get_size(self, params: Dict[str, Any]) -> int:
        size = params.get(Input.SIZE, 200)
        if size > 500:
            self.logger.info(f"'{size}' too large, set to max size of 500.")
            size = 500
        return size
