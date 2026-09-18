import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetAssessmentsInput, GetAssessmentsOutput, Input, Output, Component

# Custom imports below


class GetAssessments(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_assessments",
            description=Component.DESCRIPTION,
            input=GetAssessmentsInput(),
            output=GetAssessmentsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        filter = params.get(Input.FILTER)
        order_by = params.get(Input.ORDER_BY)
        select = params.get(Input.SELECT)
        skip = params.get(Input.SKIP)
        top = params.get(Input.TOP)
        # END INPUT BINDING - DO NOT REMOVE
        records = self.connection.client.list_records(
            "Assessments", filter_=filter, select=select, order_by=order_by, top=top, skip=skip
        )

        return {Output.ASSESSMENTS: records, Output.COUNT: len(records)}
