import insightconnect_plugin_runtime
from .schema import IncidentChangedInput, IncidentChangedOutput, Input, Output, Component

# Custom imports below
import time
from typing import Dict, Any, List, Generator, Tuple
from icon_servicenow.util.constants import MAXIMUM_NUMBER_OF_REQUESTS, PAGINATION_OFFSET


class IncidentChanged(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="incident_changed",
            description=Component.DESCRIPTION,
            input=IncidentChangedInput(),
            output=IncidentChangedOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        interval = params.get(Input.INTERVAL, 5)
        monitored_fields = params.get(Input.MONITORED_FIELDS, "")
        system_ids = params.get(Input.SYSTEM_IDS, [])
        query = params.get(Input.QUERY, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Initial pull of all the incidents with conversion generators to dict.
        # We need to store all of them in memory for the comparison.
        previous_incidents = dict(self.get_all_incidents(monitored_fields, system_ids=system_ids, query=query))

        while True:
            # Pull all the incidents
            current_incidents = self.get_all_incidents(monitored_fields, system_ids=system_ids, query=query)

            # Compare previous and new incident results. Using dict to speed up compute time.
            # After comparison the previous_incidents variable is being updated to current_incidents
            for key, value in current_incidents:
                if key in previous_incidents and value != previous_incidents.get(key):
                    if changed_fields := self._parse_new_fields(value, previous_incidents.get(key, {})):
                        self.send({Output.SYSTEM_ID: key, Output.CHANGED_FIELDS: changed_fields})
                previous_incidents[key] = value

            # Sleep for configured frequency in minutes
            self.logger.info(f"Sleeping for {interval} minutes...")
            time.sleep(interval * 60)

    def get_all_incidents(
        self, monitored_fields: str, system_ids: List[str] = None, **kwargs
    ) -> Generator[Tuple[str, Dict[str, Any]], Any, None]:
        """
        Get all the incidents from API. Uses offset to get data from all pages.

        :param monitored_fields: Field names to be monitored separated by comma.
        :type: str

        :param system_ids: List of system IDs. That parameter is optional. If not set defaults to all incidents pulled.
        :type: List[str]

        :return: A generator that yields a tuple consisting of a string and a dictionary.
        :rtype: Generator[Tuple[str, Dict[str, Any]], Any, None]
        """

        query = "ORDERBYDESCsys_created_on"
        if system_ids:
            query = "^OR".join(list(map(lambda system_id: f"sys_id={system_id}", system_ids))) + f"^{query}"

        incidents = []
        for offset in range(0, MAXIMUM_NUMBER_OF_REQUESTS * PAGINATION_OFFSET, PAGINATION_OFFSET):
            if new_incidents := (
                self.connection.request.make_request(
                    self.connection.incident_url,
                    "GET",
                    params={
                        "sysparm_limit": PAGINATION_OFFSET,
                        "sysparm_fields": f"sys_id,{monitored_fields}",
                        "sysparm_query": query,
                        "sysparm_offset": offset,
                    },
                    **kwargs,
                )
                .get("resource", {})
                .get("result", [])
            ):
                incidents.extend(new_incidents)
            else:
                break
        return self._generate_results(incidents)

    @staticmethod
    def _parse_new_fields(current_incident: Dict[str, Any], previous_incident: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parses and returns a dictionary containing the changed fields in the current incident
        compared to the previous incident.

        :param current_incident: A dictionary representing the current incident.
        :type: Dict[str, Any]

        :param previous_incident: A dictionary representing the previous incident.
        :type: Dict[str, Any]

        :return: A dictionary containing the new fields in the current incident.
        :rtype: Dict[str, Any]
        """

        changed_fields = {}
        for key, value in current_incident.items():
            previous_incident_value = previous_incident.get(key)
            if value != previous_incident_value:
                changed_fields[key] = {
                    "current": value,
                    "previous": previous_incident_value,
                }
        return changed_fields

    @staticmethod
    def _generate_results(list_of_incidents: List[Dict[str, Any]]) -> Generator[Tuple[str, Dict[str, Any]], Any, None]:
        """
        Generate results based on the list of incidents.

        This method takes a list of incidents as input and generates results based on the provided incidents.
        It returns a generator that yields a tuple consisting of a string and a dictionary. The solution
        was made in order to save the memory during trigger runtime.

        :param list_of_incidents: A list of incidents represented as dictionaries.
        :type: List[Dict[str, Any]]

        :return: A generator that yields a tuple consisting of a string and a dictionary.
        :rtype: Generator[Tuple[str, Dict[str, Any]], Any, None]
        """

        return ((incident.pop("sys_id", ""), incident) for incident in list_of_incidents)
