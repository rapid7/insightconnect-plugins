import insightconnect_plugin_runtime
from .schema import EditInput, EditOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class Edit(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="edit",
            description=Component.DESCRIPTION,
            input=EditInput(),
            output=EditOutput(),
        )

    def run(self, params={}):
        xpath = params.get(Input.XPATH)
        element = params.get(Input.ELEMENT)

        output = self.connection.request.edit_(xpath=xpath, element=element)
        try:
            return {"response": output["response"]}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )
