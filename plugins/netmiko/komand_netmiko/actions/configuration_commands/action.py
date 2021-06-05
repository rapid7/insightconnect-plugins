import insightconnect_plugin_runtime
from .schema import ConfigurationCommandsInput, ConfigurationCommandsOutput, Component, Input, Output
import netmiko

from insightconnect_plugin_runtime.exceptions import PluginException


class ConfigurationCommands(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="configuration_commands",
            description=Component.DESCRIPTION,
            input=ConfigurationCommandsInput(),
            output=ConfigurationCommandsOutput(),
        )
        self.device = None

    def run(self, params={}):
        self.device = self.connection.client(params.get(Input.HOST))
        try:
            return {Output.RESULTS: self.device.send_config_set(params.get(Input.COMMAND))}
        except netmiko.NetMikoTimeoutException:
            raise PluginException(
                cause="Cannot connect/configure this device.",
                assistance="Please check provided connection data and try again.",
            )
