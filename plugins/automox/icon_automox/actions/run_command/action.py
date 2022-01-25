import insightconnect_plugin_runtime
from .schema import RunCommandInput, RunCommandOutput, Input, Output, Component

# Custom imports below


class RunCommand(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_command", description=Component.DESCRIPTION, input=RunCommandInput(), output=RunCommandOutput()
        )

    def run(self, params={}):
        policy_id = params.get(Input.POLICY_ID)
        command = params.get(Input.COMMAND)
        command_payload = {"command_type_name": command}

        # Craft command and argument based on inputs which vary based on command being run
        if command == "InstallUpdate":
            command_payload["args"] = params.get(Input.PATCHES)
        elif command == "PolicyTest":
            command_payload["command_type_name"] = f"policy_{policy_id}_test"
        elif command == "PolicyRemediate":
            command_payload["command_type_name"] = f"policy_{policy_id}_remediate"

        self.logger.info(
            f"Running {command_payload['command_type_name']} command with the following "
            f"arguments: {command_payload.get('args', 'No arguments defined')}"
        )
        self.connection.automox_api.run_device_command(
            params.get(Input.ORG_ID), params.get(Input.DEVICE_ID), command_payload
        )
        return {Output.SUCCESS: True}
