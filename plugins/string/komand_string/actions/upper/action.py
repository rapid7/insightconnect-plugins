import insightconnect_plugin_runtime
from .schema import UpperInput, UpperOutput

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Upper(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="upper",
            description="Converts lowercase letters to uppercase",
            input=UpperInput(),
            output=UpperOutput(),
        )

    def run(self, params={}):
        string = params.get("string")
        if not string:
            raise PluginException(
                cause="Action failed! Missing required user input.",
                assistance="Please provide the input string.",
            )
        return {"upper": string.upper()}
