import insightconnect_plugin_runtime
from .schema import (
    DownloadSandboxInvestigationPackageInput,
    DownloadSandboxInvestigationPackageOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import pytmv1
import time
from datetime import datetime
import base64


class DownloadSandboxInvestigationPackage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_sandbox_investigation_package",
            description=Component.DESCRIPTION,
            input=DownloadSandboxInvestigationPackageInput(),
            output=DownloadSandboxInvestigationPackageOutput(),
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
        response = client.download_sandbox_investigation_package(
            submit_id=submit_id, poll=poll, poll_time_sec=poll_time_sec
        )
        if "error" in response.result_code.lower():
            return response
        else:
            # Make filename with timestamp
            name = "Trend Micro Download Sandbox Investigation Package "
            timestamp = time.time()
            date_time = datetime.fromtimestamp(timestamp)
            str_date_time = date_time.strftime("%d_%m_%Y_%H_%M_%S")
            file_name = name + str_date_time + ".zip"
            self.logger.info("Returning Results...")
            return {
                Output.FILE: {
                    "content": base64.b64encode(response.response.content).decode(),
                    "filename": file_name,
                }
            }
