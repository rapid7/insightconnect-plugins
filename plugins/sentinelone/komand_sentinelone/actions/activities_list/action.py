import insightconnect_plugin_runtime
from .schema import ActivitiesListInput, ActivitiesListOutput, Input, Output, Component

# Custom imports below
from komand_sentinelone.util.helper import Helper, clean


class ActivitiesList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="activities_list",
            description=Component.DESCRIPTION,
            input=ActivitiesListInput(),
            output=ActivitiesListOutput(),
        )

    def run(self, params={}):
        limit = params.get(Input.LIMIT)
        skip = params.get(Input.SKIP)
        parameters = clean(
            {
                "groupIds": Helper.join_or_empty(params.get(Input.GROUPIDS, [])),
                "includeHidden": params.get(Input.INCLUDEHIDDEN),
                "skip": skip if skip else None,
                "siteIds": Helper.join_or_empty(params.get(Input.SITEIDS, [])),
                "agentIds": Helper.join_or_empty(params.get(Input.AGENTIDS, [])),
                "skipCount": params.get(Input.SKIPCOUNT),
                "ids": Helper.join_or_empty(params.get(Input.IDS, [])),
                "createdAt__lt": params.get(Input.CREATEDATLT),
                "createdAt__lte": params.get(Input.CREATEDATLTE),
                "countOnly": params.get(Input.COUNTONLY),
                "accountIds": Helper.join_or_empty(params.get(Input.ACCOUNTIDS, [])),
                "limit": limit if limit and limit in range(1, 1000) else 1000,
                "sortBy": params.get(Input.SORTBY),
                "createdAt__gt": params.get(Input.CREATEDATGT),
                "createdAt__between": params.get(Input.CREATEDATBETWEEN),
                "activityTypes": Helper.join_or_empty(params.get(Input.ACTIVITYTYPES, [])),
                "threatIds": Helper.join_or_empty(params.get(Input.THREATIDS, [])),
                "sortOrder": params.get(Input.SORTORDER),
                "userEmails": params.get(Input.USEREMAIL),
                "userIds": Helper.join_or_empty(params.get(Input.USERIDS, [])),
                "createdAt__gte": params.get(Input.CREATEDATGTE),
            }
        )
        response = self.connection.client.get_activities_list(parameters)
        pagination = response.get("pagination", {})
        next_cursor = pagination.get("nextCursor")
        total_items = pagination.get("totalItems", 0)

        data = []
        data.extend(response.get("data", []))

        if not limit and next_cursor:
            for _ in range(9999):
                parameters["cursor"] = next_cursor
                response = self.connection.client.get_activities_list(parameters)
                data.extend(response.get("data", []))
                next_cursor = response.get("pagination", {}).get("nextCursor")
                if not next_cursor:
                    break

        return {Output.DATA: clean(data), Output.TOTALITEMS: total_items}
