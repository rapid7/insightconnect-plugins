import komand
from .schema import AddKeyToObjectInput, AddKeyToObjectOutput, Input, Output, Component
# Custom imports below


class AddKeyToObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_key_to_object',
                description=Component.DESCRIPTION,
                input=AddKeyToObjectInput(),
                output=AddKeyToObjectOutput())

    def run(self, params={}):
        json_object = params.get(Input.OBJECT)
        json_object[params.get(Input.KEY)] = params.get(Input.VALUE, "")

        return {
            Output.JSON: json_object
        }
