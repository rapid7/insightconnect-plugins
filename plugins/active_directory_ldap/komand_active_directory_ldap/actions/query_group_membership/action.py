import insightconnect_plugin_runtime

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import (
    QueryGroupMembershipInput,
    QueryGroupMembershipOutput,
    Input,
    Output,
    Component,
)


class QueryGroupMembership(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query_group_membership",
            description=Component.DESCRIPTION,
            input=QueryGroupMembershipInput(),
            output=QueryGroupMembershipOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        base = params.get(Input.SEARCH_BASE)
        group_name = params.get(Input.GROUP_NAME)
        include_groups = params.get(Input.INCLUDE_GROUPS)
        expand_nested_groups = params.get(Input.EXPAND_NESTED_GROUPS)
        # END INPUT BINDING - DO NOT REMOVE

        entries = self.connection.client.query_group_membership(
            base, group_name, include_groups, expand_nested_groups
        )
        return {Output.RESULTS: entries, Output.COUNT: len(entries)}
