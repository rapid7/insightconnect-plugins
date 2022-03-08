import cbapi.errors
import insightconnect_plugin_runtime
from .schema import UninstallSensorInput, UninstallSensorOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from cbapi.errors import ObjectNotFoundError, ApiError, UnauthorizedError, ServerError


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
        sensorId = params.get("id", "")
        try:
            # Returns single sensor if ID is supplied
            get_response = self.connection.carbon_black.get_object(f"/api/v1/sensor/{sensorId}")
            sensor_data = get_response.json_data
            sensor_data["uninstall"] = True
            self.connection.carbon_black.put_object(f"/api/v1/sensor/{sensorId}", sensor_data)
        except ApiError as ex:
            if isinstance(ex, ObjectNotFoundError):
                raise PluginException(
                    cause="Invalid sensor ID. The server ID was not found on the server.",
                    assistance="Please verify that the provided sensor ID exists.",
                ) from None
            elif isinstance(ex, UnauthorizedError):
                raise PluginException(preset=ConnectionTestException.Preset.UNAUTHORIZED) from None
            elif isinstance(ex, ServerError):
                raise PluginException(preset=ConnectionTestException.Preset.SERVER_ERROR) from None
            return {"success": False}
        return {"success": True}
