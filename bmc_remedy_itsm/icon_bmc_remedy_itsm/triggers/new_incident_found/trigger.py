import komand
from .schema import NewIncidentFoundInput, NewIncidentFoundOutput, Input, Output, Component
# Custom Imports below
import re
import time
import urllib.parse
import maya
import requests
import json
from typing import Optional
from komand.exceptions import PluginException


class NewIncidentFound(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='new_incident_found',
            description=Component.DESCRIPTION,
            input=NewIncidentFoundInput(),
            output=NewIncidentFoundOutput())

    def run(self, params={}):
        description_query = params.get(Input.DESCRIPTION_QUERY)
        compiled_query = self._check_and_compile_query(description_query)
        self.maya_initial_incident_date = self._get_initial_incident_info()

        while True:
            new_incident_json = self._get_new_incidents()
            self._check_new_incidents_and_send(compiled_query, self.maya_initial_incident_date, new_incident_json)

            interval = params.get(Input.INTERVAL, 15)
            self.logger.info(f"Sleeping for {interval} seconds\n")
            time.sleep(interval)
            self.logger.info("\n")  # Just want a break in the log between each loop

    def _check_new_incidents_and_send(self, compiled_query: object,
                                      maya_initial_incident_date: maya.MayaDT,
                                      new_incident_json: dict) -> None:
        """
        This will check an interval's worth of incidents, see if we have any new ones, and return those if they
        match the subject query (if available).

        This will also set the target time to the most recent incident if any are found, regardless of if they
        are returned.

        :param compiled_query: a compiled regex query (re.compile("blah"))
        :param maya_initial_incident_date: MayaDT - last time checked for incidents
        :param new_incident_json: dict - Payload from the last get_new_incidents call in descending order by time
        :return:
        """
        new_incident_date = new_incident_json.get("entries")[0].get("values").get("Submit Date")
        self.logger.info(f"Checking for incidents newer than: {new_incident_date}")
        maya_new_incident_date = maya.parse(new_incident_date)

        if maya_new_incident_date > maya_initial_incident_date:  # New incident was found
            new_date = maya_new_incident_date  # Reset the time as fast as possible, so we don't miss any new inidents while we're processing this set.

            for incident in new_incident_json.get("entries"):  # Check each incident and see if we have more than one new incident
                incident_to_check = incident.get("values")
                maya_new_date = maya.parse(incident_to_check.get("Submit Date"))

                if maya_new_date > maya_initial_incident_date:  # We have a new incident, see if we need to send it
                    new_incident_description = incident_to_check.get("Description")
                    self.logger.info(f"New incident found with description: {new_incident_description}")

                    if not compiled_query or compiled_query.match(new_incident_description):
                        self.logger.info(f"Returning incident with description: {new_incident_description}")
                        self.send({Output.INCIDENT: komand.helper.clean(incident)})
                    else:
                        self.logger.info(f"Incident did not match query: {compiled_query}")
            self.maya_initial_incident_date = new_date

    def _get_new_incidents(self) -> dict:
        """
        This goes out and grabs all the incidents from the server and returns them in descending order by time.

        :return: dict - json content from get new incidents
        """
        new_incident_query_endpoint = "/api/arsys/v1/entry/HPD:IncidentInterface?sort=Submit Date.desc"
        new_incident_url = urllib.parse.urljoin(self.connection.url, new_incident_query_endpoint)
        headers = self.connection.make_headers_and_refresh_token()  # This will refresh the auth token

        try:
            new_incidents_result = requests.get(new_incident_url, headers=headers)
        except requests.HTTPError as e:
            raise PluginException(
                cause=f"An unexpected error code was returned. Status code was {new_incidents_result.status_code}.",
                assistance="Please contact support with the status code and error information.",
                data=new_incidents_result.text) from e

        try:
            ret_val = new_incidents_result.json()
        except json.JSONDecodeError as e:
            raise PluginException(PluginException.Preset.INVALID_JSON) from e

        return ret_val

    def _get_initial_incident_info(self) -> maya.MayaDT:
        """
        Finds the most recent incident available on the BMC server and returns that time as a MayaDT

        :return: MayaDT - Submitted date of the most recent incident on the server
        """
        initial_query_endpoint = "/api/arsys/v1/entry/HPD:IncidentInterface?sort=Submit Date.desc&limit=1"
        get_incident_url = urllib.parse.urljoin(self.connection.url, initial_query_endpoint)
        headers = self.connection.make_headers_and_refresh_token()
        initial_incident_request = requests.get(get_incident_url, headers=headers)

        try:
            initial_incident_request.raise_for_status()
        except requests.HTTPError as e:
            raise PluginException(
                cause=f"An unexpected error code was returned. Status code was {initial_incident_request.status_code}.",
                assistance="Please contact support with the status code and error information.",
                data=initial_incident_request.text) from e

        try:
            initial_incident_json = initial_incident_request.json()
        except json.JSONDecodeError as e:
            raise PluginException(PluginException.Preset.INVALID_JSON) from e

        initial_incident_id = initial_incident_json.get("entries")[0].get("values").get("Request ID")
        initial_incident_submitted_date = initial_incident_json.get("entries")[0].get("values").get("Submit Date")

        self.logger.info(f"Initial incident found with ID: {initial_incident_id} "
                         f"and Submit Date: {initial_incident_submitted_date}")

        try:
            maya_initial_incident_date = maya.parse(initial_incident_submitted_date)
        except Exception as e:
            raise PluginException(cause="Can not parse date returned by BMC server",
                                  assistance=f"The BMC server returned a date in an "
                                             f"unexpected format: {initial_incident_submitted_date}") from e

        return maya_initial_incident_date

    def _check_and_compile_query(self, description_query: str) -> Optional[object]:
        """
        This takes a regex string and compiles it to regex. If no string is given it will return None

        :param description_query: regex as string
        :return: re.Pattern (re.compile()) OR None if no string was given
        """
        compiled_query = None

        if description_query:
            try:
                compiled_query = re.compile(description_query)
            except re.error as e:
                raise PluginException(cause=f"Invalid regex used for Description Query: {description_query}",
                                      assistance="Please check your input for Description Query for errors") from e

        return compiled_query
