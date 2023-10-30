import insightconnect_plugin_runtime
from .schema import UpdateDeviceInput, UpdateDeviceOutput, Input, Output, Component

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
        # Retrieve current group settings to be used as fallback if not provided as input
        current_device_details = self.connection.automox_api.get_device(
            params.get(Input.ORG_ID), params.get(Input.DEVICE_ID)
        )

        # Set server_group_id to current value if not provided as input
        # ICON will set the default value to 0, which causes the params.get() use an invalid group ID
        server_group_id = current_device_details["server_group_id"]
        if params.get(Input.SERVER_GROUP_ID) != 0:
            server_group_id = params.get(Input.SERVER_GROUP_ID)
        payload = {
            "server_group_id": server_group_id,
            "ip_addrs": current_device_details["ip_addrs"],
            "exception": params.get(Input.EXCEPTION, current_device_details["exception"]),
            "tags": params.get(Input.TAGS, current_device_details["tags"]),
            "custom_name": params.get(Input.CUSTOM_NAME, current_device_details["custom_name"]),
        }
        self.connection.automox_api.update_device(params.get(Input.ORG_ID), params.get(Input.DEVICE_ID), payload)

        return {Output.SUCCESS: True}
