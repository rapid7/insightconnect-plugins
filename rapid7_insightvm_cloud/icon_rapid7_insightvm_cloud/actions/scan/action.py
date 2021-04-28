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

        assets = list()
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
                            if curr["id"] not in assets:
                                assets.append(curr["id"])
                elif ip != "":
                    if "ip" in curr:
                        if ip == curr["ip"]:
                            if curr["id"] not in assets:
                                assets.append(curr["id"])
        return assets

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
            for num in range(len(extra_ids)):
                asset_ids.append(extra_ids[num])

        body = {"asset_ids": asset_ids, "name": name}

        response = self.connection.ivm_cloud_api.call_api("scan", "POST", None, body)

        return response
