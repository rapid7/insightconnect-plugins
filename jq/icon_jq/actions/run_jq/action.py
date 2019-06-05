import komand
from .schema import RunJqInput, RunJqOutput, Input, Output
# Custom imports below
import subprocess
from subprocess import PIPE
import json


class RunJq(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_jq',
                description='Pass the given JSON to the jq command, using the given flags and filter',
                input=RunJqInput(),
                output=RunJqOutput())

    def run(self, params={}):
        json_in = params.get(Input.JSON_IN)
        flags = params.get(Input.FLAGS)
        filter_ = params.get(Input.FILTER)
        timeout = params.get(Input.TIMEOUT)

        jq_cmd_array = ["jq"]

        # Setup Flags if we have them
        if len(flags) > 0:
            string_flags = ' '.join(flags)
            jq_cmd_array.append(string_flags)

        # Need to surround the filter in single quotes
        # filter = "\"" + filter + "\""
        jq_cmd_array.append(filter_)

        # Run the process
        self.logger.info("Command to Run: " + str(jq_cmd_array))
        process = subprocess.Popen(jq_cmd_array, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        std_out, std_err = process.communicate(input=json.dumps(json_in).encode(), timeout=timeout)
        return_code = process.returncode

        # This is verbose logging but there's a lot that can go wrong here
        # Hopefully we can tell if it's bad JSON or a bad filter
        self.logger.info("Return Code: " + str(return_code))
        if(return_code > 0):
            self.logger.info("JQ Standard Output: " + std_out.decode())
            self.logger.info("JQ Standard Error: " + std_err.decode())
            raise Exception("JQ failed with return code: " + str(return_code))

        output_string = std_out.decode('utf-8').strip()
        return {Output.JSON_OUT: output_string}
