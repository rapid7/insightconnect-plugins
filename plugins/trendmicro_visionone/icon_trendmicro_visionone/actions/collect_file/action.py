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
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        collect_files = params.get(Input.COLLECT_FILES)
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = {"multi_response": []}
        for i in collect_files:
            response = client.collect_file(
                pytmv1.FileTask(
                    endpointName=i["endpoint"],
                    filePath=i["file_path"],
                    description=i.get("description", ""),
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while collecting file.",
                    assistance="Please check the provided parameters and try again.",
                    data=response.errors,
                )
            else:
                multi_resp["multi_response"].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
