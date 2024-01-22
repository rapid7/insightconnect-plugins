import insightconnect_plugin_runtime
from .schema import (
    RunCustomScriptInput,
    RunCustomScriptOutput,
    Input,
    Output,
    Component,
)

from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class RunCustomScript(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_custom_script",
            description=Component.DESCRIPTION,
            input=RunCustomScriptInput(),
            output=RunCustomScriptOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        agent_guid = params.get(Input.AGENT_GUID, "")
        endpoint_name = params.get(Input.ENDPOINT_NAME, "")
        parameter = params.get(Input.PARAMETER, "")
        file_name = params.get(Input.FILE_NAME)
        description = params.get(Input.DESCRIPTION, "")
        # Prepare the request based on the conditions
        if agent_guid and endpoint_name:
            script_request = pytmv1.CustomScriptRequest(
                agent_guid=agent_guid,
                endpoint_name=endpoint_name,
                parameter=parameter,
                file_name=file_name,
                description=description,
            )
        elif agent_guid and not endpoint_name:
            script_request = pytmv1.CustomScriptRequest(
                agent_guid=agent_guid, parameter=parameter, file_name=file_name, description=description
            )
        elif endpoint_name and not agent_guid:
            script_request = pytmv1.CustomScriptRequest(
                endpoint_name=endpoint_name, parameter=parameter, file_name=file_name, description=description
            )
        else:
            # Handle case where both agent_guid and endpoint_name are not provided
            raise PluginException(
                cause="Missing required parameters.",
                assistance="Both 'agent_guid' and 'endpoint_name' cannot be empty.",
            )
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.script.run(script_request)
        # Check for error in the response
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while running a custom script.",
                assistance="Please check the provided inputs and try again.",
                data=response,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: response.response.dict().get("items")}
