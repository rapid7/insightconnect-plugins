import insightconnect_plugin_runtime
from .schema import GetAssetInput, GetAssetOutput, Input, Output, Component
# Custom imports below


class GetAsset(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_asset',
                description=Component.DESCRIPTION,
                input=GetAssetInput(),
                output=GetAssetOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
