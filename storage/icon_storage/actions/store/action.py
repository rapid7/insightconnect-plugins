import komand
from .schema import StoreInput, StoreOutput, Input, Output, Component
# Custom imports below
from icon_storage.util.cache_help import CacheHelp


class Store(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='store',
                description=Component.DESCRIPTION,
                input=StoreInput(),
                output=StoreOutput())

    def run(self, params={}):
        variable_to_store = params.get(Input.VARIABLE_NAME)
        value_to_store = params.get(Input.VARIABLE_VALUE)

        cache_help = CacheHelp()
        cache_help.store_variable(variable_to_store, value_to_store)

        return {Output.SUCCESS: True}
