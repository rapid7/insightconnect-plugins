import subprocess
from komand.exceptions import PluginException


class Helper:
    @staticmethod
    def process(input_str, sed_list, sed_opts):

        if sed_list and sed_list[0] != "":
            sed_exp = sed_list[0]
            sed_exp = f" -e '{Helper.shell_quote(sed_exp)}'"
            for item in sed_list[1:]:
                sed_exp = f"{sed_exp} -e '{Helper.shell_quote(item)}' "
        else:
            raise PluginException(
                cause='Illegal user input',
                assistance='The sed expression must not be an empty string'
            )

        sed_cmd = f"sed {Helper.shell_quote(sed_opts)} {sed_exp}"
        try:
            p = subprocess.Popen(sed_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        except Exception as e:
            raise PluginException(
                cause='Problem with process',
                assistance=e.message
            )

        return p.communicate(input=input_str)[0]

    @staticmethod
    def shell_quote(s):
        return s.replace("'", "'\\''")
