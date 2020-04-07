import insightconnect_plugin_runtime
from .schema import GetScanConfigInput, GetScanConfigOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import ScanConfig
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
import json


class GetScanConfig(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_scan_config',
                description='Get a scan configuration',
                input=GetScanConfigInput(),
                output=GetScanConfigOutput())

    def run(self, params={}):
        scan_config_id = params.get(Input.SCAN_CONFIG_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = ScanConfig.scan_config(self.connection.url)
        url = f'{url}{scan_config_id}'

        response = request.resource_request(url, 'get')
        try:
            result = json.loads(response['resource'])
        except json.decoder.JSONDecodeError:
            self.logger.error(f'InsightAppSec response: {response}')
            raise Exception('The response from InsightAppSec was not in JSON format. Contact support for help.'
                            ' See log for more details')
        try:
            return {Output.ID: result['id'], Output.CONFIG_NAME: result['name'],
                    Output.CONFIG_DESCRIPTION: result.get('description', ''), Output.APP_ID: result['app']['id'],
                    Output.ATTACK_TEMPLATE_ID: result['attack_template']['id'],
                    Output.ERRORS: result.get('errors', list()), Output.LINKS: result['links']}
        except KeyError:
            self.logger.error(result)
            raise Exception('The response from InsightAppSec was not in the correct format. Contact support for help.'
                            ' See log for more details')
