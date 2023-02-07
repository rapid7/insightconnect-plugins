import insightconnect_plugin_runtime
from .schema import ListOperatorGroupsInput, ListOperatorGroupsOutput, Input, Output, Component

# Custom imports below
from icon_topdesk.util.helpers import clean


class ListOperatorGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="listOperatorGroups",
            description=Component.DESCRIPTION,
            input=ListOperatorGroupsInput(),
            output=ListOperatorGroupsOutput(),
        )

    def run(self, params={}):
        parameters = {
            "start": params.get(Input.START),
            "page_size": params.get(Input.PAGESIZE),
            "query": params.get(Input.QUERY),
            "fields": params.get(Input.FIELDS),
        }
        return {Output.OPERATORGROUPS: self.connection.api_client.get_operator_groups(clean(parameters))}
