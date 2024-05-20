import insightconnect_plugin_runtime
from .schema import AddHostInput, AddHostOutput, Input, Output, Component

# Custom imports below


class AddHost(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_host",
            description=Component.DESCRIPTION,
            input=AddHostInput(),
            output=AddHostOutput(),
        )

    def run(self, params={}):
        host = insightconnect_plugin_runtime.helper.clean_dict(params.get(Input.HOST))

        ref = self.connection.infoblox_connection.add_host(host)

        return {Output._REF: ref}
