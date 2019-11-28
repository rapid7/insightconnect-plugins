import komand
from .schema import UpdateAccountInput, UpdateAccountOutput, Input, Output, Component
# Custom imports below
from komand_sentinelone.util.helper import Helper


class UpdateAccount(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_account',
                description=Component.DESCRIPTION,
                input=UpdateAccountInput(),
                output=UpdateAccountOutput())

    def run(self, params={}):
        accounts = self.connection.update_account(params.get(Input.ACCOUNT_ID), {
            "externalId": params.get(Input.EXTERNAL_ID),
            "skus": params.get(Input.SKUS, None),
            "accountType": params.get(Input.ACCOUNT_TYPE),
            "inherits": params.get(Input.INHERITS),
            "name": params.get(Input.NAME),
            "policy": params.get(Input.POLICY),
            "unlimitedExpiration": params.get(Input.UNLIMITED_EXPIRATION),
            "expiration": params.get(Input.EXPIRATION)
        })

        return {
            Output.DATA: accounts.get("data")
        }
