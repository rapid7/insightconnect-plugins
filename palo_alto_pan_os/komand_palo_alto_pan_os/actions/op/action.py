import komand
from .schema import OpInput, OpOutput
# Custom imports below


class Op(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='op',
                description='Run operational command',
                input=OpInput(),
                output=OpOutput())

    def run(self, params={}):
        cmd = params.get("cmd")
        output = self.connection.request.op(cmd)
        try:
            return {"response": output['response']}
        except KeyError:
            self.logger.error('The output did not contain a proper response.')
            self.logger.error(output)
            raise
