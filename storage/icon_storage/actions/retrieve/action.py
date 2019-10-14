import komand
from .schema import RetrieveInput, RetrieveOutput, Input, Output, Component
# Custom imports below
from icon_storage.util.cache_help import CacheHelp


class Retrieve(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve',
                description=Component.DESCRIPTION,
                input=RetrieveInput(),
                output=RetrieveOutput())

    def run(self, params={}):
        var_to_get = params.get(Input.VARIABLE_NAME)
        cache_help = CacheHelp()
        ret_val = cache_help.retrieve_variable(var_to_get)
        return {Output.VALUE: ret_val}
