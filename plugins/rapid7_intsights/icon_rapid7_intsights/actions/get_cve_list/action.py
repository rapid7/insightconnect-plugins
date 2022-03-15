import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import GetCveListInput, GetCveListOutput, Input, Output, Component


class GetCveList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_cve_list", description=Component.DESCRIPTION, input=GetCveListInput(), output=GetCveListOutput()
        )

    def run(self):
        return clean({Output.CONTENT: self.connection.client.get_cve([])})
