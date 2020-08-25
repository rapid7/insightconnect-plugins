import insightconnect_plugin_runtime
from .schema import StopAndQuarantineFileInput, StopAndQuarantineFileOutput, Input, Output, Component
# Custom imports below


class StopAndQuarantineFile(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='stop_and_quarantine_file',
                description=Component.DESCRIPTION,
                input=StopAndQuarantineFileInput(),
                output=StopAndQuarantineFileOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get("id")
        sha1_id = params.get(Input.SHA1)
        comment = params.get(Input.COMMENT)

        self.logger.info("Attempting to stop and quarantine file: " + sha1_id)
        self.logger.info("Attempting to stop and quarantine file on machine: " + machine_id)
        response = self.connection.client.stop_and_quarantine_file(machine_id, sha1_id, comment)
        return {Output.STOP_AND_QUARANTINE_RESPONSE: insightconnect_plugin_runtime.helper.clean(response)}
