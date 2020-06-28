import insightconnect_plugin_runtime
from .schema import StartPatchScanInput, StartPatchScanOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import polling2

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
        
        self.connection.ivanti_api.create_session_credential()

        scan = self.connection.ivanti_api.start_patch_scan(payload)

        operation_location_url = scan.headers.get("Operation-Location")

        try:
            polling2.poll(lambda: self.connection.ivanti_api.get_operation_location(operation_location_url)
            .get("percentComplete") == 100, step=10, timeout=max_poll_time)
        except polling2.TimeoutException as e:
            raise PluginException(
                cause='Action timeout.',
                assistance=f'This scan has exceeded the maximum poll time of {max_poll_time}.')

        operation_location = self.connection.ivanti_api.get_operation_location(operation_location_url)
        scan_details = scan.json()
        scan_details['isComplete'] = True
        scan_details['updatedOn'] = operation_location['lastAction']

        return {
            Output.SCAN_DETAILS: scan_details
        }
