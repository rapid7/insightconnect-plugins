import komand
from .schema import CheckForVariableInput, CheckForVariableOutput, Input, Output, Component
# Custom imports below
from icon_storage.util.cache_help import CacheHelp


class CheckForVariable(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_for_variable',
                description=Component.DESCRIPTION,
                input=CheckForVariableInput(),
                output=CheckForVariableOutput())

    def run(self, params={}):
        var_to_look_for = params.get(Input.VARIABLE_NAME)
        cache_help = CacheHelp()
        return {Output.VARIABLE_FOUND: cache_help.check_for_variable(var_to_look_for)}
