import insightconnect_plugin_runtime
from .schema import UninstallSensorInput, UninstallSensorOutput, Input, Output, Component

# Custom imports below


class UninstallSensor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="uninstall_sensor",
            description=Component.DESCRIPTION,
            input=UninstallSensorInput(),
            output=UninstallSensorOutput(),
        )

    def run(self, params={}):
        id = params.get("id", "")
        try:
            # Returns single sensor if ID is supplied
            get_response = self.connection.carbon_black.get_object("/api/v1/sensor/%s" % id)
            if get_response.status_code != 200:
                return {"success": False}
            sensor_data = get_response.json_data
            sensor_data["uninstall"] = True
            put_response = self.connection.carbon_black.put_object("/api/v1/sensor/%s" % id, sensor_data)
            if not put_response.status_code == 204:
                return {"success": False}
        except Exception as ex:
            self.logger.error("Failed to uninstall sensor: %s", ex)
            raise ex
        return {"success": True}
