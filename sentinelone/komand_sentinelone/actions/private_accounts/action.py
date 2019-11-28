import komand
from .schema import PrivateAccountsInput, PrivateAccountsOutput, Input, Output, Component
# Custom imports below


class PrivateAccounts(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='private_accounts',
                description=Component.DESCRIPTION,
                input=PrivateAccountsInput(),
                output=PrivateAccountsOutput())

    def run(self, params={}):
        accounts = self.connection.get_accounts({
            "query": params.get(Input.QUERY, None),
            "ids": params.get(Input.IDS, None),
            "skipCount": params.get(Input.SKIP_COUNT, None),
            "skip": params.get(Input.SKIP, None),
            "sortBy": params.get(Input.SORT_BY, None),
            "sortOrder": params.get(Input.SORT_ORDER, None),
            "siteIds": params.get(Input.SITE_IDS, None),
            "accountIds": params.get(Input.ACCOUNT_IDS, None),
            "limit": params.get(Input.LIMIT, None),
            "countOnly": params.get(Input.COUNT_ONLY, None),
            "cursor": params.get(Input.CURSOR, None)
        })

        return {
            Output.DATA: accounts.get("data"),
            Output.PAGINATION: accounts.get("pagination")
        }
