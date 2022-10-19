import sys
from typing import Any, Dict

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from .schema import Component, Input, RunInput, RunOutput

sys.path.append("/var/cache/python_dependencies/lib/python3.8/site-packages")

INDENTATION_CHARACTER = " "


class Run(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run", description=Component.DESCRIPTION, input=RunInput(), output=RunOutput()
        )

    def run(self, params={}):
        function_ = params.get(Input.FUNCTION, "").replace("\t", INDENTATION_CHARACTER)
        function_ = self._add_credentials_to_function(function_)

        self.logger.info(f"Input: (below)\n\n{params.get(Input.INPUT)}\n")
        self.logger.info(f"Function: (below)\n\n{function_}\n")

        try:
            out = self._exec_python_function(function_=function_, params=params)
        except Exception as error:
            raise PluginException(cause="Could not run supplied script", data=str(error))
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
    def _exec_python_function(function_: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes python function and returning it's data
        :param function_: Python script function
        :type: str
        :param params: Parameters to be added to the function
        :type: Dict[str, Any]
        :return: Output of the functions response
        :rtype: Dict[str, Any]
        """

        exec(function_)  # noqa: B102
        function_name = function_.split(" ")[1].split("(")[0]
        out = locals()[function_name](params.get(Input.INPUT))
        return out

    def _add_credentials_to_function(self, function_: str, indentation_character: str = INDENTATION_CHARACTER) -> str:
        """
        This function adds credentials to the function entered by the user. It looks for connection script
        credentials: username, password, secret_key, and adds all of them to variables inside of the function.
        :param function_: Python script function
        :type: str
        :param indentation_character: Indentation character used in function
        :type: str
        :return: Function string appended by the credential variables
        :rtype: str
        """

        credentials_definition = []

        for key, value in clean(self.connection.script_credentials).items():
            self.logger.info(f"{key}={value}")
            credentials_definition.append(f'{indentation_character}{key}="{value}"')

        function_lines = function_.split("\n")
        function_lines = [function_lines[0]] + credentials_definition + function_lines[1:]
        return "\n".join(function_lines)
