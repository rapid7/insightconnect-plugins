import komand
from .schema import ProcessStringInput, ProcessStringOutput, Input, Output
# Custom imports below
import subprocess
import pipes


class ProcessString(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='process_string',
                description='Process string',
                input=ProcessStringInput(),
                output=ProcessStringOutput())

    def run(self, params={}):
        input_str = params.get(Input.STRING)
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
        output = output.decode("utf-8")

        return {Output.OUTPUT: output}
