import insightconnect_plugin_runtime
from .schema import (
    DownloadCustomScriptInput,
    DownloadCustomScriptOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import time
from datetime import datetime
import base64


class DownloadCustomScript(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_custom_script",
            description=Component.DESCRIPTION,
            input=DownloadCustomScriptInput(),
            output=DownloadCustomScriptOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        script_id = params.get(Input.SCRIPT_ID)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.download_custom_script(
            script_id=script_id,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while downloading a custom script.",
                assistance="Please check the provided script id and try again.",
                data=response,
            )
        # Make filename with timestamp
        name = "Trend Micro Custom Script "
        timestamp = time.time()
        date_time = datetime.fromtimestamp(timestamp)
        str_date_time = date_time.strftime("%d_%m_%Y_%H_%M_%S")
        file_type = ".ps1"
        if ("#!/bin/bash" in response.response.text) or ("#!/bin/sh" in response.response.text):
            file_type = ".sh"
        file_name = name + str_date_time + file_type
        # Return results
        self.logger.info("Returning Results...")
        # self.logger.info(response.response.__dict__)
        return {
            Output.FILE: {
                "content": base64.b64encode(response.response.text).decode(),
                "filename": file_name,
            }
        }
