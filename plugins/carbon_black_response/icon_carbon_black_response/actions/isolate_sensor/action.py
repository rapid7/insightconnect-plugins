import insightconnect_plugin_runtime
from .schema import IsolateSensorInput, IsolateSensorOutput

# Custom imports below
from cbapi.response.models import Sensor


class IsolateSensor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="isolate_sensor",
            description="Isolates a sensor from the network",
            input=IsolateSensorInput(),
            output=IsolateSensorOutput(),
        )

    def run(self, params={}):
        try:
            sensor = self.connection.carbon_black.select(Sensor).where("hostname:" + params.get("hostname")).first()
            length = len(self.connection.carbon_black.select(Sensor).where("hostname:" + params.get("hostname")))
            self.logger.info(
                f"List size is: {length}"
            )
            sensor.isolate()
        except Exception as ex:
            self.logger.error("Failed to isolate sensor: %s", ex)
            raise ex
        return {"success": True}

    def test(self):
        if self.connection.test():
            return {}
