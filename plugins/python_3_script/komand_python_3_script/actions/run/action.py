import sys

import komand
from komand.exceptions import PluginException

from .schema import RunOutput, RunInput, Component, Input

sys.path.append("/var/cache/python_dependencies/lib/python3.7/site-packages")


class Run(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run", description=Component.DESCRIPTION, input=RunInput(), output=RunOutput()
        )

    def run(self, params={}):
        self.logger.info(f"Input: (below)\n\n{params.get(Input.INPUT)}\n")
        func = params.get(Input.FUNCTION)
        self.logger.info(f"Function: (below)\n\n{func}\n")
        func = self._add_credentials_to_function(func)

        try:
            out = self._exec_python_function(func=func, params=params)
        except Exception as e:
            raise PluginException(cause="Could not run supplied script", data=str(e))
        try:
            if out is None:
                raise PluginException(
                    cause="Output type was None", assistance="Ensure that output has a non-None data type"
                )
            return out
        except UnboundLocalError:
            raise PluginException(
                cause="No output was returned.", assistance="Check supplied script to ensure that it returns output"
            )

    @staticmethod
    def _exec_python_function(func, params):
        exec(func)  # noqa: B102
        funcname = func.split(" ")[1].split("(")[0]
        out = locals()[funcname](params.get(Input.INPUT))
        return out

    def _add_credentials_to_function(self, func: str) -> str:
        credentials_definition = []
        username = self.connection.script_credentials.get("username")
        password = self.connection.script_credentials.get("password")
        secret_key = self.connection.script_credentials.get("secret_key")

        if username:
            credentials_definition.append(f"\tusername='{username}'")
        if password:
            credentials_definition.append(f"\tpassword='{password}'")
        if secret_key:
            credentials_definition.append(f"\tsecret_key='{secret_key}'")

        func_lines = func.split("\n")
        func_lines = [func_lines[0]] + credentials_definition + func_lines[1:]

        return "\n".join(func_lines)
