import insightconnect_plugin_runtime
from .schema import CreatePatchGroupAndAddCvesInput, CreatePatchGroupAndAddCvesOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class CreatePatchGroupAndAddCves(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_patch_group_and_add_cves',
                description=Component.DESCRIPTION,
                input=CreatePatchGroupAndAddCvesInput(),
                output=CreatePatchGroupAndAddCvesOutput())

    def run(self, params={}):
        patch_group_payload = {
            "name": params.get(Input.NAME),
            "path": params.get(Input.PATH, None)
        }

        patch_group_details = self.connection.ivanti_api.create_patch_group(patch_group_payload)
        try:
            patch_group_id = patch_group_details['id']
        except KeyError as e:
            raise PluginException(cause=f'"{e}" not found in the API response.',
                                  assistance='If the issue persists please contact support.')

        cve_payload = {
            "cves": params.get(Input.CVES),
        }

        self.connection.ivanti_api.add_cves_to_patch_group(patch_group_id, cve_payload)

        return {
            Output.PATCH_GROUP: patch_group_details
        }
