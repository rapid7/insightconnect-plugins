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

        # record the first set of the thing you are checking
        with insightconnect_plugin_runtime.helper.open_cachefile(cache_file_name) as cache_file:
            self.logger.info(f"Found or created cache file: {cache_file_name}")
            cached_ids = {id.strip() for id in cache_file.readlines()}
            self.logger.info(f"Cached IDs: {cached_ids}")

        # Use a while true loop
        while True:
            try:
                # check the thing against what you have already
                incidents = self.connection.ivanti_service_manager_api.get_all_incidents()
                new_ids = set()

                for incident in incidents:
                    incident_id = str(incident["id"])
                    # if it's new use self.send(info)
                    if incident_id not in cached_ids:
                        # record current info
                        cached_ids.add(incident_id)
                        new_ids.add(incident_id)
                        # Use self.send(Info) to return information
                        self.logger.info(f"New incident found: {incident_id}")
                        self.send({"incident": incident})
                # sleep for frequency amount of time
                time.sleep(frequency)
            # add wee exception bit outside the while loop incase it dies
            except Exception as e:
                raise PluginException("An error occurred while reading incidents: {}".format(e))
