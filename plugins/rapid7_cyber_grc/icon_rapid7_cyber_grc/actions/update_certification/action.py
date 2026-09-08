import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import UpdateCertificationInput, UpdateCertificationOutput, Input, Output, Component

# Custom imports below


class UpdateCertification(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_certification",
            description=Component.DESCRIPTION,
            input=UpdateCertificationInput(),
            output=UpdateCertificationOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        id = params.get(Input.ID)
        record = params.get(Input.RECORD)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.CERTIFICATION: self.connection.client.update_record("Certifications", id, record)}
