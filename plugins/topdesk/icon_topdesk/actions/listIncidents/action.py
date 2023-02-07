import insightconnect_plugin_runtime
from .schema import ListIncidentsInput, ListIncidentsOutput, Input, Output, Component

# Custom imports below
from icon_topdesk.util.helpers import clean


class ListIncidents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="listIncidents",
            description=Component.DESCRIPTION,
            input=ListIncidentsInput(),
            output=ListIncidentsOutput(),
        )

    def run(self, params={}):
        parameters = {
            "pageStart": params.get(Input.PAGESTART),
            "pageSize": params.get(Input.PAGESIZE),
            "sort": params.get(Input.SORT),
            "query": params.get(Input.QUERY),
            "fields": params.get(Input.FIELDS),
            "all": params.get(Input.ALL),
        }
        return {Output.INCIDENTS: self.connection.api_client.get_incidents(clean(parameters))}
