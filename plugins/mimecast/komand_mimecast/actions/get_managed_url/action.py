import insightconnect_plugin_runtime

from .schema import GetManagedUrlInput, GetManagedUrlOutput, Component, Output
from komand_mimecast.util.constants import DATA_FIELD


class GetManagedUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_managed_url",
            description=Component.DESCRIPTION,
            input=GetManagedUrlInput(),
            output=GetManagedUrlOutput(),
        )

    def run(self, params={}):
        return {Output.RESPONSE: self.connection.client.get_managed_url(params).get(DATA_FIELD, [])}
