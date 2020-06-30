import insightconnect_plugin_runtime
from .schema import StartPatchDeploymentInput, StartPatchDeploymentOutput, Input, Output, Component
# Custom imports below


class StartPatchDeployment(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='start_patch_deployment',
                description=Component.DESCRIPTION,
                input=StartPatchDeploymentInput(),
                output=StartPatchDeploymentOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
