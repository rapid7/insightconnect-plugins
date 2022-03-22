import insightconnect_plugin_runtime
from .schema import UnisolateSensorInput, UnisolateSensorOutput

# Custom imports below
from cbapi.response.models import Sensor


class UnisolateSensor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="unisolate_sensor",
            description="Brings a sensor back into the network",
            input=UnisolateSensorInput(),
            output=UnisolateSensorOutput(),
        )

    def run(self, params={}):
        try:
            sensor = self.connection.carbon_black.select(Sensor).where("hostname:" + params.get("hostname")).first()
            sensor.unisolate()
        except Exception as ex:
            self.logger.error("Failed to unisolate sensor: %s", ex)
            raise ex

        return {"success": True}

    def test(self):
        if self.connection.test():
            return {}
