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
        name = params.get(Input.PATCH_DEPLOYMENT_TEMPLATE_NAME)
        patch_deployment_template = self.connection.ivanti_api.get_patch_deployment_template_by_name(name)

        if patch_deployment_template.get('count'):
            template_id = patch_deployment_template.get('value')[0].get('id')
            return {
                Output.PATCH_DEPLOYMENT_TEMPLATE_ID: template_id
            }
            
        raise PluginException(
            cause="Invalid patch deployment template name provided.",
            assistance=f"Patch deployment template: {name} doesn't exist."
        )
