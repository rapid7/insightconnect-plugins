import komand
from komand.exceptions import PluginException
from .schema import SendEmailInput, SendEmailOutput, Input, Output, Component
# Custom imports below
import json
import requests


class SendEmail(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_email',
                description=Component.DESCRIPTION,
                input=SendEmailInput(),
                output=SendEmailOutput())

    def run(self, params={}):
        message_to_send = self.compose_email(params)
        self.logger.info("Sending Email...")
        result = self.send_message(message_to_send, params.get(Input.EMAIL_FROM))
        self.logger.info("API call complete")

        # This will raise an exception if the status code isn't in the 200 range
        return {Output.SUCCESS: result}

    def compose_email(self, params):
        email_from = params.get(Input.EMAIL_FROM)
        email_to = params.get(Input.EMAIL_TO)
        subject = params.get(Input.SUBJECT)
        message = params.get(Input.BODY)
        html = params.get(Input.IS_HTML)
        bcc = params.get(Input.BCC)
        cc = params.get(Input.CC)
        attachment = params.get(Input.ATTACHMENT)

        if (html):
            content_type = "html"
        else:
            content_type = "text"

        bcc_container = self.make_email_container(bcc)
        cc_container = self.make_email_container(cc)

        message = {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": content_type,
                    "content": message
                },
                "from": {
                    "emailAddress": {
                        "address": email_from
                    }
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": email_to
                        }
                    }
                ],
                "ccRecipients": cc_container,
                "bccRecipients": bcc_container,
            },
            "saveToSentItems": "false"
        }

        self.make_attachment(attachment, message)

        return json.dumps(message)

    def make_attachment(self, attachment: dict, message: dict) -> None:
        if attachment:
            if attachment.get('filename') and \
                    attachment.get('content') and \
                    attachment.get('filename') is not "" and \
                    attachment.get('content') is not "":
                message['message']['attachments'] = [
                    {
                        "@odata.type": "#Microsoft.OutlookServices.FileAttachment",
                        "Name": attachment['filename'],
                        "ContentBytes": attachment['content']
                    }
                ]

    def make_email_container(self, email_list: dict) -> list:
        email_container = []

        for email in email_list:
            email_container.append(
                {
                    "emailAddress": {
                        "address": email
                    }
                }
            )

        return email_container

    def send_message(self, message: dict, mailbox_id: str) -> bool:
        headers = self.connection.get_headers(self.connection.get_auth_token())
        from_user = mailbox_id
        endpoint_formatted = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{from_user}/sendMail"
        result = requests.post(endpoint_formatted, headers=headers, data=message)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=result.text) from e

        # 202 Accepted is the response according to MS.
        # https://docs.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0&tabs=http
        return result.status_code == 202
