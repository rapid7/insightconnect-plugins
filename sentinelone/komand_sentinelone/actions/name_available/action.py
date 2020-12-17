import insightconnect_plugin_runtime
from .schema import NameAvailableInput, NameAvailableOutput, Input, Output, Component
# Custom imports below


class NameAvailable(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='name_available',
                description=Component.DESCRIPTION,
                input=NameAvailableInput(),
                output=NameAvailableOutput())

    def run(self, params={}):
        return {
            Output.AVAILABLE: self.connection.name_available(params.get("name")).get("available", False)
        }
