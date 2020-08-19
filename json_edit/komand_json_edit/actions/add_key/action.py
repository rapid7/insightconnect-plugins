import komand
from .schema import AddKeyInput, AddKeyOutput, Input, Output, Component
# Custom imports below


class AddKey(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_key',
                description=Component.DESCRIPTION,
                input=AddKeyInput(),
                output=AddKeyOutput())

    def run(self, params={}):
        return {
            Output.JSON: {
                params.get(Input.KEY): params.get(Input.VALUE)
            }
        }
