import insightconnect_plugin_runtime
from .schema import StartPatchScanInput, StartPatchScanOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import time


class StartPatchScan(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='start_patch_scan',
                description=Component.DESCRIPTION,
                input=StartPatchScanInput(),
                output=StartPatchScanOutput())

    def run(self, params={}):
        endpoint_names = params.get(Input.HOSTNAMES, [])
        machine_group_ids = params.get(Input.MACHINE_GROUP_IDS, [])
        use_machine_credential = params.get(Input.USE_MACHINE_CREDENTIAL, False)
        max_poll_time = params.get(Input.MAX_POLL_TIME)

        if not endpoint_names and not machine_group_ids:
            raise PluginException(cause='No hostnames or machine group IDs specified.',
                                  assistance='Either hostnames or machine group IDs must be specified.'
                                  )
        if use_machine_credential:
            if not endpoint_names:
                raise PluginException(cause='Machine credentials can only be set to true if hostname is specified.',
                                      assistance='Either provide a valid hostname or set machine credentials to False.')
        payload = {
            "credentialId": params.get(Input.CREDENTIAL_ID),
            "diagnosticTraceEnabled": params.get(Input.DIAGNOSTIC_TRACE_ENABLED),
            "endpointNames": endpoint_names,
            "machinegroupIds": machine_group_ids,
            "name": params.get(Input.NAME),
            "runAsCredentialId": params.get(Input.RUN_AS_CREDENTIAL_ID),
            "templateId": params.get(Input.TEMPLATE_ID),
            "useMachineCredential": use_machine_credential
        }
        scan_details = self.connection.ivanti_api.start_patch_scan(payload)

        i = 0
        # Poll for patch scan completion
        while i < max_poll_time:
            time.sleep(10)
            patch_scan_status_details = self.connection.ivanti_api.get_patch_scan_status_details(scan_details['id'], allow_404=True)
            if patch_scan_status_details is not None:
                if patch_scan_status_details.get('isComplete'):
                    scan_details['isComplete'] = patch_scan_status_details['isComplete']
                    scan_details['updatedOn'] = patch_scan_status_details['updatedOn']
                    break
            i += 10

        return {
            Output.SCAN_DETAILS: scan_details
        }
