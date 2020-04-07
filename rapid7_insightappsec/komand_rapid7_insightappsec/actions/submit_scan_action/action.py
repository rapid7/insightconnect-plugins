import insightconnect_plugin_runtime
from .schema import SubmitScanActionInput, SubmitScanActionOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Scans
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper


class SubmitScanAction(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_scan_action',
                description='Submit a new scan action',
                input=SubmitScanActionInput(),
                output=SubmitScanActionOutput())

    def run(self, params={}):
        scan_id = params.get(Input.SCAN_ID)
        action = params.get(Input.ACTION)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Scans.scan_action(self.connection.url, scan_id)
        payload = {'action': action.upper()}

        response = request.resource_request(url, 'put', payload=payload)

        return {Output.STATUS: response['status']}
