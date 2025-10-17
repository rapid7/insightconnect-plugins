import insightconnect_plugin_runtime
from .schema import ExpirePasswordInput, ExpirePasswordOutput, Input, Output, Component

# Custom imports below
from komand_okta.util.helpers import clean


class ExpirePassword(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="expire_password",
            description=Component.DESCRIPTION,
            input=ExpirePasswordInput(),
            output=ExpirePasswordOutput(),
        )

    def run(self, params={}):
        response = self.connection.api_client.expire_password(
            params.get(Input.USERID), clean({"tempPassword": params.get(Input.TEMPPASSWORD)})
        )
        return clean({Output.SUCCESS: True, Output.TEMPPASSWORD: response.get("tempPassword")})
