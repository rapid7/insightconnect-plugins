import insightconnect_plugin_runtime
import time
from .schema import GetNewInvestigationsInput, GetNewInvestigationsOutput, Input, Output, Component
# Custom imports below


class GetNewInvestigations(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="get_new_investigations",
                description=Component.DESCRIPTION,
                input=GetNewInvestigationsInput(),
                output=GetNewInvestigationsOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE

        while True:
            # TODO: Implement trigger functionality
            self.send({})
            time.sleep(5)
