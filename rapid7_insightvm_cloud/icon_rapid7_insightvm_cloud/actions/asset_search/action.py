import ast

import insightconnect_plugin_runtime
from .schema import AssetSearchInput, AssetSearchOutput, Input, Output, Component


# Custom imports below


def format_response(resources: [], params={}):
    results = list()
    ip = params.get(Input.IPS)
    hostname = params.get(Input.HOSTNAMES)

    string_page = str(resources)
    assets = string_page.split("]},")
    for asset_number in range(len(assets)):
        asset = assets[asset_number]
        if asset_number == 0:
            asset = asset[11:] + "]"
        else:
            asset = asset[2:] + "]"
        if asset_number == len(assets) - 1:
            ending = asset.split("], 'metadata':")
            asset = ending[0]
            if asset[len(asset) - 1] == "}":
                asset = asset[: len(asset) - 1]
        asset = "{" + asset + "}"
        asset = ast.literal_eval(asset)
        if hostname:
            if asset.get("host_name") in hostname:
                results.append(asset)
        if ip:
            if asset.get("ip") in ip:
                results.append(asset)
        if hostname == [] and ip == []:
            results.append(asset)
    return results


class AssetSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="asset_search", description=Component.DESCRIPTION, input=AssetSearchInput(), output=AssetSearchOutput()
        )

    def run(self, params={}):
        size = params.get(Input.SIZE, 0)
        sort_criteria = params.get(Input.SORT_CRITERIA, dict())
        parameters = list()

        for key, value in sort_criteria.items():
            parameters.append(("sort", f"{key},{value}"))

        resources = self.connection.ivm_cloud_api.call_api("assets", "POST", parameters)

        assets = []
        for asset in resources:
            assets.append(asset)

        return {Output.ASSETS: assets}
