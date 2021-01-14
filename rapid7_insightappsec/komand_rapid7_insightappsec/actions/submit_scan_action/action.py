import insightconnect_plugin_runtime
from .schema import SubmitScanActionInput, SubmitScanActionOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Scans
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json


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

        try:
            response = request.resource_request(url, 'put', payload=payload)

        except (json.decoder.JSONDecodeError, TypeError, KeyError):
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause='The response from InsightAppSec was not in JSON format.', assistance='Contact support for help.'
                                        ' See log for more details')

        return {Output.STATUS: response['status']}
