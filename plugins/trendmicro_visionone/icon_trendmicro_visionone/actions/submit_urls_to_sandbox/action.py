import insightconnect_plugin_runtime
from .schema import (
    SubmitUrlsToSandboxInput,
    SubmitUrlsToSandboxOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class SubmitUrlsToSandbox(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_urls_to_sandbox",
            description=Component.DESCRIPTION,
            input=SubmitUrlsToSandboxInput(),
            output=SubmitUrlsToSandboxOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        urls = params.get(Input.URLS)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.submit_urls_to_sandbox(*urls)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while submitting URLs to the sandbox.",
                assistance="Please check the provided url(s) and try again.",
                data=response.errors,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.SUBMIT_URLS_RESP: response.response.dict().get("items")}
