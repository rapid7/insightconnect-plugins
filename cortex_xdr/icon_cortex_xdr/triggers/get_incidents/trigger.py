import insightconnect_plugin_runtime
import time

from .schema import GetIncidentsInput, GetIncidentsOutput, Input, Output, Component
# Custom imports below

from ...util.util import Util


DEFAULT_TIME_FIELD = "creation_time"


class GetIncidents(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_incidents',
                description=Component.DESCRIPTION,
                input=GetIncidentsInput(),
                output=GetIncidentsOutput())

    def run(self, params={}):
        end_time = Util.now_ms()
        start_time = params.get(Input.START_TIME, None)
        time_field = params.get(Input.TIME_FIELD, DEFAULT_TIME_FIELD)

        self.logger.info(f"Initializing get_incidents trigger for cortex xdr plugin.")

        while True:
            incidents = self.connection.xdr_api.get_incidents(
                from_time=start_time,
                to_time=end_time,
                time_field=time_field
            )

            # TODO: implement time checking to avoid duplicate incidents across executions of this while loop.
            for incident in incidents:
                self.send({Output.INCIDENT: incident})

            time.sleep(params.get("interval", 5))

            start_time = end_time
            end_time = Util.now_ms()
