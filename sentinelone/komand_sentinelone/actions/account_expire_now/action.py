import komand
from .schema import AccountExpireNowInput, AccountExpireNowOutput, Input, Output, Component
# Custom imports below


class AccountExpireNow(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='account_expire_now',
                description=Component.DESCRIPTION,
                input=AccountExpireNowInput(),
                output=AccountExpireNowOutput())

    def run(self, params={}):
        return {
            Output.DATA: self.connection.accounts_by_id_expire_now(
                params.get(Input.ACCOUNT_ID, None)
            ).get("data", {})
        }
