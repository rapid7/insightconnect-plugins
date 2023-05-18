import insightconnect_plugin_runtime
from .schema import GetTaskResultInput, GetTaskResultOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class GetTaskResult(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_task_result",
            description=Component.DESCRIPTION,
            input=GetTaskResultInput(),
            output=GetTaskResultOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        task_id = params.get(Input.TASK_ID)
        poll = params.get(Input.POLL)
        poll_time_sec = params.get(Input.POLL_TIME_SEC)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.get_base_task_result(
            task_id=task_id,
            poll=poll,
            poll_time_sec=poll_time_sec,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while retrieving the task result.",
                assistance="Please check the task ID and try again.",
                data=response,
            )
        else:
            self.logger.info("Returning Results...")
            return response.response.dict()
