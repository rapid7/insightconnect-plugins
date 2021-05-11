import insightconnect_plugin_runtime
from .schema import AssetSearchInput, AssetSearchOutput, Input, Output, Component


# Custom imports below
from ..start_scan.action import format_body


class AssetSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="asset_search", description=Component.DESCRIPTION, input=AssetSearchInput(), output=AssetSearchOutput()
        )

    def run(self, params={}):
        asset_crit = params.get(Input.ASSET_CRITERIA)
        vuln_crit = params.get(Input.VULN_CRITERIA)
        size = params.get(Input.SIZE, 0)
        sort_criteria = params.get(Input.SORT_CRITERIA, dict())
        parameters = list()

        for key, value in sort_criteria.items():
            parameters.append(("sort", f"{key},{value}"))

        parameters.append(("size", size))
        if asset_crit or vuln_crit:
            hostnames = asset_crit.get("hostnames")
            ips = asset_crit.get("ips")
            body = format_body(hostnames, ips, vuln_crit)
            resources = self.connection.ivm_cloud_api.call_api("assets", "POST", params, body)
        else:
            resources = self.connection.ivm_cloud_api.call_api("assets", "POST", parameters)

        assets = resources.get("data")

        return {Output.ASSETS: assets}
