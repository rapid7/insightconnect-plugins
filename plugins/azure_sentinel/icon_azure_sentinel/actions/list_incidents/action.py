import datetime

import insightconnect_plugin_runtime

from .schema import Component, Input, ListIncidentsInput, ListIncidentsOutput, Output
from icon_azure_sentinel.util.tools import map_output_for_list, generate_query_params


class ListIncidents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_incidents",
            description=Component.DESCRIPTION,
            input=ListIncidentsInput(),
            output=ListIncidentsOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)

        # OData sorting/paging filters
        filters = {
            Input.ORDERBY: params.get(Input.ORDERBY),
            Input.TOP: params.get(Input.TOP),
        }

        # Build OData $filter for status and time range (same logic as trigger)
        status = params.get("status", "All") or "All"
        created_from = params.get("created_from")
        created_to = params.get("created_to")

        created_time = None
        if created_from:
            try:
                created_time = datetime.datetime.fromisoformat(created_from.replace("Z", "")).replace(tzinfo=None)
            except (ValueError, TypeError):
                self.logger.warning(f"Invalid created_from value: {created_from}, ignoring filter")

        query_params = generate_query_params(status, created_time)
        if query_params:
            filters["filter"] = query_params.get("filter", "")

        incidents, _ = self.connection.api_client.list_incident(
            resource_group_name, workspace_name, filters, subscription_id
        )
        incidents = map_output_for_list(incidents)
        return {Output.INCIDENTS: incidents}
