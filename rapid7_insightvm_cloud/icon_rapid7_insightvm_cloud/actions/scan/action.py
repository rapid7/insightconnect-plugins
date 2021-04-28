import ast

import insightconnect_plugin_runtime
from .schema import ScanInput, ScanOutput, Input, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Scan(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='scan',
            description=Component.DESCRIPTION,
            input=ScanInput(),
            output=ScanOutput())

    def asset_search(self, hostname: str, ip: str):
        parameters = list()
        parameters.append(("size", 50))
        resources = self.connection.ivm_cloud_api.call_api_pages("assets", "POST", parameters)

        results = list()
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
                            if asset["id"] not in results:
                                results.append(asset["id"])
                elif ip != "":
                    if "ip" in asset:
                        if ip == asset["ip"]:
                            if asset["id"] not in results:
                                results.append(asset["id"])
        return results

    def run(self, params={}):
        asset_ids = params.get(Input.ASSET_IDS)
        name = params.get(Input.NAME)
        ip = params.get(Input.IP)
        hostname = params.get(Input.HOSTNAME)
        if asset_ids == [] and ip == "" and hostname == "":
            raise PluginException(
                cause="Did not enter necessary information of what to scan.",
                assistance="Please enter asset id, hostname, or ip."
            )
        if hostname != "" or ip != "":
            extra_ids = self.asset_search(hostname, ip)
            for extra_id in range(len(extra_ids)):
                asset_ids.append(extra_ids[extra_id])

        body = {"asset_ids": asset_ids, "name": name}

        response = self.connection.ivm_cloud_api.call_api("scan", "POST", None, body)

        return response
