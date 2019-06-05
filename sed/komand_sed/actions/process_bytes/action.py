import komand
from .schema import ProcessBytesInput, ProcessBytesOutput, Input, Output
# Custom imports below
import subprocess
import pipes
import base64


class ProcessBytes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='process_bytes',
                description='Process bytes of base64 encoded string',
                input=ProcessBytesInput(),
                output=ProcessBytesOutput())

    def run(self, params={}):
        input_str = base64.b64decode(params.get(Input.BYTES))
        input_str = input_str.decode("utf-8")
        sed_list = params.get(Input.EXPRESSION)
        sed_opts = params.get(Input.OPTIONS)

        if sed_list and sed_list[0] != "":
            sed_exp = sed_list[0]
            sed_exp = f" -e '{sed_exp}'"
            for item in sed_list[1:]:
                sed_exp = f"{sed_exp} -e '{item}' "
        else:
            raise Exception('The sed expression must not be an empty string')

        esc_str = pipes.quote(input_str)
        echo_cmd = f"echo ${esc_str}"
        sed_cmd = f"sed {sed_opts} {sed_exp}"

        process0 = subprocess.Popen(echo_cmd, shell=True, stdout=subprocess.PIPE)
        process1 = subprocess.Popen(sed_cmd, shell=True, stdin=process0.stdout, stdout=subprocess.PIPE)
        output = process1.communicate()[0]

        output = output[1:-1]         # Remove leading "$" and trailing newline
        output = base64.b64encode(output)
        output = output.decode("utf-8")

        return {Output.OUTPUT: output}
