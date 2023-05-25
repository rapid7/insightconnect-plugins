import insightconnect_plugin_runtime
from .schema import (
    SubmitFileToSandboxInput,
    SubmitFileToSandboxOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from base64 import b64decode


class SubmitFileToSandbox(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_file_to_sandbox",
            description=Component.DESCRIPTION,
            input=SubmitFileToSandboxInput(),
            output=SubmitFileToSandboxOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        file = params.get(Input.FILE)
        document_password = params.get(Input.DOCUMENT_PASSWORD)
        archive_password = params.get(Input.ARCHIVE_PASSWORD)
        arguments = params.get(Input.ARGUMENTS)
        if not arguments:
            arguments = "None"
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.submit_file_to_sandbox(
            file=b64decode(file.get("content")),
            file_name=file.get("filename"),
            document_password=document_password,
            archive_password=archive_password,
            arguments=arguments,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while submitting the file to the sandbox.",
                assistance="Please check the provided inputs and try again.",
                data=response,
            )
        else:
            self.logger.info("Returning Results...")
            return {
                Output.ARGUMENTS: response.response.dict().get("arguments", ""),
                Output.DIGEST: response.response.dict().get("digest", {}),
                Output.ID: response.response.dict().get("id", ""),
            }
