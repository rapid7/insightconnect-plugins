import insightconnect_plugin_runtime

from .schema import AntivirusScanInput, AntivirusScanOutput, Input, Output, Component


class AntivirusScan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="antivirus_scan",
            description=Component.DESCRIPTION,
            input=AntivirusScanInput(),
            output=AntivirusScanOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        agent = params.get(Input.AGENT)
        # END INPUT BINDING - DO NOT REMOVE

        antivirus_scan = self.connection.client.antivirus_scan(self.connection.client.get_endpoint_id(agent))

        return {
            Output.ID: antivirus_scan.get("id"),
            Output.STATUS: antivirus_scan.get("status"),
            Output.REQUESTED_AT: antivirus_scan.get("requestedAt"),
        }
