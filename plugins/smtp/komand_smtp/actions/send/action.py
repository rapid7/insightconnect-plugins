import insightconnect_plugin_runtime
from .schema import SendInput, SendOutput, Input, Output, Component

# Custom imports below
from email.errors import MessageError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPException

from insightconnect_plugin_runtime.exceptions import PluginException

from komand_smtp.util.helpers import (
    clean_addresses,
    close_client,
    create_attachment_part,
    describe_smtp_error,
    describe_refused_recipients,
)


class Send(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send",
            description=Component.DESCRIPTION,
            input=SendInput(),
            output=SendOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        attachments = params.get(Input.ATTACHMENTS, [])
        bcc = params.get(Input.BCC, [])
        cc = params.get(Input.CC, [])
        email_from = params.get(Input.EMAIL_FROM, "")
        email_to = params.get(Input.EMAIL_TO, "")
        html = params.get(Input.HTML, False)
        message = params.get(Input.MESSAGE, "")
        subject = params.get(Input.SUBJECT, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Blank entries would otherwise be sent as empty recipients
        cc = clean_addresses(cc)
        bcc = clean_addresses(bcc)

        # Prepare the message
        email_message = MIMEMultipart()
        email_message["Subject"] = subject
        email_message["From"] = email_from
        email_message["To"] = email_to
        recipients = [email_to, *cc, *bcc]

        # In case there's `cc` fields, add it to the message
        if cc:
            email_message["CC"] = ", ".join(cc)

        # Add message content
        email_message.attach(MIMEText(message, "html" if html else "plain"))

        # Entries without content are skipped. Parts are built before connecting so invalid attachments fail fast.
        # Each file keeps its position in the input, so errors point to the right entry.
        files_to_attach = [
            (f"{Input.ATTACHMENTS}[{index}]", file)
            for index, file in enumerate(attachments)
            if file and (file.get("content") or "").strip()
        ]
        if files_to_attach:
            self.logger.info(f"Attaching {len(files_to_attach)} file(s) to the email")
            for label, attached_file in files_to_attach:
                email_message.attach(create_attachment_part(attached_file, label))

        # Serialize before connecting, so invalid headers (e.g. line breaks in the subject) fail fast
        try:
            email_text = email_message.as_string()
        except (MessageError, ValueError) as error:
            raise PluginException(
                cause="Failed to build the email.",
                assistance="Verify that the subject and addresses do not contain invalid characters such as line breaks.",
                data=str(error),
            ) from error

        # Connection errors are raised by `get()` as PluginException
        client = self.connection.get()
        try:
            self.logger.info(f"Sending the email to {len(recipients)} recipient(s)")
            refused = client.sendmail(email_from, recipients, email_text)
        except (SMTPException, OSError, UnicodeError) as error:
            raise PluginException(
                cause="Failed to send the email.",
                assistance="Verify the sender and recipient addresses and the SMTP server configuration.",
                data=describe_smtp_error(error),
            )
        finally:
            close_client(client)

        # `sendmail` only raises when every recipient is refused; partial refusals are returned
        if refused:
            raise PluginException(
                cause="The SMTP server refused some of the recipients.",
                assistance="The email was delivered to the remaining recipients. Verify the refused addresses and the server limits.",
                data=describe_refused_recipients(refused),
            )

        # Email sent successfully
        return {Output.RESULT: "ok"}
