import insightconnect_plugin_runtime
from .schema import ClearTagsInput, ClearTagsOutput, Input, Output
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class ClearTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='clear_tags',
            description='Clears the given tag to a supplied list of systems',
            input=ClearTagsInput(),
            output=ClearTagsOutput())

    def run(self, params=None):
        if params is None:
            params = {}
        try:
            devices = []
            for d in self.connection.client('system.find', params.get(Input.DEVICE)):
                computer_name = d["EPOComputerProperties.ComputerName"]
                self.connection.client(
                    'system.clearTag',
                    computer_name,
                    params.get(Input.TAG)
                )
                devices.append(computer_name)
            self.logger.info(f"Tag cleared from {len(devices)} devices")
            return {
                Output.MESSAGE: "Tags cleared from devices successfully"
            }
        except Exception as e:
            raise PluginException(
                cause="Tags error.",
                assistance="Tags could not be cleared from some or all devices.",
                data=e
            )
