import datetime

import insightconnect_plugin_runtime

# Custom imports below
from ...util.tools import generate_query_params
from .schema import Component, Input, Output, ListIncidentsInput, ListIncidentsOutput


class ListIncidents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_incidents",
            description=Component.DESCRIPTION,
            input=ListIncidentsInput(),
            output=ListIncidentsOutput(),
        )

    def run(self, params={}):
        status = params.get(Input.STATUS, "All")
        created_time = (
            datetime.datetime.fromisoformat(params.get(Input.CREATED_TIME)).replace(tzinfo=None)
            if params.get(Input.CREATED_TIME)
            else None
        )
        last_update_time = (
            datetime.datetime.fromisoformat(params.get(Input.LAST_UPDATE_TIME)).replace(tzinfo=None)
            if params.get(Input.LAST_UPDATE_TIME)
            else None
        )
        assigned_to = params.get(Input.ASSIGNED_TO, "")
        response, _ = self.connection.client.list_incidents(
            generate_query_params(status, created_time, last_update_time, assigned_to)
        )
        return {Output.INCIDENTS: response}
