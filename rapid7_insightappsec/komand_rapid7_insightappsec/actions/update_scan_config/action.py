import komand
from .schema import UpdateScanConfigInput, UpdateScanConfigOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import ScanConfig
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper


class UpdateScanConfig(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_scan_config',
                description='Update an existing scan configuration',
                input=UpdateScanConfigInput(),
                output=UpdateScanConfigOutput())

    def run(self, params={}):
        scan_config_id = params.get(Input.SCAN_CONFIG_ID)
        config_name = params.get(Input.CONFIG_NAME)
        config_description = params.get(Input.CONFIG_DESCRIPTION)
        app_id = params.get(Input.APP_ID)
        attack_template_id = params.get(Input.ATTACK_TEMPLATE_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = ScanConfig.scan_config(self.connection.url)
        url = f'{url}{scan_config_id}'
        payload = {'name': config_name, 'description': config_description,
                   'app': {'id': app_id}, 'attack_template': {'id': attack_template_id}}

        response = request.resource_request(url, 'put', payload=payload)

        return {Output.STATUS: response['status']}
