import insightconnect_plugin_runtime
from .schema import GetPatchDeploymentTemplateIdInput, GetPatchDeploymentTemplateIdOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetPatchDeploymentTemplateId(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_patch_deployment_template_id',
                description=Component.DESCRIPTION,
                input=GetPatchDeploymentTemplateIdInput(),
                output=GetPatchDeploymentTemplateIdOutput())

    def run(self, params={}):
        patch_deployment_template_name = params.get(Input.PATCH_DEPLOYMENT_TEMPLATE_NAME)
        try:
            patch_deployment_template_id = self.connection.ivanti_api.get_patch_deployment_template_by_name(
                patch_deployment_template_name
            )['value'][0]['id']
            return {
                Output.PATCH_DEPLOYMENT_TEMPLATE_ID: patch_deployment_template_id
            }
        except:
            raise PluginException(cause="Not a valid patch deployment template name.",
                                assistance=f"Patch deployment template: {patch_deployment_template_name} doesn't exist."
                                )
