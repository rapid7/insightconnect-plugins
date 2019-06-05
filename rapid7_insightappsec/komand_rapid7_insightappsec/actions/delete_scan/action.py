import komand
from .schema import DeleteScanInput, DeleteScanOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Scans
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper


class DeleteScan(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_scan',
                description='Delete a scan',
                input=DeleteScanInput(),
                output=DeleteScanOutput())

    def run(self, params={}):
        scan_id = params.get(Input.SCAN_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Scans.scans(self.connection.url)
        url = f'{url}{scan_id}'

        response = request.resource_request(url, 'delete')
        return {Output.STATUS: response['status']}
