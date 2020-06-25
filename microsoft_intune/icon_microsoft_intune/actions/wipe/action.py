import insightconnect_plugin_runtime
from .schema import WipeInput, WipeOutput, Input, Output, Component
# Custom imports below


class Wipe(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="wipe",
            description=Component.DESCRIPTION,
            input=WipeInput(),
            output=WipeOutput())

    def run(self, params={}):
        device = self.connection.api.get_device_by_uuid_if_not_whitelisted(
            params.get(Input.DEVICE),
            params.get(Input.WHITELIST)
        )

        if device:
            self.connection.api.wipe_managed_device(device["id"])

            return {
                Output.SUCCESS: True
            }

        self.logger.info(f"Managed device: {params.get(Input.DEVICE)} was not wiped because it was whitelisted")
        return {
            Output.SUCCESS: False
        }
