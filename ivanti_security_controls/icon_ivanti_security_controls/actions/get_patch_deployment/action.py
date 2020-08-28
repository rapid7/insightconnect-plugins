import insightconnect_plugin_runtime
from .schema import GetPatchDeploymentInput, GetPatchDeploymentOutput, Input, Output, Component
# Custom imports below


class GetPatchDeployment(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_patch_deployment',
                description=Component.DESCRIPTION,
                input=GetPatchDeploymentInput(),
                output=GetPatchDeploymentOutput())

    def run(self, params={}):
        patch_deployment = self.connection.ivanti_api.get_patch_deployment(params.get(Input.DEPLOYMENT_ID))

        if params.get(Input.MACHINE_ID):
            machine_info = self.connection.ivanti_api.get_patch_deployment_machine(params.get(Input.DEPLOYMENT_ID), params.get(Input.MACHINE_ID))
        else:
            machine_info = self.connection.ivanti_api.get_patch_deployment_machines(params.get(Input.DEPLOYMENT_ID)) 

        return {
            Output.PATCH_DEPLOYMENT_DETAILS: patch_deployment,
            Output.MACHINE_INFORMATION: machine_info
        }
