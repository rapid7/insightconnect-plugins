import insightconnect_plugin_runtime
from .schema import GetTaskResultInput, GetTaskResultOutput, Input, Output, Component

# Custom imports below
import pytmv1


class GetTaskResult(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_task_result",
            description=Component.DESCRIPTION,
            input=GetTaskResultInput(),
            output=GetTaskResultOutput(),
        )

    def run(self, params={}):
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        task_id = params.get(Input.TASK_ID)
        poll = params.get(Input.POLL)
        poll_time_sec = params.get(Input.POLL_TIME_SEC)
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.get_base_task_result(
            task_id=task_id,
            poll=poll,
            poll_time_sec=poll_time_sec,
        )
        if "error" in response.result_code.lower():
            return response
        else:
            self.logger.info("Returning Results...")
            return response.response.dict()
