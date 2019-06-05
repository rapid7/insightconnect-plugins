import komand
from .schema import CommitInput, CommitOutput
# Custom imports below


class Commit(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='commit',
                description='Commit the candidate configuration',
                input=CommitInput(),
                output=CommitOutput())

    def run(self, params={}):
        cmd = (params.get("cmd"))
        action = params.get("action")

        output = self.connection.request.commit(action, cmd)

        try:
            return {"response": output['response']}
        except KeyError:
            self.logger.error('The output did not contain a proper response.')
            self.logger.error(output)
            raise
