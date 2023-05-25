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
        multi_resp = {Output.MULTI_RESPONSE: []}
        for i in email_identifiers:
            if i["message_id"].startswith("<") and i["message_id"].endswith(">"):
                response = client.delete_email_message(
                    pytmv1.EmailMessageIdTask(
                        messageId=i["message_id"],
                        description=i.get("description", ""),
                        mailbox=i.get("mailbox", ""),
                    )
                )
            else:
                response = client.delete_email_message(
                    pytmv1.EmailMessageUIdTask(
                        uniqueId=i["message_id"],
                        description=i.get("description", ""),
                    )
                )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred when deleting the email message.",
                    assistance="Please check the email message identifiers and try again.",
                    data=response.errors,
                )
            else:
                multi_resp[Output.MULTI_RESPONSE].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
