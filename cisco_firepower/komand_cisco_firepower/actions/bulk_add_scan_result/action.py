import komand
from .schema import BulkAddScanResultInput, BulkAddScanResultOutput
# Custom imports below
from ...util.utils import generate_payload


class BulkAddScanResult(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='bulk_add_scan_result',
                description='Add scan results from a third-party vulnerability scanner',
                input=BulkAddScanResultInput(),
                output=BulkAddScanResultOutput())

    def run(self, params={}):
        scan_results = params.get('scan_results', [])
        operation = params.get('operation', '')
        max_page_size = self.connection.max_data_size

        # Generate the data to send
        payload = generate_payload(scan_results, operation, max_page_size)

        self.logger.info('Sending payload to Firepower.')
        processed, errors = self.connection.send(payload)

        return {
            "errors": errors,
            "commands_processed": processed
        }

    def test(self):
        return self.connection.test_connection()
