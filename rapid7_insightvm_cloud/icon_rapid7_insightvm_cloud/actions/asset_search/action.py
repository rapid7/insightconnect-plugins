import ast

import insightconnect_plugin_runtime
from .schema import AssetSearchInput, AssetSearchOutput, Input, Output, Component


# Custom imports below


def format_response(resources: [], params={}):
    results = list()
    ip = params.get(Input.IP)
    hostname = params.get(Input.HOSTNAME)
    for page in resources:
        string_page = str(page)
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
                    asset = asset[:len(asset) - 1]
            asset = "{" + asset + "}"
            asset = ast.literal_eval(asset)
            if hostname != "":
                if "host_name" in asset:
                    if hostname == asset["host_name"]:
                        results.append(asset)
            elif ip != "":
                if "ip" in asset:
                    if ip == asset["ip"]:
                        results.append(asset)
            elif hostname == "" and ip == "":
                results.append(asset)
    return results


class AssetSearch(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='asset_search',
            description=Component.DESCRIPTION,
            input=AssetSearchInput(),
            output=AssetSearchOutput())

    def run(self, params={}):
        size = params.get(Input.SIZE, 0)
        sort_criteria = params.get(Input.SORT_CRITERIA, dict())
        parameters = list()

        for key, value in sort_criteria.items():
            parameters.append(("sort", f"{key},{value}"))

        if size == 0:
            parameters.append(("size", 100))
            resources = self.connection.ivm_cloud_api.call_api_pages("assets", "POST", parameters)
        elif size <= 100:
            parameters.append(("size", size))
            resources = self.connection.ivm_cloud_api.call_api_pages("assets", "POST", parameters)
        else:
            parameters.append(("size", 100))
            resources = self.connection.ivm_cloud_api.call_api_pages("assets", "POST", parameters)

        assets = format_response(resources, params)

        return {Output.ASSETS: assets}
