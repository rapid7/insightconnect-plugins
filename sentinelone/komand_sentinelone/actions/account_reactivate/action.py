import komand
from .schema import AccountReactivateInput, AccountReactivateOutput, Input, Output, Component
from komand_sentinelone.util.exceptions import PluginException


class AccountReactivate(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='account_reactivate',
            description=Component.DESCRIPTION,
            input=AccountReactivateInput(),
            output=AccountReactivateOutput())

    def run(self, params={}):
        if params.get(Input.UNLIMITED, False) is False and params.get(Input.EXPIRATION, None) is None:
            raise PluginException(cause="Illegal argument",
                                  assistance="There should be expiration parameter when unlimited is set to false")

        return {
            Output.SUCCESS: self.connection.account_reactivate(
                params.get(Input.ACCOUNT_ID, None),
                params.get(Input.UNLIMITED, False),
                params.get(Input.EXPIRATION, None)
            ).get("data", {}).get("success", False)
        }
