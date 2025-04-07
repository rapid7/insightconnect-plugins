import insightconnect_plugin_runtime
from .schema import (
    RunRemoteScriptInput,
    RunRemoteScriptOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sentinelone.util.constants import (
    SCRIPT_TIMEOUT_LOWER_LIMIT,
    SCRIPT_TIMEOUT_UPPER_LIMIT,
    SCRIPT_TIMEOUT_DEFAULT,
)
from komand_sentinelone.util.helper import check_password_meets_requirements, clean


class RunRemoteScript(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_remote_script",
            description=Component.DESCRIPTION,
            input=RunRemoteScriptInput(),
            output=RunRemoteScriptOutput(),
        )

    def run(self, params={}):
        script_timeout = params.get(Input.TIMEOUT, SCRIPT_TIMEOUT_DEFAULT)
        password = params.get(Input.PASSWORD)
        code = params.get(Input.CODE)
        output_destination = params.get(Input.OUTPUTDESTINATION)
        output_directory = params.get(Input.OUTPUTDIRECTORY)
        ids = params.get(Input.IDS)

        if output_destination == "Local" and not output_directory:
            raise PluginException(
                cause="Local output destination selected but no output directory provided.",
                assistance="Please provide an output directory.",
            )

        if script_timeout not in range(SCRIPT_TIMEOUT_LOWER_LIMIT, SCRIPT_TIMEOUT_UPPER_LIMIT):
            script_timeout = SCRIPT_TIMEOUT_DEFAULT

        if password:
            check_password_meets_requirements(password)

        if code:
            self.connection.client.elevate_protected_actions_session({"data": {"code": code}})

        return {
            Output.AFFECTED: self.connection.client.run_remote_script(
                {
                    "filter": {"ids": ids} if ids else {},
                    "data": clean(
                        {
                            "scriptRuntimeTimeoutSeconds": script_timeout,
                            "scriptId": params.get(Input.SCRIPTID),
                            "outputDestination": output_destination,
                            "taskDescription": params.get(Input.TASKDESCRIPTION),
                            "inputParams": params.get(Input.INPUTPARAMETERS),
                            "outputDirectory": output_directory,
                            "password": password,
                        }
                    ),
                }
            )
            .get("data", [])
            .get("affected", 0)
        }
