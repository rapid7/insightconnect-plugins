import komand
from .schema import ShowInput, ShowOutput
from komand.exceptions import PluginException
# Custom imports below


class Show(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='show',
                description='Get active configuration',
                input=ShowInput(),
                output=ShowOutput())

    def run(self, params={}):
        xpath = params.get("xpath", "")

        output = self.connection.request.show_(xpath=xpath)
        try:
            return {"response": output['response']}
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=output)
