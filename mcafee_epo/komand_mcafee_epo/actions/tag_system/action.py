import insightconnect_plugin_runtime
from .schema import TagSystemInput, TagSystemOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class TagSystem(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='tag_system',
            description=Component.DESCRIPTION,
            input=TagSystemInput(),
            output=TagSystemOutput())

    def run(self, params=None):
        if params is None:
            params = {}

        try:
            devices = []
            for d in self.connection.client('system.find', params.get(Input.AGENT)):
                computer_name = d["EPOComputerProperties.ComputerName"]
                self.connection.client(
                    'system.applyTag',
                    computer_name,
                    params.get(Input.TAG)
                )
                devices.append(computer_name)
            self.logger.info(f"Applied to {len(devices)} devices")

            return {
                Output.MESSAGE: "Tag applied to devices successfully"
            }
        except Exception as e:
            raise PluginException(
                cause="Tag error.",
                assistance="Tag could not be added to some or all devices. Please check tag name and device name.",
                data=e
            )
