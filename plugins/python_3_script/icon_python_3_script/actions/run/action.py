import os
import subprocess  # nosec B404
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Union
from uuid import uuid4

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_python_3_script.util.constants import (
    DEFAULT_ENCODING,
    DEFAULT_PROCESS_TIMEOUT,
    RUN_FUNCTION_TEMPLATE,
)
from icon_python_3_script.util.util import extract_output_from_stdout

from .schema import Component, Input, RunInput, RunOutput


class Run(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run", description=Component.DESCRIPTION, input=RunInput(), output=RunOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        function_ = params.get(Input.FUNCTION, "")
        input_parameters = params.get(Input.INPUT, {})
        timeout = params.get(Input.TIMEOUT, DEFAULT_PROCESS_TIMEOUT)
        # END INPUT BINDING - DO NOT REMOVE

        if timeout <= 0:
            raise PluginException(
                cause="Invalid timeout value specified.",
                assistance="Please make sure the timeout value is greater than 0 and try again.",
            )

        # Check if dependencies need to be installed
        if self.connection.dependencies:
            self.connection.ensure_dependencies()

        self.logger.info(f"Input: (below)\n\n{input_parameters}\n")
        self.logger.info(f"Function: (below)\n\n{function_}\n")
        self.logger.info(f"Timeout: {timeout}\n")

        try:
            output = self._execute_function_as_process(
                function_, input_parameters, self.connection.script_credentials, timeout, self.connection.interpreter
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

    def _execute_function_as_process(
        self,
        function_: str,
        parameters: Dict[str, Any],
        credentials: Dict[str, Any],
        timeout: Optional[int] = DEFAULT_PROCESS_TIMEOUT,
        interpreter: str = sys.executable,
    ) -> Union[Dict[str, Any], None]:
        """
        Execute a function as a separate process and return its data.

        :param function_: The declaration of the run function to execute.
        :type: str

        :param parameters: The input parameters to pass to the function.
        :type: Dict[str, Any]

        :param credentials: The credentials to pass to the function.
        :type: Dict[str, Any]

        :param timeout: Timeout in minutes for function execution.
        :type: Optional[int]

        :param interpreter: Path to the Python interpreter to use.
        :type: str

        :return: The result of the function execution.
        :rtype: Union[Dict[str, Any], None]
        """

        execution_id = f"Python3Script-ActionRun-{uuid4()}"
        execution_file = self._create_execution_file(execution_id, function_, parameters)
        execution_environment = {
            **os.environ,
            "SCRIPT_USERNAME": credentials.get("username", ""),
            "SCRIPT_PASSWORD": credentials.get("password", ""),
            "SCRIPT_SECRET_KEY": credentials.get("secret_key", ""),
            "SCRIPT_SECRET_CREDENTIAL_1": credentials.get("secret_credential_1", ""),
            "SCRIPT_SECRET_CREDENTIAL_2": credentials.get("secret_credential_2", ""),
            "SCRIPT_SECRET_CREDENTIAL_3": credentials.get("secret_credential_3", ""),
        }

        try:
            output = subprocess.check_output(  # nosec B603, B607
                [interpreter, execution_file.name],
                shell=False,
                stderr=subprocess.PIPE,
                timeout=timeout * 60,
                env=execution_environment,
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
    def _create_execution_file(execution_id: str, function_: str, parameters: Dict[str, Any]) -> Path:
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
