import json

import requests

import insightconnect_plugin_runtime

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SubmitUrlForScanInput, SubmitUrlForScanOutput, Input, Output, Component
from ...util.constants import ERROR_KEY_WORDS


class SubmitUrlForScan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_url_for_scan",
            description=Component.DESCRIPTION,
            input=SubmitUrlForScanInput(),
            output=SubmitUrlForScanOutput(),
        )

    def run(self, params=None):
        if params is None:
            params = {}
        body = {"url": params.get(Input.URL)}
        if params.get(Input.PUBLIC):
            body["public"] = "on"

        response = requests.post(f"{self.connection.server}/scan", headers=self.connection.headers, data=body)

        try:
            json_response = response.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(
                cause="Received an unexpected response from the Urlscan API. ",
                assistance=f"(non-JSON or no response was received). Response was: {response.text}",
            )

        if "uuid" in json_response:
            return {Output.WAS_SCAN_SKIPPED: False, Output.SCAN_ID: json_response["uuid"]}

        if "status" in json_response:
            if json_response.get("status") == 401:
                raise PluginException(preset=PluginException.Preset.API_KEY)
            elif json_response.get("status") == 429:
                raise PluginException(cause="API limit error.", assistance=json_response.get("message", ""))

        description = json_response.get("description", "").lower()
        if (
            json_response
            and "scan prevented" in json_response.get("message", "").lower()
            and any(key_word in description for key_word in ERROR_KEY_WORDS)
        ):
            self.logger.error(f'Description: {json_response.get("description")}. Message: {json_response.get("message")}')
            return {Output.WAS_SCAN_SKIPPED: True, Output.SCAN_ID: ""}

        if ("message" in json_response) and ("description" in json_response):
            raise PluginException(cause=f"{json_response.get('message')}.", assistance=f"{json_response.get('description')}.")

        raise PluginException(
            cause="Received an unexpected response from the Urlscan API.",
            assistance=f"If the problem persists, please contact support. Response was: {response.text}",
        )
