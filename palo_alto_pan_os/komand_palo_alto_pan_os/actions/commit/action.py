import komand
from .schema import CommitInput, CommitOutput
from komand.exceptions import PluginException
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
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=output)
