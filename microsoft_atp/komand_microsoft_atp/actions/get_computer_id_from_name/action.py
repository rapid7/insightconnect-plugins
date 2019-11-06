import komand
from .schema import GetComputerIdFromNameInput, GetComputerIdFromNameOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class GetComputerIdFromName(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_computer_id_from_name',
                description=Component.DESCRIPTION,
                input=GetComputerIdFromNameInput(),
                output=GetComputerIdFromNameOutput())

    def run(self, params={}):
        machine_name = params.get(Input.MACHINE_NAME)
        machine = self.connection.translate_machine_name(machine_name)
        try:
            machine_id = machine['value'][0]['id']
        except KeyError as k:
            self.logger.error("Could not find 'value' key in file information response: " + str(k))
        return {Output.MACHINE_ID: machine_id}
