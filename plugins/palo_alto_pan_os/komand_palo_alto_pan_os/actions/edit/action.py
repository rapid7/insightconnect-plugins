import insightconnect_plugin_runtime
from .schema import EditInput, EditOutput
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class Edit(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="edit",
            description="Edit an existing object",
            input=EditInput(),
            output=EditOutput(),
        )

    def run(self, params={}):
        xpath = params.get("xpath")
        element = params.get("element")

        output = self.connection.request.edit_(xpath=xpath, element=element)
        try:
            return {"response": output["response"]}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )
