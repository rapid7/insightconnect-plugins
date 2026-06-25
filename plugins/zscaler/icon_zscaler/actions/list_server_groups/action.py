import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import ListServerGroupsInput, ListServerGroupsOutput, Input, Output, Component

# Custom imports below
from icon_zscaler.util.helpers import clean_dict


class ListServerGroups(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_server_groups",
            description=Component.DESCRIPTION,
            input=ListServerGroupsInput(),
            output=ListServerGroupsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        next_link = params.get(Input.NEXT_LINK)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.zpa_client.list_server_groups(next_link or None)
        return clean_dict(
            {
                Output.GROUPS: result.get("groups", []),
                Output.NEXT_LINK: result.get("next_link", ""),
            }
        )
