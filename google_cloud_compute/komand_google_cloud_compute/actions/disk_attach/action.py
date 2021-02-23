import insightconnect_plugin_runtime

from .schema import DiskAttachInput, DiskAttachOutput, Input, Component


class DiskAttach(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disk_attach", description=Component.DESCRIPTION, input=DiskAttachInput(), output=DiskAttachOutput()
        )

    def run(self, params={}):
        return self.connection.client.disk_attach(
            params.get(Input.ZONE), params.get(Input.INSTANCE), params.get(Input.SOURCE)
        )
