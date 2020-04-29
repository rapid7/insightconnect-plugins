import komand
from .schema import RevokeSignInSessionsInput, RevokeSignInSessionsOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class RevokeSignInSessions(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='revoke_sign_in_sessions',
                description=Component.DESCRIPTION,
                input=RevokeSignInSessionsInput(),
                output=RevokeSignInSessionsOutput())

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)
        endpoint = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{user_id}/revokeSignInSessions"

        self.logger.info(f"Revoking sign in sessions for user: {user_id}")

        headers = self.connection.get_headers(self.connection.get_auth_token())
        result = requests.post(endpoint, headers=headers)

        # This is supposed to return 204...however it actually returns 200. The docs make note of this
        # https://docs.microsoft.com/en-us/graph/api/user-revokesigninsessions
        # Thus, I'm just going to look for invalid responses
        if result.status_code >= 400:
            raise PluginException(cause="Revoke Sign In Sessions Failed.",
                                  assistance="Unexpected return code from server.",
                                  data=result.text)

        return {Output.SUCCESS: True}
