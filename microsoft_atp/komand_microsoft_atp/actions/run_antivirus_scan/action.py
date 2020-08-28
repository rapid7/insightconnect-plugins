import insightconnect_plugin_runtime
from .schema import RunAntivirusScanInput, RunAntivirusScanOutput, Input, Output, Component
# Custom imports below


class RunAntivirusScan(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_antivirus_scan',
                description=Component.DESCRIPTION,
                input=RunAntivirusScanInput(),
                output=RunAntivirusScanOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get("id")
        scan_type = params.get(Input.SCAN_TYPE)
        comment = params.get(Input.COMMENT)

        self.logger.info("Attempting to run a " + scan_type + " antivirus scan on machine id: " + machine_id)
        response = self.connection.client.run_antivirus_scan(machine_id, scan_type, comment)
        return {Output.MACHINE_ACTION_RESPONSE: insightconnect_plugin_runtime.helper.clean(response)}
