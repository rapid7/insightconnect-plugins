import insightconnect_plugin_runtime
from .schema import UninstallSensorInput, UninstallSensorOutput, Input, Output, Component
# Custom imports below


class UninstallSensor(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='uninstall_sensor',
                description=Component.DESCRIPTION,
                input=UninstallSensorInput(),
                output=UninstallSensorOutput())

    def run(self, params={}):
        id = params.get("id", "")
        try:
            # Returns single sensor if ID is supplied
            sensor_data = self.connection.carbon_black.get_object("/api/v1/sensor/%s" % id)
            sensor_data["uninstall"] = True
            put_response = self.connection.carbon_black.put_object("/api/v1/sensor/%s" % id, sensor_data)
            sensor_data = self.connection.carbon_black.get_object("/api/v1/sensor/%s" % id)
            if not sensor_data["uninstall"]:
                return {"success": False}
        except Exception as ex:
            self.logger.error("Failed to uninstall sensor: %s", ex)
            raise ex
        return {"success": True}
