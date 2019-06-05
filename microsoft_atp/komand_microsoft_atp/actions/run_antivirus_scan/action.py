import komand
from .schema import RunAntivirusScanInput, RunAntivirusScanOutput
# Custom imports below


class RunAntivirusScan(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_antivirus_scan',
                description='Initiate a Windows Defender Antivirus scan on a machine',
                input=RunAntivirusScanInput(),
                output=RunAntivirusScanOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = params.get("machine_id")
        scan_type = params.get("scan_type")
        comment = params.get("comment")

        self.logger.info("Attempting to run a " + scan_type + " antivirus scan on machine id: " + machine_id)
        response = self.connection.run_antivirus_scan(machine_id, scan_type, comment)
        return {"machine_action_response": komand.helper.clean(response)}
