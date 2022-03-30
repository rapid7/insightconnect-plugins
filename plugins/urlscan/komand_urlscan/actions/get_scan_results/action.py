import json

import requests

import insightconnect_plugin_runtime

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_urlscan.util.constants import SCAN_RESULTS
from komand_urlscan.util.util import Util
from .schema import GetScanResultsInput, GetScanResultsOutput, Input, Output, Component


class GetScanResults(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan_results",
            description=Component.DESCRIPTION,
            input=GetScanResultsInput(),
            output=GetScanResultsOutput(),
        )

    def run(self, params={}):
        response = requests.get(
            f"{self.connection.server}/result/{params[Input.SCAN_ID]}",
            headers=self.connection.headers,
        )

        try:
            json_response = response.json()
        except json.JSONDecodeError as e:
            raise PluginException(
                cause="Received an unexpected response from the Urlscan API.",
                assistance=f"(non-JSON or no response was received). Response was: {response.text}",
                data=e,
            )

        if response.status_code != 200:
            if response.status_code == 404:
                raise PluginException(
                    cause="The requested scan results were not found.",
                    assistance="If you are running this action directly after a new scan, you may need to add a delay "
                               "to ensure the scan results "
                    "are available when they are requested (typically ~5-10 seconds is sufficient.",
                )

            if "message" in json_response and "description" in json_response:
                raise PluginException(cause=json_response.get("message"), assistance=json_response.get("description"))

            raise PluginException(
                cause="Received an unexpected response from the Urlscan API.",
                assistance=f"If the problem persists, please contact support. Response was: {response.text}",
            )

        try:
            data = json_response["data"]
            screenshot_urls = json_response["task"]["screenshotURL"]
        except KeyError as e:
            raise PluginException(
                cause="Received an unexpected response from the Urlscan API. ",
                assistance=f"Please ensure your scan report is ready and that you're using a valid scan ID: Response was: {response.text}",
                data=e,
            )

        data["screenshotURL"] = screenshot_urls

        return {
            Output.SCAN_RESULTS: Util.update_properties(data, SCAN_RESULTS),
            Output.TASK: json_response.get("task", {}),
            Output.PAGE: json_response.get("page", {}),
            Output.LISTS: json_response.get("lists", {}),
            Output.META: json_response.get("meta", {}),
            Output.STATS: json_response.get("stats", {}),
            Output.VERDICTS: json_response.get("verdicts", {}),
        }
