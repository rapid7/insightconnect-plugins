import insightconnect_plugin_runtime
from .schema import RunCommandInput, RunCommandOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class RunCommand(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_command", description=Component.DESCRIPTION, input=RunCommandInput(), output=RunCommandOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        device_id = params.get(Input.DEVICE_ID, 0)
        policy_id = params.get(Input.POLICY_ID, 0)
        command = params.get(Input.COMMAND, "")
        patches = params.get(Input.PATCHES, [])
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        if device_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Device ID must be a positive integer")

        if policy_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Policy ID must be a positive integer")

        command_payload = {"command_type_name": command}

        if command == "InstallUpdate":
            command_payload["args"] = patches
        elif command == "PolicyTest":
            command_payload["command_type_name"] = f"policy_{policy_id}_test"
        elif command == "PolicyRemediate":
            command_payload["command_type_name"] = f"policy_{policy_id}_remediate"

        self.logger.info(
            f"Running {command_payload['command_type_name']} command with the following "
            f"arguments: {command_payload.get('args', 'No arguments defined')}"
        )
        self.connection.automox_api.run_device_command(org_id, device_id, command_payload)
        return {Output.SUCCESS: True}
