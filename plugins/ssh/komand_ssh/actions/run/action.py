import insightconnect_plugin_runtime

from .schema import Input, Output, RunInput, RunOutput

# Custom imports below


class Run(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run", description="Run remote command", input=RunInput(), output=RunOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        host = params.get(Input.HOST, "")
        command = params.get(Input.COMMAND, "")
        # END INPUT BINDING - DO NOT REMOVE

        results = {}
        client = self.connection.client(host)
        _, stdout, stderr = client.exec_command(command)
        results["stdout"] = "\n".join(stdout.readlines())
        results["stderr"] = "\n".join(stderr.readlines())
        results["all_output"] = results["stdout"] + results["stderr"]
        client.close()
        return {Output.RESULTS: results}
