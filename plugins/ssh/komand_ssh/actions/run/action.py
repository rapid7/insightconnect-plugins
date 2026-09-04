import insightconnect_plugin_runtime

from .schema import Input, Output, RunInput, RunOutput

# Custom imports below
from komand_ssh.util.constants import DEFAULT_ENCODING, MAX_COMMAND_ARG_BYTES


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
        encoded_command = command.encode(DEFAULT_ENCODING)
        try:
            if len(encoded_command) >= MAX_COMMAND_ARG_BYTES:
                # Above MAX_ARG_STRLEN, exec_command(command) fails with "Argument list too long"
                self.logger.info("Command exceeds argument-length threshold, sending it via stdin instead")
                stdin, stdout, stderr = client.exec_command("/bin/sh -s")
                stdin.write(encoded_command)
                stdin.flush()
                stdin.channel.shutdown_write()
            else:
                _, stdout, stderr = client.exec_command(command)

            results["stdout"] = stdout.read().decode(DEFAULT_ENCODING)
            results["stderr"] = stderr.read().decode(DEFAULT_ENCODING)
            results["all_output"] = results["stdout"] + results["stderr"]

            exit_code = stdout.channel.recv_exit_status()
            if exit_code != 0:
                self.logger.warning(f"Remote command exited with a non-zero status: {exit_code}")
        finally:
            client.close()

        return {Output.RESULTS: results}
