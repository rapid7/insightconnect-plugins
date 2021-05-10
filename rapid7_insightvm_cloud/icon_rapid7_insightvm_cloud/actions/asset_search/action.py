import ast

import insightconnect_plugin_runtime
from .schema import AssetSearchInput, AssetSearchOutput, Input, Output, Component


# Custom imports below


class AssetSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="asset_search", description=Component.DESCRIPTION, input=AssetSearchInput(), output=AssetSearchOutput()
        )

    def run(self, params={}):
        results = list()
        ips = params.get(Input.IPS)
        hostnames = params.get(Input.HOSTNAMES)
        size = params.get(Input.SIZE, 0)
        sort_criteria = params.get(Input.SORT_CRITERIA, dict())
        parameters = list()

        for key, value in sort_criteria.items():
            parameters.append(("sort", f"{key},{value}"))

        parameters.append(("size", size))
        resources = self.connection.ivm_cloud_api.call_api("assets", "POST", parameters)

        assets = resources.get("data")
        for asset in assets:
            if hostnames:
                if asset.get("host_name") in hostnames:
                    results.append(asset)
            if ips:
                if asset.get("ip") in ips:
                    results.append(asset)
            if hostnames == [] and ips == []:
                results.append(asset)

        return {Output.ASSETS: results}
