import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetItAssetsInput, GetItAssetsOutput, Input, Output, Component

# Custom imports below


class GetItAssets(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_it_assets",
            description=Component.DESCRIPTION,
            input=GetItAssetsInput(),
            output=GetItAssetsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        expand = params.get(Input.EXPAND)
        filter = params.get(Input.FILTER)
        order_by = params.get(Input.ORDER_BY)
        select = params.get(Input.SELECT)
        skip = params.get(Input.SKIP)
        top = params.get(Input.TOP)
        # END INPUT BINDING - DO NOT REMOVE
        records = self.connection.client.list_records(
            "ITAssets", filter_=filter, select=select, expand=expand, order_by=order_by, top=top, skip=skip
        )

        return {Output.IT_ASSETS: records, Output.COUNT: len(records)}
