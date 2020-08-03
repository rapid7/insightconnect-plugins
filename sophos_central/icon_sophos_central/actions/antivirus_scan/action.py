import insightconnect_plugin_runtime
from .schema import AntivirusScanInput, AntivirusScanOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AntivirusScan(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='antivirus_scan',
                description=Component.DESCRIPTION,
                input=AntivirusScanInput(),
                output=AntivirusScanOutput())

    def run(self, params={}):
        uuid = None
        page_key = None
        agent = params.get(Input.AGENT)

        for index in range(9999):
            endpoints = self.connection.client.get_endpoints(page_key=page_key)
            page_key = endpoints.get("pages", {}).get("nextKey", None)

            for e in endpoints.get("items", []):
                if e.get("hostname") == agent:
                    uuid = e.get("id")
                elif e.get("id") == agent:
                    uuid = e.get("id")
                elif agent in e.get("ipv4Addresses"):
                    uuid = e.get("id")
                elif agent in e.get("macAddresses"):
                    uuid = e.get("id")
                elif agent in e.get("ipv6Addresses"):
                    uuid = e.get("id")

            if page_key is None or index > endpoints.get("pages", {}).get("total", 0):
                break

        if uuid is None:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)

        antivirus_scan = self.connection.client.antivirus_scan(uuid)

        return {
            Output.ID: antivirus_scan.get("id"),
            Output.STATUS: antivirus_scan.get("status"),
            Output.REQUESTED_AT: antivirus_scan.get("requestedAt")
        }
