import insightconnect_plugin_runtime
from .schema import RunInput, RunOutput, Input, Output

# Custom imports below


class Run(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run", description="Run remote command", input=RunInput(), output=RunOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        command = params.get(Input.COMMAND)
        host = params.get(Input.HOST)
        # END INPUT BINDING - DO NOT REMOVE

        results = {}
        client = self.connection.client(host)
        _, stdout, stderr = client.exec_command(command)
        results["stdout"] = "\n".join(stdout.readlines())
        results["stderr"] = "\n".join(stderr.readlines())
        results["all_output"] = results["stdout"] + results["stderr"]
        client.close()
        return {Output.RESULTS: results}
