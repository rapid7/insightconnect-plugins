import insightconnect_plugin_runtime
from .schema import ModifyHostInput, ModifyHostOutput, Input, Output, Component

# Custom imports below


class ModifyHost(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="modify_host",
            description=Component.DESCRIPTION,
            input=ModifyHostInput(),
            output=ModifyHostOutput(),
        )

    def run(self, params={}):
        ref = params.get(Input.REF)
        updated_host = insightconnect_plugin_runtime.helper.clean_dict(params.get(Input.UPDATED_HOST))

        ref = self.connection.infoblox_connection.modify_host(ref, updated_host)

        return {Output._REF: ref}
