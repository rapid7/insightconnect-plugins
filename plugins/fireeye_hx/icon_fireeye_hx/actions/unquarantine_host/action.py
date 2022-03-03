import insightconnect_plugin_runtime
from .schema import UnquarantineHostInput, UnquarantineHostOutput, Input, Output, Component

# Custom imports below


class UnquarantineHost(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="unquarantine_host",
            description=Component.DESCRIPTION,
            input=UnquarantineHostInput(),
            output=UnquarantineHostOutput(),
        )

    def run(self, params={}):
        # TODO: Implement run function
        return {}
