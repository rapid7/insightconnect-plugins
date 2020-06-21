import validators
from insightconnect_plugin_runtime.exceptions import PluginException


class Utils:

    @staticmethod
    def get_device_by_uuid_if_not_whitelisted(device, connection_search_device_fn, whitelist):
        if not validators.uuid(device):
            raise PluginException(
                cause=f"Managed device ID: {device} is not valid UUID",
                assistance="Contact support for help. See log for more details"
            )
        device_response = connection_search_device_fn(device)

        if not device_response:
            raise PluginException(
                cause=f"Managed device: {device}, was not found",
                assistance="Contact support for help. See log for more details"
            )
        elif len(device_response) > 1:
            raise PluginException(
                cause=f"Search criteria: {device} returned too many results. Results returned: {len(device_response)}",
                assistance="Contact support for help. See log for more details"
            )

        device_response = device_response[0]
        data_to_look_for_in_whitelist = []
        for key in ["deviceName", "userId", "id", "emailAddress"]:
            data_to_look_for_in_whitelist.append(device_response[key])

        if whitelist and any(item in whitelist for item in data_to_look_for_in_whitelist):
            return {}

        return device_response
