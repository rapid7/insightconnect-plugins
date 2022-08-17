import insightconnect_plugin_runtime
from .schema import GetAssetByIdInput, GetAssetByIdOutput, Input, Output, Component

# Custom imports below


class GetAssetById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset_by_id",
            description=Component.DESCRIPTION,
            input=GetAssetByIdInput(),
            output=GetAssetByIdOutput(),
        )

    def run(self, params={}):
        return {Output.ASSET: self.connection.api.get_asset_by_id(params.get(Input.ASSET_UNIQUE_ID))}
