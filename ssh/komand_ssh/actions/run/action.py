import komand
from .schema import RunInput, RunOutput, Input, Output
# Custom imports below


class Run(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run',
                description='Run remote command',
                input=RunInput(),
                output=RunOutput())

    def run(self, params={}):
        results = {}
        command = params.get(Input.COMMAND)
        client = self.connection.client(params.get(Input.HOST))
        (stdin, stdout, stderr) = client.exec_command(command)
        results['stdout'] = "\n".join(stdout.readlines())
        results['stderr'] = "\n".join(stderr.readlines())
        results['all_output'] = results['stdout'] + results['stderr']
        client.close()
        return {Output.RESULTS: results}
