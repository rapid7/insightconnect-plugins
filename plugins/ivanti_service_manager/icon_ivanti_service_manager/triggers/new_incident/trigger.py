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
        # Set frequency and file name
        frequency = params.get("frequency, 10")
        cache_file_name = "cached_incidents_ids"

        # Record the first set of incidents
        with insightconnect_plugin_runtime.helper.open_cachefile(cache_file_name) as cache_file:
            self.logger.info(f"Found or created cache file: {cache_file_name}")
            cached_ids = {incident_id.strip() for incident_id in cache_file.readlines()}
            self.logger.info(f"Cached IDs: {cached_ids}")

        while True:
            try:
                # Check the new list of incidents against current list
                incidents = self.connection.ivanti_service_manager_api.get_all_incidents().get("value")
                new_ids = set()

                for incident in incidents:
                    incident_id = str(incident["IncidentNumber"])
                    if incident_id not in cached_ids:
                        # Record new incidents
                        cached_ids.add(incident_id)
                        new_ids.add(incident_id)
                        # Use self.send(Info) to return new information
                        self.logger.info(f"New incident found: {incident_id}")
                        self.send({"incident": incident})
                time.sleep(frequency)
            except Exception as error:
                raise PluginException(
                    cause=f"An error occurred while reading incidents",
                    assistance="Please look at log for details",
                    data=error,
                )
