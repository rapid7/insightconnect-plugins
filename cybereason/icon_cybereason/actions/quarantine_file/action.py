import insightconnect_plugin_runtime
from .schema import QuarantineFileInput, QuarantineFileOutput, Input, Output, Component
# Custom imports below


class QuarantineFile(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine_file',
                description=Component.DESCRIPTION,
                input=QuarantineFileInput(),
                output=QuarantineFileOutput())

    def run(self, params={}):
        sensor = params.get(Input.SENSOR)
        sensor_details = self.connection.api.get_sensor_details(sensor)
        sensor_guid = sensor_details['guid']
        sensor_name = sensor_details['machineName']        
        malop_id = params.get(Input.MALOP_ID)
        quarantine = params.get(Input.QUARANTINE)

        malop_data = self.connection.api.get_malop(malop_id)

        if not check_machine_in_malop():
            raise PluginException(
                cause="Sensor provided not related to the Malop ID Provided."
                assistance=f"Make sure that sensor provided is involved in the Malop - {malop_id}."
            )
        
        file_guids = self.get_file_guids(
            get_files_in_malop(self.connection.api.get_malop(malop_id)),
            sensor_name,
            sensor_guid,
            quarantine
        )
        
        if quarantine:
            action_type = "QUARANTINE_FILE"
        else:
            action_type = "UNQUARANTINE_FILE"

        actions = []
        for guid in file_guids:
            actions.append({"targetId": guid, "actionType": action_type})


        return {Output.REMEDIATE_ITEMS_RESPONSE: self.connection.api.remediate(
            self.connection.api.username,
            actions_by_machine
        )}

    def get_file_guids(self, files: list, machine_name: str, machine_guid: str, quarantine: bool) -> list:
        filters = [
            {
                "facetName": "elementDisplayName",
                "filterType": "ContainsIgnoreCase",
                "values": files
            },
            {
                "facetName": "ownerMachine",
                "filterType": "ContainsIgnoreCase",
                "values": [
                    machine_name
                ]
            }
        ]
        try:
            if quarantine:
                results = self.connection.api.get_visual_search(
                    requestedType = "File",
                    filters = filters,
                    customFields = ["ownerMachine"]
                )
            else:
                results = self.connection.api.get_visual_search(
                    requestedType = "QuarantineFile",
                    filters = filters,
                    customFields = ["quarantineFile"]
                )
        
        if quarantine:
            return [k for k in results.keys()]
        
        quarantined_file_guids = []
        for k in results.keys():
            try:
                quarantined_files = result[k]["elementValues"]["quarantineFile"]["elementValues"]
            except KeyError:
                continue
            for f in quarantined_files:
                quarantined_file_guids.append(f.get('guid'))

        return quarantined_file_guids

    @staticmethod
    def get_files_in_malop(malop_data: dict) -> list:
        try:
            element_values = malop_data["elementValues"]["primaryRootCauseElements"]["elementValues"]
        except KeyError:
            raise PluginException(
                cause="No root cause elements found for this Malop.",
                assistance="Please provide a Malop GUID of a Malop that has files involved.",
            )

        file_names = [e.get('name') for e in element_values if e.get("elementType") == "File"]
        
        if file_names:
            return file_names
        
        raise PluginException(
                cause="No files related to this Malop found.",
                assistance="Please provide a Malop GUID of a Malop that has files involved.",
            )

    @staticmethod
    def check_machine_in_malop(malop_data: dict, machine_guid: str) -> bool:
        try:
            element_values = malop_data["elementValues"]["affectedMachines"]["elementValues"]
        except KeyError:
            raise PluginException(
                cause="No affected machines found for this Malop.",
                assistance="Please provide a Malop GUID of a Malop that has machines involved.",
            )

        if [m for m in element_values if m.get("guid") == machine_guid]:
            return True

        return False
