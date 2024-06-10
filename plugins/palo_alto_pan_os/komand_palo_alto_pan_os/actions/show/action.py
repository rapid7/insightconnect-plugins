import insightconnect_plugin_runtime
from .schema import ShowInput, ShowOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class Show(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="show",
            description=Component.DESCRIPTION,
            input=ShowInput(),
            output=ShowOutput(),
        )

    def run(self, params={}):
        xpath = params.get(Input.XPATH, "")

        output = self.connection.request.show_(xpath=xpath)
        try:
            return {Output.RESPONSE: output["response"]}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )
