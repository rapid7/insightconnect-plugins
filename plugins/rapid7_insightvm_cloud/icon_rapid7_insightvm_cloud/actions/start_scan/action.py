import insightconnect_plugin_runtime
from .schema import StartScanInput, StartScanOutput, Input, Component, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from ipaddress import ip_address, IPv4Address, IPv6Address


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
        if asset_ids is None and ips is None and hostnames is None:
            raise PluginException(
                cause="Did not enter necessary information of what to scan.",
                assistance="Please enter asset ID, hostname, or IP address.",
            )
        if ips or hostnames:
            body = _format_body(hostnames, ips)
            resources = self.connection.ivm_cloud_api.call_api("assets", "POST", params, body)
            extra_ids = resources.get("data", [])
            for extra_id in extra_ids:
                if extra_id.get("id") not in asset_ids:
                    asset_ids.append(extra_id.get("id"))

        body = {"asset_ids": asset_ids, "name": name}

        response = self.connection.ivm_cloud_api.call_api("scan", "POST", None, body)

        try:
            scans = response.get("scans")
            scan_ids = []
            asset_ids = []
            for scan in scans:
                scan_ids.append(scan.get("id"))
                for asset_id in scan.get("asset_ids"):
                    asset_ids.append(asset_id)
            return_data = insightconnect_plugin_runtime.helper.clean(
                {
                    Output.DATA: response,
                    Output.IDS: scan_ids,
                    Output.ASSET_IDS: asset_ids
                }
            )
            return return_data
        except IndexError as error:
            raise PluginException(
                cause=f"Failed to get a valid response from InsightVM for a scan call.",
                assistance=f"Response was {error}.",
                data=str(error),
            )


def _format_body(hostnames: [str], ips: [str]) -> object:
    asset_body = ""
    for hostname in hostnames:
        asset_body = asset_body + "asset.name STARTS WITH '" + hostname + "' || "
    for ip in ips:
        try:
            if type(ip_address(ip)) is IPv4Address:
                asset_body = asset_body + "asset.ipv4 = " + ip + " || "
            if type(ip_address(ip)) is IPv6Address:
                asset_body = asset_body + "asset.ipv6 = " + ip + " || "
        except ValueError as error:
            raise PluginException(
                cause="Invalid IP address provided.",
                assistance="Please enter only valid IP addresses.",
                data=str(error)
            )
    if asset_body[len(asset_body) - 2] == "|":
        asset_body = asset_body[: len(asset_body) - 4]
    body_object = {"asset": asset_body}
    return body_object
