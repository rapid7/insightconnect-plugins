import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import QuickScanInput, QuickScanOutput, Input, Output, Component

# Custom imports below


class QuickScan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quick_scan", description=Component.DESCRIPTION, input=QuickScanInput(), output=QuickScanOutput()
        )

    def run(self, params={}):
        return {Output.SUCCESS: self.connection.api.quick_scan(params.get(Input.DEVICE_ID))}
