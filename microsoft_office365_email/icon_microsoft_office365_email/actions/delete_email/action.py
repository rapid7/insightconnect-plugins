import komand
from .schema import DeleteEmailInput, DeleteEmailOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class DeleteEmail(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_email',
                description=Component.DESCRIPTION,
                input=DeleteEmailInput(),
                output=DeleteEmailOutput())

    def delete_message(self, email_id: str, user_message: str) -> None:
        headers = self.connection.get_headers(self.connection.get_auth_token())
        delete_endpoint_formatted = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{user_message}/messages/{email_id}"

        try:
            request = requests.delete(delete_endpoint_formatted, headers=headers)
        except Exception as e:
            raise PluginException(cause="Unable to delete email.",
                                  assistance=f"Email ID {email_id} in Mailbox ID {user_message} may no longer exist.",
                                  data=e)

        self.logger.info(f"Delete Response Code: {request.status_code}")

        if request.status_code != 204:  # correct response is 204 no content
            raise PluginException(cause="Unable to delete email.",
                                  assistance=f"Unrecognized status code {request.status_code}",
                                  data=request.text)
        return

    def run(self, params={}):
        email_id = params.get(Input.EMAIL_ID)
        mailbox_id = params.get(Input.MAILBOX_ID)
        self.delete_message(email_id, mailbox_id)
        return {Output.SUCCESS: True}
