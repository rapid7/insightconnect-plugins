import insightconnect_plugin_runtime
from .schema import ListOperatorsInput, ListOperatorsOutput, Input, Output, Component

# Custom imports below
from icon_topdesk.util.helpers import clean


class ListOperators(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="listOperators",
            description=Component.DESCRIPTION,
            input=ListOperatorsInput(),
            output=ListOperatorsOutput(),
        )

    def run(self, params={}):
        parameters = {
            "start": params.get(Input.START),
            "page_size": params.get(Input.PAGESIZE),
            "query": params.get(Input.QUERY),
            "fields": params.get(Input.FIELDS),
        }
        return {Output.OPERATORS: self.connection.api_client.get_operators(clean(parameters))}
