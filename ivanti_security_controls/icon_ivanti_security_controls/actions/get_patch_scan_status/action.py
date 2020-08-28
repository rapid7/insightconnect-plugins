import insightconnect_plugin_runtime
from .schema import GetPatchScanStatusInput, GetPatchScanStatusOutput, Input, Output, Component
# Custom imports below


class GetPatchScanStatus(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_patch_scan_status',
                description=Component.DESCRIPTION,
                input=GetPatchScanStatusInput(),
                output=GetPatchScanStatusOutput())

    def run(self, params={}):
        patch_scan_status_details = self.connection.ivanti_api.get_patch_scan_status_details(params.get(Input.SCAN_ID))
        return {
            Output.PATCH_SCAN_STATUS_DETAILS: patch_scan_status_details
        }
