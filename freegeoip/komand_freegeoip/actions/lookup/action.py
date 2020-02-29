import komand
from .schema import LookupInput, LookupOutput, Input, Output, Component


class Lookup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup',
            description=Component.DESCRIPTION,
            input=LookupInput(),
            output=LookupOutput())

    def run(self, params={}):
        response = self.connection.client.lookup(
            params.get(Input.LANGUAGE, 'en'),
            params.get(Input.SHOULD_RETURN_HOSTNAME, True),
            params.get(Input.SHOULD_RETURN_HOSTNAME, True)
        )
        return {
            Output.INFORMATION: komand.helper.clean_dict(response)
        }
