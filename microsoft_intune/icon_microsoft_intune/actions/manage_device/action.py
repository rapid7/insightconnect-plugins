import insightconnect_plugin_runtime
from .schema import ManageDeviceInput, ManageDeviceOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
import validators


class ManageDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='manage_device',
            description=Component.DESCRIPTION,
            input=ManageDeviceInput(),
            output=ManageDeviceOutput())

        self.actions = {
            "Reboot": "rebootNow",
            "Sync": "syncDevice",
        }

    def run(self, params={}):
        device_name = params.get(Input.DEVICE)
        device = self.connection.api.get_device_by_uuid_if_not_whitelisted(
            device_name,
            params.get(Input.WHITELIST)
        )

        if device:
            response = self.connection.api.managed_device_action(device["id"], self.actions[params.get(Input.TYPE)])
            self.logger.info(f"response: {response}")

            return {
                Output.SUCCESS: not response
            }

        self.logger.info(f"Action: {params.get(Input.TYPE)} will not be taken on managed device: {device_name} because it was whitelisted")
        return {
            Output.SUCCESS: False
        }
