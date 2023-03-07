import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import RunRemoteScriptInput, RunRemoteScriptOutput, Input, Output, Component

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
                cause=f"No script id provided to execute.",
                assistance=f"Please select a script to execute from the SentinelOne console.",
            )
        task_description = params.get(Input.TASK_DESCRIPTION)
        if not task_description:
            raise PluginException(
                cause=f"No task description provided.",
                assistance=f"Please provide a task description for the script.",
            )

        script_timeout = params.get(Input.TIMEOUT, 3600)
        if script_timeout < 60 or script_timeout > 172800:
            # Timeout outside of allowed parameters - use default value instead
            script_timeout = 3600

        input_params = params.get(Input.INPUT_PARAMETERS, "")
        password = params.get(Input.PASSWORD, "")
        if password:
            if len(password) <= 10 or " " in password:
                raise PluginException(
                    cause="Invalid password.",
                    assistance="Password must have more than 10 characters and cannot contain whitespace.",
                )

        output_dest = params.get(Input.OUTPUT_DESTINATION, "")
        output_dir = params.get(Input.OUTPUT_DIRECTORY, "")
        if output_dest == "Local" and not output_dir:
            raise PluginException(
                cause=f"Local output destination selected but no output directory provided.",
                assistance=f"Please provide an output directory.",
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
