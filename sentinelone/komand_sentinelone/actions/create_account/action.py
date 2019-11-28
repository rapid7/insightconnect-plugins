import komand
from .schema import CreateAccountInput, CreateAccountOutput, Input, Output, Component
# Custom imports below


class CreateAccount(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_account',
                description=Component.DESCRIPTION,
                input=CreateAccountInput(),
                output=CreateAccountOutput())

    def run(self, params={}):
        self.connection.create_account(
                {
                    "externalId": params.get(Input.EXTERNAL_ID, None),
                    "skus": params.get(Input.SKUS),
                    "accountType": params.get(Input.ACCOUNT_TYPE),
                    "inherits": params.get(Input.INHERITS, None),
                    "name": params.get(Input.NAME),
                    "policy": params.get(Input.POLICY, None),
                    "unlimitedExpiration":  params.get(Input.UNLIMITED_EXPIRATION, None),
                    "expiration":  params.get(Input.EXPIRATION, None)
                }
            )

        return {Output.SUCCESS: True}
