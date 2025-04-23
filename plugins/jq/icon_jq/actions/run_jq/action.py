import json
import os
import re

# Custom imports below
import subprocess  # noqa: B404
from subprocess import PIPE  # noqa: B404

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.util import is_running_in_cloud

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
            raise PluginException("JQ failed due to the timeout exceeding the maximum limit of 300 seconds.")
        elif timeout < 1:
            raise PluginException("The timeout must be greater than 0 seconds.")

        jq_cmd_array = ["jq"]
        accepted_flags = ["-c", "-r", "-R"]

        flags = params.get(Input.FLAGS)

        if flags:
            # Cleaning input of whitespace and splitting
            flag_list = []
            for item in flags:
                split_items = item.split(",")
                cleaned = [flag.strip() for flag in split_items if flag.strip()]
                flag_list.extend(cleaned)

            # Validate
            if all(f in accepted_flags for f in flag_list):
                jq_cmd_array.extend(flag_list)
            else:
                invalid_flags = [f for f in flag_list if f not in accepted_flags]
                raise PluginException(
                    f"The following flag(s) are not supported: {invalid_flags}. "
                    f"Please ensure your input meets the criteria of the following flags: {accepted_flags}"
                )

        blocked_patterns = [r"/proc/", r"/dev/", r'import\s+"']
        #  Prevents possible malicious injections
        for pattern in blocked_patterns:
            if re.search(pattern, filter_, re.IGNORECASE):
                raise PluginException(f"Blocked pattern found in filter: {pattern}")

        jq_cmd_array.append(filter_)

        self.logger.info(f"Command to Run: {jq_cmd_array}")
        process = subprocess.Popen(jq_cmd_array, stdout=PIPE, stderr=PIPE, stdin=PIPE)  # noqa: B603
        std_out, std_err = process.communicate(input=json.dumps(json_in).encode(), timeout=timeout)
        return_code = process.returncode

        self.logger.info(f"Return Code: {return_code}")
        if return_code > 0:
            self.logger.info(f"JQ Standard Output: {std_out.decode()}")
            self.logger.info(f"JQ Standard Error: {std_err.decode}")
            raise PluginException(f"JQ failed with return code: {return_code}")

        output_string = std_out.decode("utf-8").strip()
        return {Output.JSON_OUT: output_string}
