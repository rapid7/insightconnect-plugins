import insightconnect_plugin_runtime
from .schema import UpdatePatchGroupInput, UpdatePatchGroupOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import re


class UpdatePatchGroup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_patch_group',
                description=Component.DESCRIPTION,
                input=UpdatePatchGroupInput(),
                output=UpdatePatchGroupOutput())

    def run(self, params={}):
        vulnerability_identifiers = params.get(Input.VULNERABILITY_IDENTIFIER)
        cves = []
        patch_ids = []
        invalid_identifiers = []

        for identifier in vulnerability_identifiers:
            if identifier.isdigit():
                patch_ids.append(identifier)
                continue
            elif re.match("CVE-\d{4}-\d{4,7}", identifier, re.IGNORECASE):
                cves.append(identifier)
                continue
            else:
                invalid_identifiers.append(identifier)
        
        if invalid_identifiers:
            raise PluginException(
                cause='Invalid vulnerability identifiers provided.',
                assistance=f'Following vulnerabilites are not valid: {str(invalid_identifiers)[1:-1]}.'
            )

        patch_group_id = self.get_patch_group_id(params.get(Input.PATCH_GROUP))
        success = False
        if cves:
            self.connection.ivanti_api.add_cves_to_patch_group(patch_group_id, {"cves": cves})
            success = True
        if patch_ids:
            self.connection.ivanti_api.add_patches_to_patch_group(patch_group_id, patch_ids)
            success = True

        return {
            Output.SUCCESS: success
        }

    def get_patch_group_id(self, patch_group: str) -> str:
        if patch_group.isdigit() and self.check_patch_group_exists(patch_group):
            patch_group_id = patch_group
        else:
            get_patch_group_response = self.connection.ivanti_api.get_patch_group_by_name(patch_group)
            if get_patch_group_response.get('count'):
                patch_group_id = get_patch_group_response.get('value')[0].get('id')

        if patch_group_id:
            return patch_group_id

        raise PluginException(
            cause='Invalid Patch Group provided.',
            assistance=f'Patch group: "{patch_group}" doesn\'t exist.'
        )

    def check_patch_group_exists(self, patch_group: str) -> bool:
        if self.connection.ivanti_api.get_patch_group(patch_group):
            return True
        raise PluginException(
            cause='Invalid Patch Group provided.',
            assistance=f'Patch group: "{patch_group}" doesn\'t exist.'
        )
