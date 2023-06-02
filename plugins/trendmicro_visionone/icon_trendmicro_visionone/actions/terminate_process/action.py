import insightconnect_plugin_runtime
from .schema import (
    TerminateProcessInput,
    TerminateProcessOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class TerminateProcess(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="terminate_process",
            description=Component.DESCRIPTION,
            input=TerminateProcessInput(),
            output=TerminateProcessOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        process_identifiers = params.get(Input.PROCESS_IDENTIFIERS)
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = {Output.MULTI_RESPONSE: []}
        for i in process_identifiers:
            if i.get("endpoint_name") and i.get("agent_guid"):
                response = client.terminate_process(
                    pytmv1.ProcessTask(
                        endpointName=i.get("endpoint_name"),
                        agentGuid=i.get("agent_guid"),
                        fileSha1=i["file_sha1"],
                        description=i.get("description", ""),
                        fileName=i.get("filename", ""),
                    )
                )
            elif i.get("endpoint_name") and not i.get("agent_guid"):
                response = client.terminate_process(
                    pytmv1.ProcessTask(
                        endpointName=i.get("endpoint_name"),
                        fileSha1=i["file_sha1"],
                        description=i.get("description", ""),
                        fileName=i.get("filename", ""),
                    )
                )
            elif i.get("agent_guid") and not i.get("endpoint_name"):
                response = client.terminate_process(
                    pytmv1.ProcessTask(
                        agentGuid=i.get("agent_guid"),
                        fileSha1=i["file_sha1"],
                        description=i.get("description", ""),
                        fileName=i.get("filename", ""),
                    )
                )
            else:
                raise PluginException(
                    cause="Neither Endpoint Name nor Agent GUID provided.",
                    assistance="Please check the provided parameters and try again.",
                )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while terminating process.",
                    assistance="Please check the process identifiers and try again.",
                    data=response.errors,
                )
            else:
                multi_resp[Output.MULTI_RESPONSE].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
