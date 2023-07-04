import insightconnect_plugin_runtime
import time
from .schema import (
    PollSandboxSuspiciousListInput,
    PollSandboxSuspiciousListOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import json


class PollSandboxSuspiciousList(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="poll_sandbox_suspicious_list",
            description=Component.DESCRIPTION,
            input=PollSandboxSuspiciousListInput(),
            output=PollSandboxSuspiciousListOutput(),
        )

    def run(self, params={}):
        """Run the trigger"""
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        poll = params.get(Input.POLL)
        poll_time_sec = params.get(Input.POLL_TIME_SEC)
        task_id = params.get(Input.ID)

        while True:
            # Make Action API Call
            self.logger.info("Making API Call...")
            response = client.get_sandbox_suspicious_list(submit_id=task_id, poll=poll, poll_time_sec=poll_time_sec)
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while polling the sandbox suspicious list.",
                    assistance="Check the input parameters and try again.",
                    data=response.error,
                )
            # Json load suspicious list objects
            sandbox_suspicious_list_resp = []
            for item in response.response.dict().get("items"):
                sandbox_suspicious_list_resp.append(json.loads(json.dumps(item)))
            # Return result
            self.logger.info("Returning Results...")
            self.send({Output.SANDBOX_SUSPICIOUS_LIST_RESP: sandbox_suspicious_list_resp})
            # Sleep before next run
            time.sleep(params.get(Input.INTERVAL, 1800))
