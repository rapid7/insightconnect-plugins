import insightconnect_plugin_runtime
import time
from .schema import ScanCompletionInput, ScanCompletionOutput, Input, Output, Component
# Custom imports below


class ScanCompletion(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="scan_completion",
                description=Component.DESCRIPTION,
                input=ScanCompletionInput(),
                output=ScanCompletionOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE

        while True:
            # TODO: Implement trigger functionality
            self.send({})
            time.sleep(5)
