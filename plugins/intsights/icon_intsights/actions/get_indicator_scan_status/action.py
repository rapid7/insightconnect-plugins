import insightconnect_plugin_runtime
from .schema import GetIndicatorScanStatusInput, GetIndicatorScanStatusOutput, Input, Output, Component
# Custom imports below


class GetIndicatorScanStatus(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_indicator_scan_status',
                description=Component.DESCRIPTION,
                input=GetIndicatorScanStatusInput(),
                output=GetIndicatorScanStatusOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
