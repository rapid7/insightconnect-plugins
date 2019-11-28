import komand
from .schema import LastActivityAsSyslogInput, LastActivityAsSyslogOutput, Input, Output, Component
# Custom imports below
from komand_sentinelone.util.helper import Helper


class LastActivityAsSyslog(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='last_activity_as_syslog',
                description=Component.DESCRIPTION,
                input=LastActivityAsSyslogInput(),
                output=LastActivityAsSyslogOutput())

    def run(self, params={}):
        accounts = self.connection.last_activity_as_syslog({
            "groupIds": Helper.join_or_empty(params.get(Input.GROUP_IDS, [])),
            "includeHidden": params.get(Input.INCLUDE_HIDDEN, False),
            "skip": params.get(Input.SKIP, None),
            "siteIds": Helper.join_or_empty(params.get(Input.SITE_IDS, [])),
            "agentIds": Helper.join_or_empty(params.get(Input.AGENT_IDS, [])),
            "skipCount": params.get(Input.SKIP_COUNT, False),
            "ids": Helper.join_or_empty(params.get(Input.IDS, [])),
            "createdAt__lt": params.get(Input.CREATED_AT_LT, None),
            "createdAt__lte": params.get(Input.CREATED_AT_LTE, None),
            "cursor": params.get(Input.CURSOR, None),
            "countOnly": params.get(Input.COUNT_ONLY, False),
            "accountIds": Helper.join_or_empty(params.get(Input.ACCOUNT_IDS, [])),
            "limit": params.get(Input.LIMIT, 10),
            "sortBy": params.get(Input.SORT_BY, None),
            "createdAt__gt": params.get(Input.CREATED_AT_GT, None),
            "createdAt__between": params.get(Input.CREATED_AT_BETWEEN, None),
            "activityTypes": Helper.join_or_empty(params.get(Input.ACTIVITY_TYPES, [])),
            "threatIds": Helper.join_or_empty(params.get(Input.THREAT_IDS, [])),
            "sortOrder": params.get(Input.SORT_ORDER, None),
            "userEmails": Helper.join_or_empty(params.get(Input.USER_EMAILS, [])),
            "userIds": Helper.join_or_empty(params.get(Input.USER_IDS, [])),
            "createdAt__gte": params.get(Input.CREATED_AT_GTE, None),
        })

        return {
            Output.DATA: accounts.get("data"),
            Output.PAGINATION: accounts.get("pagination")
        }
