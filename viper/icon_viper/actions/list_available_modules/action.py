import komand
from .schema import ListAvailableModulesInput, ListAvailableModulesOutput, Input, Output, Component
from ...util import module


class ListAvailableModules(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_available_modules',
                description=Component.DESCRIPTION,
                input=ListAvailableModulesInput(),
                output=ListAvailableModulesOutput())

    def run(self, params={}):
        return {
            Output.MODULES: module.Module.all(self.connection.config)
        }
