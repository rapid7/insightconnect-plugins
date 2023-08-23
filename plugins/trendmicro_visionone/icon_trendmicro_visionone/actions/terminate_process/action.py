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
        # Build processes list
        processes = []
        for process_identifier in process_identifiers:
            if process_identifier.get("endpoint_name") and process_identifier.get(
                "agent_guid"
            ):
                processes.append(
                    pytmv1.ProcessTask(
                        endpointName=process_identifier.get("endpoint_name"),
                        agentGuid=process_identifier.get("agent_guid"),
                        fileSha1=process_identifier["file_sha1"],
                        description=process_identifier.get("description", ""),
                        fileName=process_identifier.get("filename", ""),
                    )
                )
            elif process_identifier.get("endpoint_name") and not process_identifier.get(
                "agent_guid"
            ):
                processes.append(
                    pytmv1.ProcessTask(
                        endpointName=process_identifier.get("endpoint_name"),
                        fileSha1=process_identifier["file_sha1"],
                        description=process_identifier.get("description", ""),
                        fileName=process_identifier.get("filename", ""),
                    )
                )
            elif process_identifier.get("agent_guid") and not process_identifier.get(
                "endpoint_name"
            ):
                processes.append(
                    pytmv1.ProcessTask(
                        agentGuid=process_identifier.get("agent_guid"),
                        fileSha1=process_identifier["file_sha1"],
                        description=process_identifier.get("description", ""),
                        fileName=process_identifier.get("filename", ""),
                    )
                )
            else:
                raise PluginException(
                    cause="Neither Endpoint Name nor Agent GUID provided.",
                    assistance="Please check the provided parameters and try again.",
                )
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.terminate_process(*processes)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while terminating process.",
                assistance="Please check the process identifiers and try again.",
                data=response.errors,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: response.response.dict().get("items")}
