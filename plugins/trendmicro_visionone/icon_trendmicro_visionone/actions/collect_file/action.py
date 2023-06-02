import insightconnect_plugin_runtime
from .schema import CollectFileInput, CollectFileOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class CollectFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="collect_file",
            description=Component.DESCRIPTION,
            input=CollectFileInput(),
            output=CollectFileOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        collect_files = params.get(Input.COLLECT_FILES)
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = {Output.MULTI_RESPONSE: []}
        for i in collect_files:
            if i.get("endpoint_name") and i.get("agent_guid"):
                response = client.collect_file(
                    pytmv1.FileTask(
                        endpointName=i.get("endpoint_name"),
                        agentGuid=i.get("agent_guid"),
                        filePath=i["file_path"],
                        description=i.get("description", ""),
                    )
                )
            elif i.get("endpoint_name") and not i.get("agent_guid"):
                response = client.collect_file(
                    pytmv1.FileTask(
                        endpointName=i.get("endpoint_name"),
                        filePath=i["file_path"],
                        description=i.get("description", ""),
                    )
                )
            elif i.get("agent_guid") and not i.get("endpoint_name"):
                response = client.collect_file(
                    pytmv1.FileTask(
                        agentGuid=i.get("agent_guid"),
                        filePath=i["file_path"],
                        description=i.get("description", ""),
                    )
                )
            else:
                raise PluginException(
                    cause="Neither Endpoint Name nor Agent GUID provided.",
                    assistance="Please check the provided parameters and try again.",
                )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while collecting file.",
                    assistance="Please check the provided parameters and try again.",
                    data=response.errors,
                )
            else:
                multi_resp[Output.MULTI_RESPONSE].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
