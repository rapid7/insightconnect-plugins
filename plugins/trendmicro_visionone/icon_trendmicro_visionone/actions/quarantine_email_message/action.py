import insightconnect_plugin_runtime
from .schema import (
    QuarantineEmailMessageInput,
    QuarantineEmailMessageOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import pytmv1


class QuarantineEmailMessage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine_email_message",
            description=Component.DESCRIPTION,
            input=QuarantineEmailMessageInput(),
            output=QuarantineEmailMessageOutput(),
        )

    def run(self, params={}):
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        email_identifiers = params.get(Input.EMAIL_IDENTIFIERS)
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = {"multi_response": []}
        for i in email_identifiers:
            if i["message_id"].startswith("<") and i["message_id"].endswith(">"):
                response = client.quarantine_email_message(
                    pytmv1.EmailMessageIdTask(
                        messageId=i["message_id"],
                        description=i.get("description", ""),
                        mailbox=i.get("mailbox", ""),
                    )
                )
            else:
                response = client.quarantine_email_message(
                    pytmv1.EmailMessageUIdTask(
                        uniqueId=i["message_id"],
                        description=i.get("description", ""),
                    )
                )
            if "error" in response.result_code.lower():
                return response.errors
            else:
                multi_resp["multi_response"].append(response.response.dict().get("items")[0])
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
