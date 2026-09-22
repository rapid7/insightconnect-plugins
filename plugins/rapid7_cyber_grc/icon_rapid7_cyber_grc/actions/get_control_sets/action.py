import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetControlSetsInput, GetControlSetsOutput, Input, Output, Component

# Custom imports below


class GetControlSets(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_control_sets",
            description=Component.DESCRIPTION,
            input=GetControlSetsInput(),
            output=GetControlSetsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        filter_ = params.get(Input.FILTER)
        order_by = params.get(Input.ORDER_BY)
        select = params.get(Input.SELECT)
        skip = params.get(Input.SKIP)
        top = params.get(Input.TOP)
        # END INPUT BINDING - DO NOT REMOVE
        records = self.connection.client.list_records(
            "ControlSets", filter_=filter_, select=select, order_by=order_by, top=top, skip=skip
        )

        return {Output.CONTROL_SETS: records, Output.COUNT: len(records)}
