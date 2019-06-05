import komand
from .schema import DeleteInput, DeleteOutput
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
        try:
            output = self.connection.request.delete_(xpath=xpath)
            return {"response": output['response']}
        except KeyError:
            self.logger.error('The output did not contain a proper response.')
            self.logger.error(output)
            raise
