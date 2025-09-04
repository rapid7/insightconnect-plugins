import json
import time
from datetime import datetime
from typing import Any, Dict, List

import insightconnect_plugin_runtime
import requests
from dateutil import parser
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

# Custom imports below
from icon_azure_ad_admin.util.komand_clean_with_nulls import remove_null_and_clean

from .schema import Component, Input, Output, RiskDetectionInput, RiskDetectionOutput

DEFAULT_REQUESTS_TIMEOUT = 30
DETECTED_RISK_DATE_FIELD = "detectedDateTime"


class RiskDetection(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="risk_detection",
            description=Component.DESCRIPTION,
            input=RiskDetectionInput(),
            output=RiskDetectionOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        risk_level = params.get(Input.RISK_LEVEL)
        frequency = params.get(Input.FREQUENCY, 60)
        # END INPUT BINDING - DO NOT REMOVE

        # Initialize the trigger with starting data point
        current_risks = self._get_risks(risk_level)
        latest_risk_detection_time = self._get_latest_risk_detection_time(current_risks)

        while True:
            # Retrieve current 'riskDetection' data
            self.logger.info("Retrieving risks data from the API...")
            current_risks = self._get_risks(risk_level, latest_risk_detection_time)

            # Filter all results by their 'detectedDateTime', returning only results whose time is greater than
            # the last risk detection 'detectedDateTime'.
            new_risks = list(
                filter(
                    lambda element: self.parse_datetime(element.get(DETECTED_RISK_DATE_FIELD))
                    > latest_risk_detection_time,
                    current_risks,
                )
            )

            if new_risks:
                self.logger.info(f"Found new {len(new_risks)} risks. Returning...")
                latest_risk_detection_time = self._get_latest_risk_detection_time(new_risks)
                for risk in new_risks:
                    self.send({Output.RISK: risk})
            else:
                self.logger.info(f"No new risks found. Sleeping for {frequency} seconds...")
            time.sleep(frequency)

    @staticmethod
    def parse_datetime(input_datetime_str: str) -> datetime:
        """
        Parse a string representation of a datetime object and return a :class:`datetime.datetime` object.
        This function accepts a string formatted according to a standard datetime format, primarily supporting ISO 8601.

        :param input_datetime_str: The string representation of the datetime to be parsed.
        :type: str

        :returns: A datetime object representing the parsed datetime.
        :rtype: datetime
        """

        return parser.parse(input_datetime_str, ignoretz=True)

    def _get_latest_risk_detection_time(self, risk_detections: List[Dict[str, Any]]) -> datetime:
        """
        Retrieve the latest risk detection time from a list of risk detections.

        :param risk_detections: A list of risk detection records, where each record is a dictionary containing details about the risk detection event.
        :type: List[Dict[str, Any]]

        :return: The latest risk detection time found in the provided list.
        :rtype: datetime
        """

        if not risk_detections:
            return datetime.utcnow()
        return self.parse_datetime(risk_detections[-1].get(DETECTED_RISK_DATE_FIELD))

    def _get_risks(self, risk_level: str, latest_risk_detection_time: datetime = None) -> List[Dict[str, Any]]:
        """
        Retrieve the risk detection event from MS Graph API.

        :param risk_level: Risk detection level for results to be filtered on.
        :type: str

        :param latest_risk_detection_time: Determines whether API should return all results greater than specific time or not. Defaults to None.
        :type: datetime

        :return: The latest risk detection time found in the provided list.
        :rtype: List[Dict[str, Any]]
        """

        # The 'riskLevel' filter condition to be applied when it's not 'all'
        risk_filter = f" and riskLevel eq '{risk_level}'" if risk_level != "all" else ""

        # Sending request to the MS Graph API with detectedDateTime filter, it allows to return only new detections
        # Setup $top to 500 as it's the maximum number of record that can be returned using that endpoint
        response = requests.get(
            "https://graph.microsoft.com/v1.0/identityProtection/riskDetections",
            headers=self.connection.get_headers(self.connection.get_auth_token()),
            params=clean(
                {
                    "$filter": (
                        f"{DETECTED_RISK_DATE_FIELD} gt {latest_risk_detection_time.isoformat()}Z" + risk_filter
                        if latest_risk_detection_time
                        else ""
                    ),
                    "$top": 500,
                }
            ),
            timeout=DEFAULT_REQUESTS_TIMEOUT,
        )

        if not response.status_code == 200:
            raise PluginException(
                cause=f"Risk Detections returned an unexpected response: {response.status_code}",
                assistance="Please contact support for help.",
                data=response.text,
            )

        try:
            # Cleaning out the response records and sorting them out manually in ascending order
            # because MS Graph API was not ordering them properly
            return sorted(
                remove_null_and_clean(response.json()["value"]),
                key=lambda element: self.parse_datetime(element.get(DETECTED_RISK_DATE_FIELD)),
            )
        except KeyError:
            raise PluginException(
                cause="Unexpected output format.",
                assistance="The output from Azure Active Directory was not in the expected format. Please contact support for help.",
                data=response.text,
            )
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
