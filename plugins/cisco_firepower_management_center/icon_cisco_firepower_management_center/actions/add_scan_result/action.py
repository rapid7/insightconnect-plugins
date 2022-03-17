import insightconnect_plugin_runtime
from .schema import AddScanResultInput, AddScanResultOutput, Input, Output, Component

# Custom imports below
from ...util.utils import generate_payload


class AddScanResult(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_scan_result",
            description=Component.DESCRIPTION,
            input=AddScanResultInput(),
            output=AddScanResultOutput(),
        )

    def run(self, params={}):
        scan_result = params.get(Input.SCAN_RESULT, {})
        operation = params.get(Input.OPERATION, "")

        self.logger.info("Sending payload to Firepower.")
        processed, errors = self.connection.cisco_firepower_host_input.send(
            generate_payload([scan_result], operation, self.connection.cisco_firepower_host_input.max_data_size)
        )

        return {Output.ERRORS: errors, Output.COMMANDS_PROCESSED: processed}
