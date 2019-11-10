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
        command = params.get(Input.COMMAND)
        client = self.connection.client(params.get(Input.HOST))
        (stdin, stdout, stderr) = client.exec_command(command)
        stdout_string = "\n".join(stdout.readlines())
        stderr_string = "\n".join(stderr.readlines())
        client.close()
        return {Output.RESULTS: stdout_string + stderr_string}

