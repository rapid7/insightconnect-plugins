import insightconnect_plugin_runtime
from .schema import SubmitScanInput, SubmitScanOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Scans
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper


class SubmitScan(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_scan',
                description='Submit a new scan',
                input=SubmitScanInput(),
                output=SubmitScanOutput())

    def run(self, params={}):
        scan_config_id = params.get(Input.SCAN_CONFIG_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Scans.scans(self.connection.url)
        payload = {'scan_config': {'id': scan_config_id}}

        response = request.resource_request(url, 'post', payload=payload)

        return {Output.STATUS: response['status']}
