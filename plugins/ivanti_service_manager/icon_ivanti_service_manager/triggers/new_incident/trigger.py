import insightconnect_plugin_runtime
import time
from .schema import NewIncidentInput, NewIncidentOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException


class NewIncident(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_incident", description=Component.DESCRIPTION, input=NewIncidentInput(), output=NewIncidentOutput()
        )

    def run(self, params={}):
        # Set frequency and a list of initial incident numbers
        frequency = params.get(Input.FREQUENCY)
        incidents = self.connection.ivanti_service_manager_api.get_all_incidents().get("value")
        self.logger.info("Initializing trigger")

        while True:
            try:
                # Get a new list of incidents
                new_incidents = self.connection.ivanti_service_manager_api.get_all_incidents().get("value")
                # Check the new list of incidents against current list
                for incident in new_incidents:
                    if incident not in incidents:
                        # Record new incidents
                        incidents.append(incident)
                        # Use self.send(Info) to return new information
                        self.logger.info(f"New incident found: {str(incident['IncidentNumber'])}")
                        self.send({Output.INCIDENT: incident})

                # Sleep for frequency amount of time before running the loop again
                time.sleep(frequency)

            except Exception as error:
                raise PluginException(
                    cause="An error occurred while reading incidents",
                    assistance="Please look at log for details",
                    data=error,
                )
