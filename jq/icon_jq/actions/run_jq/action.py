import json
# Custom imports below
import subprocess
from subprocess import PIPE

import komand
from .schema import RunJqInput, RunJqOutput, Input, Output


class RunJq(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_jq',
                description='Pass the given JSON to the jq command, using the given flags and filter',
                input=RunJqInput(),
                output=RunJqOutput())

    def run(self, params=None):
        if params is None:
            params = {}

        json_in = params.get(Input.JSON_IN)
        flags = params.get(Input.FLAGS)
        filter_ = params.get(Input.FILTER)
        timeout = params.get(Input.TIMEOUT)

        jq_cmd_array = ["jq"]

        if len(flags) > 0:
            string_flags = ' '.join(flags)
            jq_cmd_array.append(string_flags)

        jq_cmd_array.append(filter_)

        self.logger.info("Command to Run: {}".format(jq_cmd_array))
        process = subprocess.Popen(jq_cmd_array, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        std_out, std_err = process.communicate(input=json.dumps(json_in).encode(), timeout=timeout)
        return_code = process.returncode

        self.logger.info("Return Code: {}".format(return_code))
        if return_code > 0:
            self.logger.info("JQ Standard Output: {}".format(std_out.decode()))
            self.logger.info("JQ Standard Error: {}".format(std_err.decode()))
            raise Exception("JQ failed with return code: {}".format(return_code))

        output_string = std_out.decode('utf-8').strip()
        return {Output.JSON_OUT: output_string}
