import insightconnect_plugin_runtime
from .schema import DeleteAssetInput, DeleteAssetOutput, Input, Output, Component
# Custom imports below


class DeleteAsset(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_asset',
                description=Component.DESCRIPTION,
                input=DeleteAssetInput(),
                output=DeleteAssetOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
