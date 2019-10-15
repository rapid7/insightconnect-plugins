import komand
from .schema import DeleteInput, DeleteOutput
from komand.exceptions import PluginException
# Custom imports below


class Delete(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete',
                description='Delete an object',
                input=DeleteInput(),
                output=DeleteOutput())

    def run(self, params={}):
        xpath = params.get("xpath")

        output = self.connection.request.delete_(xpath=xpath)
        try:
            return {"response": output['response']}
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=output)
