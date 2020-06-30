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
        patch_group_ids = params.get(Input.PATCHGROUPIDS)

        self.valdate_patch_group_ids(patch_group_ids)

        payload = {
            "description": params.get(Input.DESCRIPTION, None),
            "name": params.get(Input.NAME),
            "patchFilter": {
                "patchGroupFilterType": "Scan",
                "patchGroupIds": patch_group_ids
            },
            "path": params.get(Input.PATH, None),
            "threadCount": params.get(Input.THREADCOUNT, None)
        }

        template_id = self.connection.ivanti_api.create_patch_scan_template(payload).get('id')
        if template_id:
            return {
                Output.PATCH_SCAN_TEMPLATE: self.connection.ivanti_api.get_patch_scan_template(template_id)
            }
        
        raise PluginException(
            cause='Invalid API response.',
            assistance='If the issue persists please contact support.'
        )

    def valdate_patch_group_ids(self, patch_group_ids: list):
        invalid_ids = []
        for patch_group_id in patch_group_ids:
            if not self.connection.ivanti_api.get_patch_group(patch_group_id):
                invalid_ids.append(patch_group_id)
        if len(invalid_ids) >= 1:
            raise PluginException(
                cause='Invalid Patch Group ID provided.',
                assistance=f'Following Patch Group IDs do not exist: {str(invalid_ids)[1:-1]}.'
            )
        return
