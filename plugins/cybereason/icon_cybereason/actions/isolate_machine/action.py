import insightconnect_plugin_runtime
from .schema import IsolateMachineInput, IsolateMachineOutput, Input, Output, Component

# Custom imports below


class IsolateMachine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="isolate_machine",
            description=Component.DESCRIPTION,
            input=IsolateMachineInput(),
            output=IsolateMachineOutput(),
        )

    def run(self, params={}):
        malop_id = params.get(Input.MALOP_ID, None)
        quarantine = params.get(Input.QUARANTINE_STATE)
        pylum_id = self.connection.api.get_sensor_details(params.get(Input.SENSOR)).get("pylumId")

        if quarantine:
            response = self.connection.api.isolate_machines([pylum_id], malop_id)
        else:
            response = self.connection.api.un_isolate_machines([pylum_id], malop_id)

        success = False
        if response[pylum_id] == "Succeeded":
            success = True

        return {Output.MACHINE_ID: pylum_id, Output.SUCCESS: success}
