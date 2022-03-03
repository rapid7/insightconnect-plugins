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
            out = response.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(
                cause="Received an unexpected response from the Urlscan API. ",
                assistance=f"(non-JSON or no response was received). Response was: {response.text}",
            )

        if "uuid" in out:
            return {Output.WAS_SCAN_SKIPPED: False, Output.SCAN_ID: out["uuid"]}

        if "status" in out:
            if out.get("status") == 401:
                raise PluginException(preset=PluginException.Preset.API_KEY)
            elif out.get("status") == 429:
                raise PluginException(cause="API limit error.", assistance=out.get("message", ""))

        description = out.get("description", "").lower()
        if (
            out
            and "scan prevented" in out.get("message", "").lower()
            and any(key_word in description for key_word in ERROR_KEY_WORDS)
        ):
            self.logger.error(f'Description: {out.get("description")}. Message: {out.get("message")}')
            return {Output.WAS_SCAN_SKIPPED: True, Output.SCAN_ID: ""}

        if ("message" in out) and ("description" in out):
            raise PluginException(cause=f"{out.get('message')}. ", assistance=f"{out.get('description')}.")

        raise PluginException(
            cause="Received an unexpected response from the Urlscan API. ",
            assistance=f"If the problem persists, please contact support. Response was: {response.text}",
        )
