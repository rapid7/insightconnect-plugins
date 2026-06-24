import insightconnect_plugin_runtime
from .schema import UpdateDeviceInput, UpdateDeviceOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class UpdateDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_device",
            description=Component.DESCRIPTION,
            input=UpdateDeviceInput(),
            output=UpdateDeviceOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        device_id = params.get(Input.DEVICE_ID, 0)
        server_group_id = params.get(Input.SERVER_GROUP_ID, 0)
        exception = params.get(Input.EXCEPTION, False)
        tags = params.get(Input.TAGS, [])
        custom_name = params.get(Input.CUSTOM_NAME, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        current_device_details = self.connection.automox_api.get_device(org_id, device_id)

        server_group_id = current_device_details["server_group_id"] if server_group_id == 0 else server_group_id
        payload = {
            "server_group_id": server_group_id,
            "ip_addrs": current_device_details["ip_addrs"],
            "exception": exception,
            "tags": tags,
            "custom_name": custom_name,
        }
        self.connection.automox_api.update_device(org_id, device_id, payload)
        return {Output.SUCCESS: True}
