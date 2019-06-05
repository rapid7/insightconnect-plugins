import komand
from .schema import SetInput, SetOutput
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
        try:
            output = self.connection.request.set_(xpath=xpath, element=element)
            return {"response": output['response']}
        except KeyError:
            self.logger.error('The output did not contain a proper response.')
            self.logger.error(output)
            raise
