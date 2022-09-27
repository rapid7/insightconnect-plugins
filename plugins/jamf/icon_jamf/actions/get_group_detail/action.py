import insightconnect_plugin_runtime
from .schema import GetGroupDetailInput, GetGroupDetailOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetGroupDetail(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_group_detail",
            description=Component.DESCRIPTION,
            input=GetGroupDetailInput(),
            output=GetGroupDetailOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.ID)
        response = self.connection.client.get_group_detail(identifier)
        return {Output.GROUP_DETAIL: response.get("mobile_device_group", {})}
