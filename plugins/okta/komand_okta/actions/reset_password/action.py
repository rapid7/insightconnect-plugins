import komand
from .schema import ResetPasswordInput, ResetPasswordOutput, Input, Output, Component

# Custom imports below
import requests


class ResetPassword(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reset_password",
            description=Component.DESCRIPTION,
            input=ResetPasswordInput(),
            output=ResetPasswordOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)
        temp_password = params.get(Input.TEMP_PASSWORD)

        url = requests.compat.urljoin(
            self.connection.okta_url, f"/api/v1/users/{user_id}/lifecycle/expire_password?tempPassword={temp_password}"
        )
        response = self.connection.session.post(url)
        data = response.json()

        if response.status_code != 200:
            error_summary = data["errorSummary"]
            self.logger.error(f"Okta: Password reset for user failed: {error_summary}")
            return {Output.SUCCESS: False}

        if temp_password:
            return {Output.TEMP_PASSWORD: data["tempPassword"], Output.SUCCESS: True}

        return {Output.SUCCESS: True}
