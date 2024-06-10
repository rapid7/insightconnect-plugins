import insightconnect_plugin_runtime
from .schema import DeleteInput, DeleteOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class Delete(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete",
            description=Component.DESCRIPTION,
            input=DeleteInput(),
            output=DeleteOutput(),
        )

    def run(self, params={}):
        xpath = params.get(Input.XPATH)

        output = self.connection.request.delete_(xpath=xpath)
        try:
            return {"response": output["response"]}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )
