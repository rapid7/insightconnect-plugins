import insightconnect_plugin_runtime
from .schema import DeleteDeviceInput, DeleteDeviceOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class DeleteDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_device",
            description=Component.DESCRIPTION,
            input=DeleteDeviceInput(),
            output=DeleteDeviceOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        device_id = params.get(Input.DEVICE_ID, 0)
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        if device_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Device ID must be a positive integer")

        self.connection.automox_api.delete_device(org_id, device_id)
        return {Output.SUCCESS: True}
