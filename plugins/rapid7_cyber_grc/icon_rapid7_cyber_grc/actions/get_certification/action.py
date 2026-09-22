import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetCertificationInput, GetCertificationOutput, Input, Output, Component

# Custom imports below


class GetCertification(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_certification",
            description=Component.DESCRIPTION,
            input=GetCertificationInput(),
            output=GetCertificationOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record_id = params.get(Input.ID)
        select = params.get(Input.SELECT)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.CERTIFICATION: self.connection.client.get_record("Certifications", record_id, select=select)}
