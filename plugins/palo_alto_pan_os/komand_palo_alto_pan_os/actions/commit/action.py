import insightconnect_plugin_runtime
from .schema import CommitInput, CommitOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class Commit(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="commit",
            description=Component.DESCRIPTION,
            input=CommitInput(),
            output=CommitOutput(),
        )

    def run(self, params={}):
        cmd = params.get(Input.CMD)
        action = params.get(Input.ACTION)

        output = self.connection.request.commit(action, cmd)

        try:
            return {"response": output["response"]}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )
