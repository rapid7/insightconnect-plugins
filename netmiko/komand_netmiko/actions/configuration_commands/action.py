import komand
from .schema import ConfigurationCommandsInput, ConfigurationCommandsOutput
import netmiko


class ConfigurationCommands(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='configuration_commands',
                description='Change the devices configuration',
                input=ConfigurationCommandsInput(),
                output=ConfigurationCommandsOutput())
        self.device = None

    def run(self, params={}):
        self.device = self.connection.client(params.get('host'))
        any_config_command = params.get('command')
        try:
            output = self.device.send_config_set(any_config_command)
            return {'results': output}
        except netmiko.NetMikoTimeoutException:
            self.logger.error("Cannot connect/configure this device")
            raise

    def test(self):
        output = self.connection.device_connect.is_alive()
        if not output:
            raise Exception("Could not connect")
        return {'results': 'Test passed!'}
