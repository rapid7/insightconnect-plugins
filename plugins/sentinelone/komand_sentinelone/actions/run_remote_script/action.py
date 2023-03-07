import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import RunRemoteScriptInput, RunRemoteScriptOutput, Input, Output, Component
from komand_sentinelone.util.constants import (
    SCRIPT_TIMEOUT_LOWER_LIMIT,
    SCRIPT_TIMEOUT_UPPER_LIMIT,
    SCRIPT_TIMEOUT_DEFAULT,
)
from komand_sentinelone.util.helper import check_password_meets_requirements

# Custom imports below


class RunRemoteScript(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_remote_script",
            description=Component.DESCRIPTION,
            input=RunRemoteScriptInput(),
            output=RunRemoteScriptOutput(),
        )

    def run(self, params={}):
        agent_ids = params.get(Input.IDS)
        script_id = params.get(Input.SCRIPT_ID)
        if not script_id:
            raise PluginException(
                cause="No script id provided to execute.",
                assistance="Please select a script to execute from the SentinelOne console.",
            )
        task_description = params.get(Input.TASK_DESCRIPTION)
        if not task_description:
            raise PluginException(
                cause="No task description provided.",
                assistance="Please provide a task description for the script.",
            )

        script_timeout = params.get(Input.TIMEOUT, SCRIPT_TIMEOUT_DEFAULT)
        if script_timeout < SCRIPT_TIMEOUT_LOWER_LIMIT or script_timeout > SCRIPT_TIMEOUT_UPPER_LIMIT:
            # Timeout outside of allowed parameters - use default value instead
            script_timeout = SCRIPT_TIMEOUT_DEFAULT

        input_params = params.get(Input.INPUT_PARAMETERS, "")
        password = params.get(Input.PASSWORD, "")
        if password:
            check_password_meets_requirements(password)

        output_dest = params.get(Input.OUTPUT_DESTINATION, "")
        output_dir = params.get(Input.OUTPUT_DIRECTORY, "")
        if output_dest == "Local" and not output_dir:
            raise PluginException(
                cause="Local output destination selected but no output directory provided.",
                assistance="Please provide an output directory.",
            )

        user_filter = {}
        if agent_ids:
            user_filter = {"ids": agent_ids}
        data = {
            "scriptRuntimeTimeoutSeconds": script_timeout,
            "scriptId": script_id,
            "outputDestination": output_dest,
            "taskDescription": task_description,
            "inputParams": input_params,
            "outputDirectory": output_dir,
            "password": password,
        }

        affected = self.connection.run_remote_script(user_filter, data)

        return {Output.AFFECTED: affected}
