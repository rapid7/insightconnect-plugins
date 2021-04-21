import insightconnect_plugin_runtime
from .schema import QuarantineFileInput, QuarantineFileOutput, Input, Output, Component
# Custom imports below


class QuarantineFile(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine_file',
                description=Component.DESCRIPTION,
                input=QuarantineFileInput(),
                output=QuarantineFileOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
