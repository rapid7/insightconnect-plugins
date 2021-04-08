import insightconnect_plugin_runtime
from .schema import AssetSearchInput, AssetSearchOutput, Input, Output, Component
# Custom imports below


class AssetSearch(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='asset_search',
                description=Component.DESCRIPTION,
                input=AssetSearchInput(),
                output=AssetSearchOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
