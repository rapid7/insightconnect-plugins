import insightconnect_plugin_runtime
from .schema import ManageDeviceInput, ManageDeviceOutput, Input, Output, Component
# Custom imports below


class ManageDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='manage_device',
            description=Component.DESCRIPTION,
            input=ManageDeviceInput(),
            output=ManageDeviceOutput())

        self.actions = {
            "Shutdown": "shutDown",
            "Reboot": "rebootNow",
            "Sync": "syncDevice",
            "Reset PassCode": "resetPasscode",
            "Lock": "remoteLock",
        }

    def run(self, params={}):
        device = self.connection.api.get_device_by_uuid_if_not_whitelisted(
            params.get(Input.DEVICE),
            params.get(Input.WHITELIST)
        )

        if device:
            self.connection.api.managed_device_action(device["id"], self.actions[params.get(Input.TYPE)])

            return {
                Output.SUCCESS: True
            }

        self.logger.info(f"Action: {params.get(Input.TYPE)} will not be taken on managed device: {params.get(Input.DEVICE)} because it was whitelisted")
        return {
            Output.SUCCESS: False
        }
