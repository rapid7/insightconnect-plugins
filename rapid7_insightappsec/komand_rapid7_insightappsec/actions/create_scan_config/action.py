import insightconnect_plugin_runtime
from .schema import CreateScanConfigInput, CreateScanConfigOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import ScanConfig
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json

class CreateScanConfig(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_scan_config',
                description='Create a new scan configuration',
                input=CreateScanConfigInput(),
                output=CreateScanConfigOutput())

    def run(self, params={}):
        config_name = params.get(Input.CONFIG_NAME)
        config_description = params.get(Input.CONFIG_DESCRIPTION)
        app_id = params.get(Input.APP_ID)
        attack_template_id = params.get(Input.ATTACK_TEMPLATE_ID)
        assignment_environment = params.get(Input.ASSIGNMENT_ENVIRONMENT)
        assignment_id = params.get(Input.ASSIGNMENT_ID)
        assignment_type = params.get(Input.ASSIGNMENT_TYPE)
        request = ResourceHelper(self.connection.session, self.logger)

        url = ScanConfig.scan_config(self.connection.url)
        payload = {'name': config_name, 'description': config_description,
                   'app': {'id': app_id}, 'attack_template': {'id': attack_template_id},
                   'assignment': {'environment': assignment_environment, 'type': assignment_type}}
        try:
            response = request.resource_request(url, 'post', payload=payload)

        except (json.decoder.JSONDecodeError, TypeError, KeyError):
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause='The response from InsightAppSec was not in JSON format.', assistance='Contact support for help.'
                            ' See log for more details')

        uuid = response.get("headers")
        uuid = uuid.get("Location")
        parts = uuid.split('/')
        scan_config_id = parts[-1]
        return {Output.SCAN_CONFIG_ID:scan_config_id}
