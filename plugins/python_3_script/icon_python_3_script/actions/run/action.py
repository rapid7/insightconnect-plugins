import subprocess  # nosec B404
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Union
from uuid import uuid4

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from icon_python_3_script.util.constants import (
    DEFAULT_ENCODING,
    DEFAULT_PROCESS_TIMEOUT,
    INDENTATION_CHARACTER,
    RUN_FUNCTION_TEMPLATE,
)
from icon_python_3_script.util.util import extract_output_from_stdout

from .schema import Component, Input, RunInput, RunOutput

sys.path.append("/var/cache/python_dependencies/lib/python3.9/site-packages")


class Run(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run", description=Component.DESCRIPTION, input=RunInput(), output=RunOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        function_ = params.get(Input.FUNCTION, "")
        input_parameters = params.get(Input.INPUT, {})
        timeout = params.get(Input.TIMEOUT)
        # END INPUT BINDING - DO NOT REMOVE

        if timeout <= 0:
            raise PluginException(
                cause="Invalid timeout value specified.",
                assistance="Please make sure the timeout value is greater than 0 and try again.",
            )

        self.logger.info(f"Input: (below)\n\n{input_parameters}\n")
        self.logger.info(f"Function: (below)\n\n{function_}\n")
        self.logger.info(f"Timeout: {timeout}\n")

        try:
            output = self._execute_function_as_process(
                function_, input_parameters, self.connection.script_credentials, timeout
            )
        except Exception as error:
            raise PluginException(cause="Could not run supplied script", data=error) from None
        try:
            if output is None:
                raise PluginException(
                    cause="Output type was None", assistance="Ensure that output has a non-None data type"
                )
            return output
        except UnboundLocalError:
            raise PluginException(
                cause="No output was returned.", assistance="Check supplied script to ensure that it returns output"
            )

    @staticmethod
    def _exec_python_function(function_: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes python function and returning its data
        :param function_: Python script function
        :type: str

        :param params: Parameters to be added to the function
        :type: Dict[str, Any]

        :return: Output of the functions response
        :rtype: Dict[str, Any]
        """

        exec(function_)  # noqa: B102
        function_name = function_.split(" ")[1].split("(")[0]
        return locals()[function_name](params.get(Input.INPUT))

    def _execute_function_as_process(
        self,
        function_: str,
        parameters: Dict[str, Any],
        credentials: Dict[str, Any],
        timeout: Optional[int] = DEFAULT_PROCESS_TIMEOUT,
    ) -> Union[Dict[str, Any], None]:
        """
        Execute a function as a separate process and return its data.

        :param function_: The declaration of the run function to execute.
        :type: str

        :param parameters: The input parameters to pass to the function.
        :type: Dict[str, Any]

        :param credentials: The credentials to pass to the function.
        :type: Dict[str, Any]

        :return: The result of the function execution.
        :rtype: Union[Dict[str, Any], None]
        """

        execution_id = f"Python3Script-ActionRun-{uuid4()}"
        execution_file = self.create_execution_file(execution_id, function_, parameters)
        execution_arguments = ["python", execution_file.name]

        if credentials:
            for key, value in credentials.items():
                if value:
                    execution_arguments.append(f"--{key}={value}")

        try:
            output = subprocess.check_output(  # nosec B603, B607
                execution_arguments,
                shell=False,
                stderr=subprocess.PIPE,
                timeout=timeout * 60,
            )
            return extract_output_from_stdout(output.decode(DEFAULT_ENCODING), execution_id)
        except subprocess.CalledProcessError as error:
            raise PluginException(error.stderr.decode(DEFAULT_ENCODING).replace(execution_id, "")) from None
        except subprocess.TimeoutExpired:
            raise PluginException(f"Function timed out after {timeout} minutes.") from None
        finally:
            if execution_file.is_file():
                execution_file.unlink()

    @staticmethod
    def create_execution_file(execution_id: str, function_: str, parameters: Dict[str, Any]) -> Path:
        """
        Create an execution file with the given execution ID, function name, and parameters.

        :param execution_id: A unique identifier for the execution.
        :type: str

        :param function_: The body of the function to be executed.
        :type: str

        :param parameters: A dictionary of parameters to be passed to the function.
        :type: Dict[str, Any]

        :return: The path to the created execution file.
        :rtype: Path
        """

        filename = f"{execution_id}.py"
        function_name = function_.split(" ")[1].split("(")[0]
        with open(filename, "w", encoding=DEFAULT_ENCODING) as file_:
            file_.write(
                RUN_FUNCTION_TEMPLATE.format(
                    execution_id=execution_id,
                    function_=function_,
                    function_name=function_name,
                    parameters=parameters,
                )
            )
        return Path(filename)

    @staticmethod
    def _add_credentials_to_function(
        function_: str, credentials: Dict[str, str], indentation_character: str = INDENTATION_CHARACTER
    ) -> str:
        """
        This function adds credentials to the function entered by the user. It looks for connection script
        credentials: username, password, secret_key, secret_credential_1, secret_credential_2, secret_credential_3 and adds all of them to variables inside the function.
        :param function_: Python script function
        :type: str

        :param credentials: Credentials to be added
        :type: Dict[str, str]

        :param indentation_character: Indentation character used in function
        :type: str

        :return: Function string appended by the credential variables
        :rtype: str
        """

        credentials_definition = []

        for key, value in clean(credentials).items():
            credentials_definition.append(f'{indentation_character}{key}="{value}"')

        function_lines = function_.split("\n")
        function_lines = [function_lines[0]] + credentials_definition + function_lines[1:]
        return "\n".join(function_lines)

    @staticmethod
    def _check_indentation_character(function_: str) -> str:
        """
        This function returns the indentation character that is used in the input python's function
        :param function_: Python script function
        :type: str

        :return: Indentation character that is used
        :rtype: str
        """

        indentation_character = ""
        first_new_line_index = function_.index("\n")
        for character in function_[first_new_line_index + 1 :]:
            if character in ("\t", " "):
                indentation_character += character
            else:
                return indentation_character
