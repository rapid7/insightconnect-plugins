import insightconnect_plugin_runtime
from .schema import LockComputerInput, LockComputerOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class LockComputer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lock_computer",
            description=Component.DESCRIPTION,
            input=LockComputerInput(),
            output=LockComputerOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.ID)
        passcode = params.get(Input.PASSCODE)
        self.connection.client.lock_computer(identifier, passcode)
        return {Output.STATUS: True}
