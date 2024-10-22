import insightconnect_plugin_runtime
from .schema import GetTagDetailsInput, GetTagDetailsOutput, Input, Component

# Custom imports below
from icon_greynoise.util.util import GNRequestFailure
from greynoise.exceptions import RequestFailure


class GetTagDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_tag_details",
            description=Component.DESCRIPTION,
            input=GetTagDetailsInput(),
            output=GetTagDetailsOutput(),
        )

    def run(self, params={}):
        tag_name = params.get(Input.TAG_NAME).lower()
        output = {}
        try:
            resp = self.connection.gn_client.metadata()
            for tag in resp["metadata"]:
                if tag["name"].lower() == tag_name:
                    output = tag
        except RequestFailure as e:
            raise PluginException(
                cause=f"API responded with ERROR: {e.args[0]} - {e.args[1]}.",
                assistance="Please check error and try again.",
            )

        if output:
            return output
        else:
            return {"name": params.get(Input.TAG_NAME), "description": "Tag Not Found"}
