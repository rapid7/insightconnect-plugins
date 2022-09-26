import insightconnect_plugin_runtime
import time
from datetime import datetime, timedelta

from .schema import GetIncidentsInput, GetIncidentsOutput, Input, Output, Component
# Custom imports below

ARMORBLOX_INCIDENT_API_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

class GetIncidents(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_incidents',
                description=Component.DESCRIPTION,
                input=GetIncidentsInput(),
                output=GetIncidentsOutput())

    def run(self, params={}):
        """Run the trigger"""
        fetch_interval = int(params.get(Input.INTERVAL))
        last_fetch_time = datetime.today() - timedelta(days=1)        
        last_fetch_time = last_fetch_time.strftime(ARMORBLOX_INCIDENT_API_TIME_FORMAT)                                                           
        while True:
            events = self.connection.api.get_incidents(last_fetch_time)
            if len(events) != 0:
                last_fetch_time = datetime.strptime(events[-1]['date'], ARMORBLOX_INCIDENT_API_TIME_FORMAT)
                # Adding 1 second to avoid the dupliaction of last fetched incident
                last_fetch_time = (last_fetch_time + timedelta(seconds=1)).strftime(ARMORBLOX_INCIDENT_API_TIME_FORMAT)
            self.send({Output.INCIDENTS: events})
            time.sleep(fetch_interval)

