import insightconnect_plugin_runtime
from .schema import (
    SubmitRemediationInput,
    SubmitRemediationOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException


class SubmitRemediation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_remediation",
            description=Component.DESCRIPTION,
            input=SubmitRemediationInput(),
            output=SubmitRemediationOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        action_type = params.get(Input.ACTION_TYPE, "")
        devices_json = params.get(Input.DEVICES_JSON, {})
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        result = self.connection.automox_api.submit_remediation(
            org_id=org_id,
            action_type=action_type,
            devices_input=devices_json,
        )

        return {
            Output.BATCH_UUID: result["batch_uuid"],
            Output.TOTAL_DEVICES: result["total_devices"],
            Output.CHUNKS_SENT: result["chunks_sent"],
            Output.RESPONSES: result["responses"],
        }
