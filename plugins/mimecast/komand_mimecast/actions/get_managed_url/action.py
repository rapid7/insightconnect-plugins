import insightconnect_plugin_runtime

from .schema import GetManagedUrlInput, GetManagedUrlOutput, Component, Output, Input
from komand_mimecast.util.constants import DATA_FIELD
from ...util.util import Utils


class GetManagedUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_managed_url",
            description=Component.DESCRIPTION,
            input=GetManagedUrlInput(),
            output=GetManagedUrlOutput(),
        )

    def run(self, params={}):
        data = self.connection.client.get_managed_url(
            {
                Input.DOMAINORURL: params.get(Input.DOMAINORURL, ""),
                Input.EXACTMATCH: params.get(Input.EXACTMATCH, False),
            }
        ).get(DATA_FIELD, [])

        filter_ = {}
        for key, value in params.items():
            if key != Input.DOMAINORURL or key != Input.EXACTMATCH:
                temp = Utils.normalize(key, value)
                filter_.update(temp)

        for key, value in filter_.items():
            data[:] = [element for element in data if str(element.get(key)) == value]

        return {Output.RESPONSE: data}
