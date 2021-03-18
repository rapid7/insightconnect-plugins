import insightconnect_plugin_runtime

from .schema import DiskDetachInput, DiskDetachOutput, Input, Component


class DiskDetach(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disk_detach", description=Component.DESCRIPTION, input=DiskDetachInput(), output=DiskDetachOutput()
        )

    def run(self, params={}):
        return self.connection.client.disk_detach(
            params.get(Input.ZONE), params.get(Input.INSTANCE), params.get(Input.DEVICENAME)
        )
