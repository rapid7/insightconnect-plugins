import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetServerGroupInput, GetServerGroupOutput, Input, Output, Component

# Custom imports below


class GetServerGroup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_server_group",
            description=Component.DESCRIPTION,
            input=GetServerGroupInput(),
            output=GetServerGroupOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        group_id = params.get(Input.GROUP_ID)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.zpa_client.get_server_group(group_id)
        return {
            Output.GROUP: result,
        }
