import insightconnect_plugin_runtime
from .schema import (
    GetSandboxSubmissionStatusInput,
    GetSandboxSubmissionStatusOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class GetSandboxSubmissionStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sandbox_submission_status",
            description=Component.DESCRIPTION,
            input=GetSandboxSubmissionStatusInput(),
            output=GetSandboxSubmissionStatusOutput(),
        )

    def run(self, params={}):
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        task_id = params.get(Input.TASK_ID)
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.get_sandbox_submission_status(submit_id=task_id)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting sandbox submission status.",
                assistance="Please check the task ID and try again.",
                data=response,
            )
        else:
            self.logger.info("Returning Results...")
            return response.response.dict()
