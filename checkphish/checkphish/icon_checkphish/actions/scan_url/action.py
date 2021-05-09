import insightconnect_plugin_runtime
from .schema import ScanUrlInput, ScanUrlOutput, Input, Output, Component
# Custom imports below


class ScanUrl(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='scan_url',
                description=Component.DESCRIPTION,
                input=ScanUrlInput(),
                output=ScanUrlOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
