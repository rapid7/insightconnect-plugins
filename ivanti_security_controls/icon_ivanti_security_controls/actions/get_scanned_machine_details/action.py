import insightconnect_plugin_runtime
from .schema import GetScannedMachineDetailsInput, GetScannedMachineDetailsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetScannedMachineDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_scanned_machine_details',
                description=Component.DESCRIPTION,
                input=GetScannedMachineDetailsInput(),
                output=GetScannedMachineDetailsOutput())

    def run(self, params={}):
        machine_id = ""
        scan_id = params.get(Input.SCAN_ID)
        hostname = params.get(Input.HOSTNAME)

        patch_scan_machine = self.connection.ivanti_api.get_patch_scan_machines(scan_id)
        machine = {}
        for m in patch_scan_machine['value']:
            if m['name'] == hostname:
                machine_id = m['id']
                machine = m
                break

        if not machine_id:
            raise PluginException(cause=f"No patch scan machine found with hostname {hostname} for scan ID {scan_id}.",
                                  assistance="Please provide valid hostname.")
        detected_patches = self.connection.ivanti_api.get_detected_patches(scan_id, machine_id)['value']

        return {
            Output.PATCH_SCAN_MACHINE: machine,
            Output.DETECTED_PATCHES: detected_patches
        }
