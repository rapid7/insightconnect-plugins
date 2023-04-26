import insightconnect_plugin_runtime
from .schema import (
    SubmitUrlsToSandboxInput,
    SubmitUrlsToSandboxOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import pytmv1


class SubmitUrlsToSandbox(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_urls_to_sandbox",
            description=Component.DESCRIPTION,
            input=SubmitUrlsToSandboxInput(),
            output=SubmitUrlsToSandboxOutput(),
        )

    def run(self, params={}):
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        urls = params.get(Input.URL)
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        # Make Action API Call
        self.logger.info("Making API Call...")
        submit_urls_resp = {"submit_urls_resp": []}
        for i in urls:
            response = client.submit_urls_to_sandbox(i)
            if "error" in response.result_code.lower():
                return response.errors
            else:
                submit_urls_resp["submit_urls_resp"].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return submit_urls_resp
