import insightconnect_plugin_runtime
from .schema import EraseComputerInput, EraseComputerOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class EraseComputer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="erase_computer",
            description=Component.DESCRIPTION,
            input=EraseComputerInput(),
            output=EraseComputerOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.ID)
        passcode = params.get(Input.PASSCODE)
        self.connection.client.erase_computer(identifier, passcode)
        return {Output.STATUS: True}
