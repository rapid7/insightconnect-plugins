import komand
from .schema import ShowInput, ShowOutput
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
        try:
            output = self.connection.request.show_(xpath=xpath)
            return {"response": output['response']}
        except KeyError:
            self.logger.error('The output did not contain a proper response.')
            self.logger.error(output)
            raise
