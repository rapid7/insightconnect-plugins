import ast

import insightconnect_plugin_runtime
from .schema import AssetSearchInput, AssetSearchOutput, Input, Output, Component


# Custom imports below


def format_response(resources: [], params={}):
    assets = list()
    ip = params.get(Input.IP)
    hostname = params.get(Input.HOSTNAME)
    for page in range(len(resources)):
        current = str(resources[page])
        asset = current.split("]},")
        for num in range(len(asset)):
            curr = asset[num]
            if num == 0:
                curr = curr[11:] + "]"
            else:
                curr = curr[2:] + "]"
            if num == len(asset) - 1:
                ending = curr.split("], 'metadata':")
                curr = ending[0]
                if curr[len(curr) - 1] == "}":
                    curr = curr[:len(curr) - 1]
            curr = "{" + curr + "}"
            curr = ast.literal_eval(curr)
            if hostname != "":
                if "host_name" in curr:
                    if hostname == curr["host_name"]:
                        assets.append(curr)
            elif ip != "":
                if "ip" in curr:
                    if ip == curr["ip"]:
                        assets.append(curr)
            elif hostname == "" and ip == "":
                assets.append(curr)
    return assets


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
