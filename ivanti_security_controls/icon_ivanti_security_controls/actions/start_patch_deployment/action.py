import insightconnect_plugin_runtime
from .schema import StartPatchDeploymentInput, StartPatchDeploymentOutput, Input, Output, Component
# Custom imports below
from validators import uuid
from insightconnect_plugin_runtime.exceptions import PluginException


class StartPatchDeployment(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='start_patch_deployment',
                description=Component.DESCRIPTION,
                input=StartPatchDeploymentInput(),
                output=StartPatchDeploymentOutput())

    def run(self, params={}):
        scan_identifier = params.get(Input.SCAN_IDENTIFIER)
        template_identifier = params.get(Input.TEMPLATE_IDENTIFIER)

        if not uuid(scan_identifier):
            scan_identifier = self.get_scan_id(scan_identifier)
        if not uuid(template_identifier):
            template_identifier = self.get_template_id(template_identifier)

        if params.get(Input.DOWNLOAD_PATCHES):
            self.connection.ivanti_api.start_patch_download(scan_identifier)

        payload = {
            'scanId': scan_identifier,
            'templateId': template_identifier
        }

        self.connection.ivanti_api.create_session_credential()
        success = False
        if self.connection.ivanti_api.start_patch_deployment(payload):
            success = True

        return {
            Output.SUCCESS: success
        }

    def get_scan_id(self, scan_name: str) -> str:
        get_response = self.connection.ivanti_api.get_patch_scan_by_name(scan_name)
        if get_response.get('count'):
            return get_response.get('value')[0].get('id')

        raise PluginException(
            cause='Scan not found.',
            assistance=f'Scan: "{scan_name}" doesn\'t exist, please validate the name.'
        )

    def get_template_id(self, template_name: str) -> str:
        get_response = self.connection.ivanti_api.get_patch_deployment_template_by_name(template_name)
        if get_response.get('count'):
            return get_response.get('value')[0].get('id')

        raise PluginException(
            cause='Template not found.',
            assistance=f'Template: "{template_name}" doesn\'t exist, please validate the name.'
        )
