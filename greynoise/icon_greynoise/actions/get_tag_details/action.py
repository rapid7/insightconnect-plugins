import insightconnect_plugin_runtime
from .schema import GetTagDetailsInput, GetTagDetailsOutput, Input, Output, Component

# Custom imports below
from greynoise.exceptions import RequestFailure
from insightconnect_plugin_runtime.exceptions import PluginException


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
                cause="Received HTTP %d status code from GreyNoise. Verify your input and try again." % e.args[0],
                assistance="If the issue persists please contact support.",
                data=f"{e.args[0]}, {e.args[1]['message']}",
            )
        if output:
            return output
        else:
            return {"name": params.get(Input.TAG_NAME), "description": "Tag Not Found"}
