import insightconnect_plugin_runtime
from .schema import GetInput, GetOutput
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class Get(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get",
            description="Get candidate configuration",
            input=GetInput(),
            output=GetOutput(),
        )

    def run(self, params={}):
        xpath = params.get("xpath", "")

        output = self.connection.request.get_(xpath=xpath)
        try:
            return {"response": output["response"]}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )
