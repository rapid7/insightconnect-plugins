import komand
from .schema import DeleteScanConfigInput, DeleteScanConfigOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import ScanConfig
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper


class DeleteScanConfig(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_scan_config',
                description='Delete an existing scan configuration',
                input=DeleteScanConfigInput(),
                output=DeleteScanConfigOutput())

    def run(self, params={}):
        scan_config_id = params.get(Input.SCAN_CONFIG_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = ScanConfig.scan_config(self.connection.url)
        url = f'{url}{scan_config_id}'

        response = request.resource_request(url, 'delete')
        return {Output.STATUS: response['status']}
