import insightconnect_plugin_runtime
from .schema import CreateQueryInput, CreateQueryOutput, Input, Output, Component

# Custom imports below


class CreateQuery(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_query", description=Component.DESCRIPTION, input=CreateQueryInput(), output=CreateQueryOutput()
        )

    def run(self, params={}):
        account_ids = params.get(Input.ACCOUNT_IDS, None)
        group_ids = params.get(Input.GROUP_IDS, None)
        is_verbose = params.get(Input.IS_VERBOSE, None)
        limit = params.get(Input.LIMIT, None)
        query_type = params.get(Input.QUERY_TYPE, None)
        site_ids = params.get(Input.SITE_IDS, None)
        tenant = params.get(Input.TENANT, None)

        payload = {
            "fromDate": params.get(Input.FROM_DATE),
            "toDate": params.get(Input.TO_DATE),
            "query": params.get(Input.QUERY),
        }

        if account_ids:
            payload["accountIds"] = account_ids
        if group_ids:
            payload["groupIds"] = group_ids
        if is_verbose:
            payload["isVerbose"] = is_verbose
        if limit:
            payload["limit"] = limit
        if query_type:
            payload["queryType"] = query_type
        if site_ids:
            payload["siteIds"] = site_ids
        if tenant:
            payload["tenant"] = tenant

        return {Output.RESPONSE: self.connection.create_query(payload=payload)}
