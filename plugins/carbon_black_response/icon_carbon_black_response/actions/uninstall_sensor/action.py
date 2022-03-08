import cbapi.errors
import insightconnect_plugin_runtime
from .schema import UninstallSensorInput, UninstallSensorOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException


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
            sensor_data = get_response.json_data
            sensor_data["uninstall"] = True
            put_response = self.connection.carbon_black.put_object("/api/v1/sensor/%s" % id, sensor_data)
        except cbapi.errors.ServerError as ex:
            if ex.error_code == 404:
                raise PluginException(
                    cause="Invalid sensor ID. The server ID was not found on the server.",
                    assistance="Please verify that the provided sensor ID exists.",
                ) from cbapi.errors.ServerError(404, "Invalid Sensor")
            return {"success": False}
        return {"success": True}
