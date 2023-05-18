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


class GetSandboxSubmissionStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sandbox_submission_status",
            description=Component.DESCRIPTION,
            input=GetSandboxSubmissionStatusInput(),
            output=GetSandboxSubmissionStatusOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        task_id = params.get(Input.TASK_ID)
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
