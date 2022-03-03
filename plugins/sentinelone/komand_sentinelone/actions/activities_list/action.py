import insightconnect_plugin_runtime

from .schema import ActivitiesListInput, ActivitiesListOutput, Input, Output, Component
from komand_sentinelone.util.helper import Helper


class ActivitiesList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="activities_list",
            description=Component.DESCRIPTION,
            input=ActivitiesListInput(),
            output=ActivitiesListOutput(),
        )

    def run(self, params={}):
        response = self.connection.activities_list(
            {
                "groupIds": Helper.join_or_empty(params.get(Input.GROUP_IDS, [])),
                "includeHidden": params.get(Input.INCLUDE_HIDDEN, False),
                "skip": params.get(Input.SKIP, None),
                "siteIds": Helper.join_or_empty(params.get(Input.SITE_IDS, [])),
                "agentIds": Helper.join_or_empty(params.get(Input.AGENT_IDS, [])),
                "skipCount": params.get(Input.SKIP_COUNT, False),
                "ids": Helper.join_or_empty(params.get(Input.IDS, [])),
                "createdAt__lt": params.get(Input.CREATED_AT_LT, None),
                "createdAt__lte": params.get(Input.CREATED_AT_LTE, None),
                "countOnly": params.get(Input.COUNT_ONLY, False),
                "accountIds": Helper.join_or_empty(params.get(Input.ACCOUNT_IDS, [])),
                "limit": params.get(Input.LIMIT, 1000),
                "sortBy": params.get(Input.SORT_BY, None),
                "createdAt__gt": params.get(Input.CREATED_AT_GT, None),
                "createdAt__between": params.get(Input.CREATED_AT_BETWEEN, None),
                "activityTypes": Helper.join_or_empty(params.get(Input.ACTIVITY_TYPES, [])),
                "threatIds": Helper.join_or_empty(params.get(Input.THREAT_IDS, [])),
                "sortOrder": params.get(Input.SORT_ORDER, None),
                "userEmails": Helper.join_or_empty(params.get(Input.USER_EMAILS, [])),
                "userIds": Helper.join_or_empty(params.get(Input.USER_IDS, [])),
                "createdAt__gte": params.get(Input.CREATED_AT_GTE, None),
            }
        )

        data = []
        self.add_to_data(data, response)

        limit = params.get(Input.LIMIT, 1000)

        pagination = response.get("pagination", {})
        next_cursor = pagination.get("nextCursor")
        while next_cursor and not limit:
            response = self.connection.activities_list(
                {
                    "cursor": next_cursor,
                }
            )

            data = self.add_to_data(data, response)
            pagination = response.get("pagination")
            next_cursor = pagination.get("nextCursor")

        return {Output.DATA: data}

    @staticmethod
    def add_to_data(data, response):
        if Output.DATA in response:
            for i in response.get(Output.DATA):
                data.append(insightconnect_plugin_runtime.helper.clean_dict(i))
        return data
