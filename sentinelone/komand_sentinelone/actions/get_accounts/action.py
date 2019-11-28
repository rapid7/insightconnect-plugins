import komand
from .schema import GetAccountsInput, GetAccountsOutput, Input, Output, Component
# Custom imports below
from komand_sentinelone.util.exceptions import PluginException
from komand_sentinelone.util.helper import Helper


class GetAccounts(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_accounts',
            description=Component.DESCRIPTION,
            input=GetAccountsInput(),
            output=GetAccountsOutput())

    def run(self, params={}):
        if params.get(Input.FEATURES) and not all(elem in ["firewall-control", "device-control", "ioc"] for elem in params.get(Input.FEATURES)):
            raise PluginException(
                cause="Wrong parameter",
                assistance='Feature input should be one of: firewall-control, device-control, ioc'
            )

        accounts = self.connection.get_accounts({
            "cursor": params.get(Input.CURSOR, None),
            "limit": params.get(Input.LIMIT, None),
            "activeLicenses": params.get(Input.ACTIVE_LICENSES, None),
            "skipCount": params.get(Input.SKIP_COUNT, None),
            "query": params.get(Input.QUERY, None),
            "features": Helper.join_or_empty(params.get(Input.FEATURES, [])),
            "accountIds": Helper.join_or_empty(params.get(Input.ACCOUNT_IDS, None)),
            "totalLicenses": params.get(Input.TOTAL_LICENSES, None),
            "ids": Helper.join_or_empty(params.get(Input.IDS, None)),
            "skip": params.get(Input.SKIP, None),
            "countOnly": params.get(Input.COUNT_ONLY, None),
            "sortBy": params.get(Input.SORT_BY, None),
            "accountType": params.get(Input.ACCOUNT_TYPE, None),
            "createdAt": params.get(Input.CREATED_AT, None),
            "sortOrder": params.get(Input.SORT_ORDER, None),
            "isDefault": params.get(Input.IS_DEFAULT, None),
            "states": params.get(Input.STATES, None),
            "name": params.get(Input.NAME, None),
            "updateAt": params.get(Input.UPDATED_AT, None),
            "expiration": params.get(Input.EXPIRATION, None)
        })

        if not accounts or 'data' not in accounts:
            return {
                Output.DATA: {},
                Output.PAGINATION: accounts.get("pagination", {})
            }

        return {
            Output.DATA: accounts.get("data", {}),
            Output.PAGINATION: accounts.get("pagination", {})
        }
