import komand
from .schema import ShowCommandsInput, ShowCommandsOutput
import netmiko


class ShowCommands(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='show_commands',
                description='Check the devices configurations',
                input=ShowCommandsInput(),
                output=ShowCommandsOutput())
        self.device = None

    def run(self, params={}):
        self.device = self.connection.client(params.get('host'))
        any_show_command = params.get('command')
        try:
            output = self.device.send_command(any_show_command)
            return {'results': output}
        except netmiko.NetMikoTimeoutException:
            self.logger.error("Cannot connect to this device.")
            raise

    def test(self):
        output = self.connection.device_connect.is_alive()
        if not output:
            raise Exception("Could not connect")
        return {'results': 'Test passed!'}