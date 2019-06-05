import komand
from .schema import GetInput, GetOutput
# Custom imports below


class Get(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get',
                description='Get candidate configuration',
                input=GetInput(),
                output=GetOutput())

    def run(self, params={}):
        xpath = params.get("xpath", "")

        output = self.connection.request.get_(xpath=xpath)
        try:
            return {"response": output['response']}
        except KeyError:
            self.logger.error('The output did not contain a proper response.')
            self.logger.error(output)
            raise
