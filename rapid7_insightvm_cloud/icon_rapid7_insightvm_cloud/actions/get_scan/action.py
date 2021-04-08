import insightconnect_plugin_runtime
from .schema import GetScanInput, GetScanOutput, Input, Output, Component
# Custom imports below


class GetScan(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_scan',
                description=Component.DESCRIPTION,
                input=GetScanInput(),
                output=GetScanOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
