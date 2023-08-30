import insightconnect_plugin_runtime
from .schema import FullScanInput, FullScanOutput, Input, Output, Component

# Custom imports below


class FullScan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="full_scan", description=Component.DESCRIPTION, input=FullScanInput(), output=FullScanOutput()
        )

    def run(self, params={}):
        return {Output.SUCCESS: self.connection.api.full_scan(params.get(Input.DEVICE_ID))}
