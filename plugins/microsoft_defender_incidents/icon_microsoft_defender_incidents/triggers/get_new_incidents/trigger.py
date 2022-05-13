import datetime
import time

import insightconnect_plugin_runtime

# Custom imports below
from icon_microsoft_defender_incidents.util.tools import Defaults

from ...util.tools import generate_query_params
from .schema import Component, GetNewIncidentsInput, GetNewIncidentsOutput, Input, Output


class GetNewIncidents(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_new_incidents",
            description=Component.DESCRIPTION,
            input=GetNewIncidentsInput(),
            output=GetNewIncidentsOutput(),
        )

    def run(self, params={}):
        interval = abs(params.get(Input.INTERVAL, Defaults.DEFAULT_TRIGGER_INTERVAL))
        status = params.get(Input.STATUS, "All")
        last_update_time = (
            datetime.datetime.fromisoformat(params.get(Input.LAST_UPDATE_TIME)).replace(tzinfo=None)
            if params.get(Input.LAST_UPDATE_TIME)
            else None
        )
        assigned_to = params.get(Input.ASSIGNED_TO)
        request_elapsed_time = datetime.timedelta(seconds=interval)
        while True:
            time_ago = datetime.datetime.now() - (request_elapsed_time + datetime.timedelta(seconds=interval))
            response, request_elapsed_time = self.connection.client.list_incidents(
                generate_query_params(status, time_ago, last_update_time, assigned_to)
            )
            if response:
                self.send({Output.INCIDENTS: response})
            else:
                self.logger.info("No new incidents have been found!")
            self.logger.info(f"Sleeping for {interval} seconds...\n")
            time.sleep(interval)
