import komand
from .schema import AddScanResultInput, AddScanResultOutput
# Custom imports below
from ...util.utils import generate_payload


class AddScanResult(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_scan_result',
                description='Add a scan result from a third-party vulnerability scanner',
                input=AddScanResultInput(),
                output=AddScanResultOutput())

    def run(self, params={}):
        scan_result = params.get('scan_result', {})
        operation = params.get('operation', '')
        max_page_size = self.connection.max_data_size

        # Generate the data to send
        payload = generate_payload([scan_result], operation, max_page_size)

        self.logger.info('Sending payload to Firepower.')
        processed, errors = self.connection.send(payload)

        return {
            "errors": errors,
            "commands_processed": processed
        }

    def test(self):
        return self.connection.test_connection()
