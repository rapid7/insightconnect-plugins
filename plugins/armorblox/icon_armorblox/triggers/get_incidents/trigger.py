import insightconnect_plugin_runtime
import time
from datetime import datetime, timedelta
from icon_armorblox.util.constants import (
    ARMORBLOX_INCIDENT_API_TIME_FORMAT,
    ARMORBLOX_INCIDENT_API_TIME_DELTA_IN_DAYS,
    DEFAULT_INTERVAL_VALUE,
)
from .schema import GetIncidentsInput, GetIncidentsOutput, Input, Output, Component

# Custom imports below


class GetIncidents(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_incidents",
            description=Component.DESCRIPTION,
            input=GetIncidentsInput(),
            output=GetIncidentsOutput(),
        )

    def run(self, params={}):
        """Run the trigger"""
        fetch_interval = params.get(Input.INTERVAL, DEFAULT_INTERVAL_VALUE)
        # First fetch
        last_fetch_time = (datetime.utcnow() - timedelta(days={ARMORBLOX_INCIDENT_API_TIME_DELTA_IN_DAYS})).strftime(
            {ARMORBLOX_INCIDENT_API_TIME_FORMAT}
        )
        while True:
            current_time = datetime.utcnow().replace(second=0).strftime({ARMORBLOX_INCIDENT_API_TIME_FORMAT})
            events = self.connection.api.get_incidents(from_date=last_fetch_time, to_date=current_time)
            if events:
                self.send({Output.INCIDENTS: events})
            else:
                self.logger.info(f"No events retrieved. Sleeping for {fetch_interval} seconds....")
            last_fetch_time = current_time
            time.sleep(fetch_interval)
