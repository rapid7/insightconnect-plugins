import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean, convert_dict_to_snake_case
from icon_microsoft_intune.util.helpers import handle_key_names_exceptions
from .schema import GetDeviceInput, GetDeviceOutput, Input, Output, Component

# Custom imports below


class GetDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_device", description=Component.DESCRIPTION, input=GetDeviceInput(), output=GetDeviceOutput()
        )

    def run(self, params={}):
        return {
            Output.DEVICE: convert_dict_to_snake_case(
                handle_key_names_exceptions(clean(self.connection.api.get_device(params.get(Input.DEVICE_ID))))
            )
        }
