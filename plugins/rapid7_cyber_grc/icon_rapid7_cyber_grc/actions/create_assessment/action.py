import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CreateAssessmentInput, CreateAssessmentOutput, Input, Output, Component

# Custom imports below


class CreateAssessment(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_assessment",
            description=Component.DESCRIPTION,
            input=CreateAssessmentInput(),
            output=CreateAssessmentOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record = params.get(Input.RECORD)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.ASSESSMENT: self.connection.client.create_record("Assessments", record)}
