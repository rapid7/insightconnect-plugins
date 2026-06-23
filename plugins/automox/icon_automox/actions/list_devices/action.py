import insightconnect_plugin_runtime
from .schema import ListDevicesInput, ListDevicesOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class ListDevices(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_devices", description=Component.DESCRIPTION, input=ListDevicesInput(), output=ListDevicesOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        group_id = params.get(Input.GROUP_ID, 0)
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        group_id = None if group_id == 0 else group_id

        devices = self.connection.automox_api.get_devices(org_id, group_id)
        self.logger.info(f"Returned {len(devices)} devices")

        return {Output.DEVICES: devices}
