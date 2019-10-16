import komand
from .schema import SetInput, SetOutput
from komand.exceptions import PluginException
# Custom imports below


class Set(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set',
                description='Create a new object',
                input=SetInput(),
                output=SetOutput())

    def run(self, params={}):
        xpath = params.get("xpath")
        element = params.get("element")

        output = self.connection.request.set_(xpath=xpath, element=element)
        try:
            return {"response": output['response']}
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=output)
