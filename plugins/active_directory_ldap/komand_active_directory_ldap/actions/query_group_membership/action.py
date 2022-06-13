import insightconnect_plugin_runtime

# Custom imports below
from .schema import QueryGroupMembershipInput, QueryGroupMembershipOutput, Input, Output, Component


class QueryGroupMembership(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query_group_membership",
            description=Component.DESCRIPTION,
            input=QueryGroupMembershipInput(),
            output=QueryGroupMembershipOutput(),
        )

    def run(self, params={}):
        base = params.get(Input.SEARCH_BASE)
        include_groups = params.get(Input.INCLUDE_GROUPS)
        expand_nested_groups = params.get(Input.EXPAND_NESTED_GROUPS)
        entries = self.connection.client.query_group_membership(
            base, params.get(Input.GROUP_NAME), include_groups, expand_nested_groups
        )
        return {Output.RESULTS: entries, Output.COUNT: len(entries)}
