import json

import insightconnect_plugin_runtime
from .schema import (
    GetSandboxSuspiciousListInput,
    GetSandboxSuspiciousListOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import pytmv1


class GetSandboxSuspiciousList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sandbox_suspicious_list",
            description=Component.DESCRIPTION,
            input=GetSandboxSuspiciousListInput(),
            output=GetSandboxSuspiciousListOutput(),
        )

    def run(self, params={}):
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        submit_id = params.get(Input.ID)
        poll = params.get(Input.POLL)
        poll_time_sec = params.get(Input.POLL_TIME_SEC)
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.get_sandbox_suspicious_list(
            submit_id=submit_id, poll=poll, poll_time_sec=poll_time_sec
        )
        if "error" in response.result_code.lower():
            return response.error
        else:
            # Json load suspicious list objects
            sandbox_suspicious_list_resp = []
            for i in response.response.dict().get("items"):
                sandbox_suspicious_list_resp.append(json.loads(json.dumps(i)))
            # Return results
            self.logger.info("Returning Results...")
            return {Output.SANDBOX_SUSPICIOUS_LIST_RESP: sandbox_suspicious_list_resp}
