import insightconnect_plugin_runtime
from .schema import CuckooStatusInput, CuckooStatusOutput, Component


class CuckooStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="cuckoo_status",
            description=Component.DESCRIPTION,
            input=CuckooStatusInput(),
            output=CuckooStatusOutput(),
        )

    def run(self):
        endpoint = "cuckoo/status"
        response = self.connection.api.send(endpoint)
        return response
