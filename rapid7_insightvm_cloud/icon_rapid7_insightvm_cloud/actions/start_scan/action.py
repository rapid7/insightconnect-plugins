import insightconnect_plugin_runtime
from .schema import StartScanInput, StartScanOutput, Input, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class StartScan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="start_scan", description=Component.DESCRIPTION, input=StartScanInput(), output=StartScanOutput()
        )

    def run(self, params={}):
        asset_ids = params.get(Input.ASSET_IDS)
        name = params.get(Input.NAME)
        ips = params.get(Input.IPS)
        hostnames = params.get(Input.HOSTNAMES)
        resources = self.connection.ivm_cloud_api.call_api("assets", "POST", params)
        if asset_ids == [] and ips == [] and hostnames == []:
            raise PluginException(
                cause="Did not enter necessary information of what to scan.",
                assistance="Please enter asset id, hostname, or ip.",
            )
        if hostnames != [] or ips != []:
            extra_ids = resources.get("data")
            for extra_id in extra_ids:
                if hostnames:
                    if extra_id.get("host_name") in hostnames:
                        if extra_id.get("id") not in asset_ids:
                            asset_ids.append(extra_id.get("id"))
                if ips:
                    if extra_id.get("ip") in ips:
                        if extra_id.get("id") not in asset_ids:
                            asset_ids.append(extra_id.get("id"))

        body = {"asset_ids": asset_ids, "name": name}

        response = self.connection.ivm_cloud_api.call_api("scan", "POST", None, body)

        return response
