import insightconnect_plugin_runtime
from .schema import VpnStatusInput, VpnStatusOutput, Component, Output


class VpnStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="vpn_status",
            description=Component.DESCRIPTION,
            input=VpnStatusInput(),
            output=VpnStatusOutput(),
        )

    def run(self, params={}):
        endpoint = "vpn/status"
        response = self.connection.api.send(endpoint)
        vpns = response.get("vpns", [])
        vpn_list = []
        for vpn, running_status in vpns.items():
            status = "Running" if running_status else "Not running"
            vpn_list.append({"name": vpn, "status": status})
        return {Output.VPNS: vpn_list}
