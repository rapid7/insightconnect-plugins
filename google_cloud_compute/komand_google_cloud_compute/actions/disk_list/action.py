import insightconnect_plugin_runtime

from .schema import DiskListInput, DiskListOutput, Input, Component


class DiskList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disk_list", description=Component.DESCRIPTION, input=DiskListInput(), output=DiskListOutput()
        )

    def run(self, params={}):
        return self.connection.client.disk_list(
            params.get(Input.ZONE), params.get(Input.FILTER), params.get(Input.MAXRESULTS), params.get(Input.ORDERBY)
        )
