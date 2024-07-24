import insightconnect_plugin_runtime
from .schema import ExportRpzInput, ExportRpzOutput, Input, Output, Component
# Custom imports below


class ExportRpz(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="export_rpz",
                description=Component.DESCRIPTION,
                input=ExportRpzInput(),
                output=ExportRpzOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        event_id = params.get(Input.EVENT_ID)
        from = params.get(Input.FROM)
        tags = params.get(Input.TAGS)
        to = params.get(Input.TO)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RPZ: None,
        }
