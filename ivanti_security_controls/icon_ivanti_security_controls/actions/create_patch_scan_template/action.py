import insightconnect_plugin_runtime
from .schema import CreatePatchScanTemplateInput, CreatePatchScanTemplateOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class CreatePatchScanTemplate(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_patch_scan_template',
                description=Component.DESCRIPTION,
                input=CreatePatchScanTemplateInput(),
                output=CreatePatchScanTemplateOutput())

    def run(self, params={}):
        payload = {
            "description": params.get(Input.DESCRIPTION, None),
            "name": params.get(Input.NAME),
            "patchFilter": {
                "patchGroupFilterType": "Scan",
                "patchGroupIds": params.get(Input.PATCHGROUPIDS)
            },
            "path": params.get(Input.PATH, None),
            "threadCount": params.get(Input.THREADCOUNT, None)
        }
        try:
            template_id = self.connection.ivanti_api.create_patch_scan_template(payload)['id']
        except KeyError as e:
            raise PluginException(cause=f'"{e}" not found in the API response.',
                                  assistance='If the issue persists please contact support.')

        return {
            Output.PATCH_SCAN_TEMPLATE: self.connection.ivanti_api.get_patch_scan_template(template_id)
        }
