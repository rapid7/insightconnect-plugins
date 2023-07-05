import insightconnect_plugin_runtime
from .schema import (
    DeleteEmailMessageInput,
    DeleteEmailMessageOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class DeleteEmailMessage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_email_message",
            description=Component.DESCRIPTION,
            input=DeleteEmailMessageInput(),
            output=DeleteEmailMessageOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        email_identifiers = params.get(Input.EMAIL_IDENTIFIERS)
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = []
        for email_identifier in email_identifiers:
            if email_identifier["message_id"].startswith("<") and email_identifier["message_id"].endswith(">"):
                response = client.delete_email_message(
                    pytmv1.EmailMessageIdTask(
                        messageId=email_identifier["message_id"],
                        description=email_identifier.get("description", ""),
                        mailbox=email_identifier.get("mailbox", ""),
                    )
                )
            else:
                response = client.delete_email_message(
                    pytmv1.EmailMessageUIdTask(
                        uniqueId=email_identifier["message_id"],
                        description=email_identifier.get("description", ""),
                    )
                )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred when deleting the email message.",
                    assistance="Please check the email message identifiers and try again.",
                    data=response.errors,
                )
            multi_resp.append(response.response.dict().get("items")[0])
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: multi_resp}
