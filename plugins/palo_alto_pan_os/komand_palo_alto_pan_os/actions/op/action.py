import insightconnect_plugin_runtime
from .schema import OpInput, OpOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class Op(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="op", description=Component.DESCRIPTION, input=OpInput(), output=OpOutput()
        )

    def run(self, params={}):
        cmd = params.get(Input.CMD)
        output = self.connection.request.op(cmd)
        try:
            return {"response": output["response"]}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )
