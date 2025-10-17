import insightconnect_plugin_runtime
from .schema import ResetPasswordInput, ResetPasswordOutput, Input, Output, Component

# Custom imports below
from komand_okta.util.helpers import clean


class ResetPassword(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reset_password",
            description=Component.DESCRIPTION,
            input=ResetPasswordInput(),
            output=ResetPasswordOutput(),
        )

    def run(self, params={}):
        response = self.connection.api_client.reset_password(
            params.get(Input.USERID),
            clean({"sendEmail": params.get(Input.SENDEMAIL), "revokeSessions": params.get(Input.REVOKESESSIONS)}),
        )
        return clean({Output.SUCCESS: True, Output.RESETPASSWORDURL: response.get("resetPasswordUrl")})
