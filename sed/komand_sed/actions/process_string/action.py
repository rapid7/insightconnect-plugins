import komand
from .schema import ProcessStringInput, ProcessStringOutput, Input, Output
# Custom imports below
import subprocess


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

        sed_cmd = f"sed {sed_opts} {sed_exp}"

        p = subprocess.Popen(sed_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output = p.communicate(input=input_str.encode())[0]

        output = output.decode("utf-8")

        return {Output.OUTPUT: output}
