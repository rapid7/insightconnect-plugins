import insightconnect_plugin_runtime
from .schema import ScanInput, ScanOutput, Input, Output, Component
# Custom imports below


class Scan(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='scan',
                description=Component.DESCRIPTION,
                input=ScanInput(),
                output=ScanOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
