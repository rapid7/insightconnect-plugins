import insightconnect_plugin_runtime
from .schema import GetSensorInput, GetSensorOutput, Input, Output, Component


class GetSensor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sensor",
            description=Component.DESCRIPTION,
            input=GetSensorInput(),
            output=GetSensorOutput(),
        )

    def run(self, params={}):
        return {Output.SENSOR: self.connection.api.get_sensors(params.get(Input.INDICATOR))}
