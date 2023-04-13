import insightconnect_plugin_runtime
from .schema import QuarantineFileInput, QuarantineFileOutput, Input, Output, Component

# Custom imports below
from icon_cybereason.util.api import CybereasonAPI


class QuarantineFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine_file",
            description=Component.DESCRIPTION,
            input=QuarantineFileInput(),
            output=QuarantineFileOutput(),
        )

    def run(self, params={}):
        sensor_details = self.connection.api.get_sensor_details(params.get(Input.SENSOR))
        malop_id = params.get(Input.MALOP_ID)
        quarantine = params.get(Input.QUARANTINE)
        malop_data = self.connection.api.get_malop(malop_id)
        sensor_guid = sensor_details.get("guid")
        sensor_machine_name = sensor_details.get("machineName")

        CybereasonAPI.check_machine_in_malop(malop_data, sensor_guid, malop_id)

        files_in_malop = CybereasonAPI.get_files_in_malop(malop_data)
        file_guids = self.connection.api.get_file_guids(files_in_malop, sensor_machine_name, quarantine)
        actions = CybereasonAPI.get_list_of_actions(quarantine, file_guids)
        return {
            Output.REMEDIATE_ITEMS_RESPONSE: self.connection.api.remediate(
                self.connection.api.username, {sensor_guid: actions}, malop_id=malop_id
            )
        }
