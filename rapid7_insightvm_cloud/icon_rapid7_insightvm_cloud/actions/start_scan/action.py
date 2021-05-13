import insightconnect_plugin_runtime
from .schema import StartScanInput, StartScanOutput, Input, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from ipaddress import ip_address, IPv4Address, IPv6Address


def format_body(hostnames: [], ips: []):
    asset_body = ""
    for hostname in hostnames:
        asset_body = asset_body + "asset.name STARTS WITH '" + hostname + "' || "
    for ip in ips:
        if type(ip_address(ip)) is IPv4Address:
            asset_body = asset_body + "asset.ipv4 = " + ip + " || "
        if type(ip_address(ip)) is IPv6Address:
            asset_body = asset_body + "asset.ipv6 = " + ip + " || "
    if asset_body[len(asset_body) - 2] == "|":
        asset_body = asset_body[: len(asset_body) - 4]
    body_object = {"asset": asset_body}
    return body_object


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
        if asset_ids == [] and ips == [] and hostnames == []:
            raise PluginException(
                cause="Did not enter necessary information of what to scan.",
                assistance="Please enter asset id, hostname, or ip.",
            )
        if ips or hostnames:
            body = format_body(hostnames, ips)
            resources = self.connection.ivm_cloud_api.call_api("assets", "POST", params, body)
            extra_ids = resources.get("data")
            for extra_id in extra_ids:
                if extra_id.get("id") not in asset_ids:
                    asset_ids.append(extra_id.get("id"))

        body = {"asset_ids": asset_ids, "name": name}

        response = self.connection.ivm_cloud_api.call_api("scan", "POST", None, body)

        return response
