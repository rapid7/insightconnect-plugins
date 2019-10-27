import komand
from .schema import DeleteVariableInput, DeleteVariableOutput, Input, Output, Component
# Custom imports below
from icon_storage.util.cache_help import CacheHelp


class DeleteVariable(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_variable',
                description=Component.DESCRIPTION,
                input=DeleteVariableInput(),
                output=DeleteVariableOutput())

    def run(self, params={}):
        var_to_delete = params.get(Input.VARIABLE_NAME)
        cache_helper = CacheHelp()
        cache_helper.delete_variable(var_to_delete)
        return {Output.SUCCESS: True}
