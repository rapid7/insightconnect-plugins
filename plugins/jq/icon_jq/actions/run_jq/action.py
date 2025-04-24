import json

# Custom imports below
import subprocess  # noqa: B404
from subprocess import PIPE  # noqa: B404

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.telemetry import auto_instrument
from .schema import RunJqInput, RunJqOutput, Input, Output


class RunJq(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_jq",
            description="Pass the given JSON to the jq command, using the given flags and filter",
            input=RunJqInput(),
            output=RunJqOutput(),
        )

    @auto_instrument
    def run(self, params=None):
        if params is None:
            params = {}

        json_in = params.get(Input.JSON_IN)
        filter_ = params.get(Input.FILTER)
        timeout = params.get(Input.TIMEOUT, 15)

        # Max time is 5 minutes
        if timeout > 300:
            raise PluginException(
                "JQ failed due to the timeout exceeding the maximum limit of 300 seconds.",
                data=f"The timeout value: {timeout} is over 300 seconds.",
                assistance="Please ensure the specified timeout is below 300 seconds.",
            )
        elif timeout < 1:
            raise PluginException(
                "JQ failed due to the timeout not exceeding 1 second.",
                data=f"The timeout value {timeout} is below 1 second.",
                assistance="Please ensure the timeout value is greater than 0 seconds.",
            )

        jq_cmd_array = ["jq"]
        accepted_flags = ["-c", "-r", "-R", "-j", "-S", "-n", "--tab"]

        flags = params.get(Input.FLAGS)

        invalid_flags = []
        if flags:
            # Stripping whitespaces in input and checking if valid flag
            for item in flags:
                cleaned = item.strip()
                if cleaned in accepted_flags:
                    jq_cmd_array.append(cleaned)
                else:
                    invalid_flags.append(cleaned)

        if invalid_flags:
            raise PluginException(
                cause=f"The following flag(s) are not supported: {invalid_flags}.",
                assistance=f"Please remove the following in order for the action to run: {invalid_flags}.",
                data=f"The following flag(s) are not accepted: {invalid_flags}. Please ensure all flags specified meet the criteria of: {accepted_flags}.",
            )

        if filter_:
            jq_cmd_array.append(filter_)

        self.logger.info(f"Command to Run: {jq_cmd_array}")
        process = subprocess.Popen(jq_cmd_array, stdout=PIPE, stderr=PIPE, stdin=PIPE)  # noqa: B603
        std_out, std_err = process.communicate(input=json.dumps(json_in).encode(), timeout=timeout)
        return_code = process.returncode

        self.logger.info(f"Return Code: {return_code}")
        if return_code > 0:
            self.logger.info(f"JQ Standard Output: {std_out.decode()}")
            self.logger.info(f"JQ Standard Error: {std_err.decode()}")
            raise PluginException(f"JQ failed with return code: {return_code}")

        output_string = std_out.decode("utf-8").strip()
        return {Output.JSON_OUT: output_string}
