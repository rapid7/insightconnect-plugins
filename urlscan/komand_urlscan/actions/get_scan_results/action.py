import komand
from .schema import GetScanResultsInput, GetScanResultsOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import requests
import json


class GetScanResults(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_scan_results',
            description=Component.DESCRIPTION,
            input=GetScanResultsInput(),
            output=GetScanResultsOutput())

    def run(self, params={}):
        response = requests.get(f"{self.connection.server}/result/{params[Input.SCAN_ID]}",
                                headers=self.connection.headers)

        try:
            js = response.json()
        except json.JSONDecodeError as e:
            raise PluginException(cause="Received an unexpected response from the Urlscan API. ",
                                  assistance=f"(non-JSON or no response was received). Response was: {response.text}",
                                  data=e)

        # Non-200 status code responses should have a JSON payload containing message, description, and status code
        # Display those values to the user for assistance purposes.
        # See: https://urlscan.io/about-api/#errors
        if response.status_code != 200:
            if response.status_code == 404:
                raise PluginException(cause="The requested scan results were not found. ",
                                      assistance="If you are running this action directly after a new scan, "
                                                 "you may need to add a delay to ensure the scan results "
                                                 "are available when they are requested (typically ~5-10 seconds is sufficient.")

            if ('message' in js) and ('description' in js):
                raise PluginException(cause=js['message'], assistance=js['description'])

            raise PluginException(cause="Received an unexpected response from the Urlscan API. ",
                                  assistance=f"If the problem persists, please contact support. Response was: {response.text}")

        try:
            ret = js["data"]
            su = js["task"]["screenshotURL"]
        except KeyError as e:
            raise PluginException(cause="Received an unexpected response from the Urlscan API. ",
                                  assistance=f"Please ensure your scan report is ready and that you're using a valid scan ID: Response was: {response.text}",
                                  data=e)

        ret["screenshotURL"] = su

        return {
            Output.SCAN_RESULTS: ret
        }
