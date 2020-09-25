import insightconnect_plugin_runtime
import time
from .schema import IncidentCreatedInput, IncidentCreatedOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from datetime import datetime, timezone, timedelta
import pytz


class IncidentCreated(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='incident_created',
            description=Component.DESCRIPTION,
            input=IncidentCreatedInput(),
            output=IncidentCreatedOutput())
        self.last_poll_time = (datetime.now(tz=timezone.utc) - timedelta(seconds=1)).replace(microsecond=0)
        self.most_recent_system_id = ""
        self.last_sys_id = ""

    def poll(self, url, method, query, utc):
        response = self.connection.request.make_request(url, method, params=query)

        try:
            results = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        incidents = [(result.get("sys_created_on"), result.get("sys_id")) for result in results
                     if result.get("sys_created_on") is not None and result.get("sys_id") is not None]

        # Incidents stored from least to most recent date
        # Loop from most recent incident to least recent incident

        most_recent_incident = True
        for incident in sorted(incidents, reverse=True):
            if len(incident) == 2:
                if incident[0] != "" and incident[1] != "":
                    d = datetime.strptime(incident[0], "%Y-%m-%d %H:%M:%S")

                    # Turn offset naive date into offset aware date
                    date_aware = utc.localize(d)

                    sys_id = incident[1]

                    # Since descending date list, an incident that is after last polling time can break the loop
                    # Other condition ensures no duplicate triggers
                    if date_aware >= self.last_poll_time and sys_id != self.last_sys_id:
                        self.connection.logger.info(f"Found new incident: {sys_id}")
                        if most_recent_incident is True:
                            self.last_sys_id = sys_id
                            most_recent_incident = False
                        self.send({Output.SYSTEM_ID: sys_id})
                    else:
                        break
                else:
                    if incident[0] == "":
                        self.connection.logger.warning(f"Warning: An incident could not be read -- incident creation "
                                                       f"date could not be found. Verify that the created date field exists.")
                    else:
                        self.connection.logger.warning(f"Warning: An incident could not be read -- incident system id "
                                                       f"could not be found. Verify that the system id field exists.")

            else:
                self.connection.logger.warning(f'Warning: An incident could not be read -- the incident '
                                               f'did not have the necessary values.')

        # minus ~1 second to ensure that incidents between polls are not missed
        adjusted_poll = datetime.now(tz=timezone.utc) - timedelta(seconds=1)
        self.last_poll_time = adjusted_poll.replace(microsecond=0)

    def run(self, params={}):
        url = self.connection.incident_url
        method = "get"
        utc = pytz.timezone('UTC')

        # Pulls directly from SNOW db to grab creation date in UTC
        query = {"sysparm_display_value": False, "sysparm_query": "ORDERBYsys_created_on"}

        if params.get(Input.QUERY):
            query["sysparm_query"] = params.get(Input.QUERY) + "^ORDERBYsys_created_on"
        else:
            query["sysparm_query"] = "ORDERBYsys_created_on"

        while True:
            self.poll(url, method, query, utc)
            time.sleep(params.get(Input.INTERVAL, 5))
