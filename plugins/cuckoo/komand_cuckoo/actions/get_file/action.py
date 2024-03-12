import insightconnect_plugin_runtime
from .schema import GetFileInput, GetFileOutput, Input, Output

# Custom imports below
import requests
import base64


class GetFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_file",
            description="Returns the binary content of the file matching the specified SHA256 hash",
            input=GetFileInput(),
            output=GetFileOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        sha256 = params.get(Input.SHA256, "")
        endpoint = f"{server}/files/get/{sha256}"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            if response.headers.get("Content-Type", "").startswith("application/octet-stream"):
                content = response.content
                return {Output.CONTENTS: base64.b64encode(content).decode("UTF-8")}

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
