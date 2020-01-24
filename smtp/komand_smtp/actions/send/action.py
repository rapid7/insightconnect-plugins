import komand
from .schema import SendInput, SendOutput, Input, Output

# Custom imports below
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


class Send(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='send',
            description='Send an email',
            input=SendInput(),
            output=SendOutput())

    def run(self, params={}):
        """Run action"""

        client = self.connection.get()
        msg = MIMEMultipart()
        emails = []

        msg['Subject'] = params.get(Input.SUBJECT)
        msg['From'] = params.get(Input.EMAIL_FROM)
        msg['To'] = params.get(Input.EMAIL_TO)
        html = params.get(Input.HTML)
        emails.append(params.get(Input.EMAIL_TO))

        if params.get(Input.CC):
            msg['CC'] = ', '.join(params.get(Input.CC))
            cc_emails = params.get(Input.CC)
            emails = emails + cc_emails
        if params.get(Input.BCC):
            bcc_emails = params.get(Input.BCC)
            emails = emails + bcc_emails

        msg.attach(MIMEText(params.get(Input.MESSAGE), 'plain' if not html else 'html'))

        # Check if attachment exists. If it does, attach it!
        attachment = params.get(Input.ATTACHMENT)
        if attachment is not None and attachment.get("content"):
            self.logger.info("Found attachment! Attaching...")
            attachment_base64 = attachment.get("content")
            attachment_filename = attachment.get("filename")

            # Prepare the attachment. Parts of this code below pulled out of encoders.encode_base64.
            # Since we already have base64, don't bother calling that func since it does too much.
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment_base64)
            part['Content-Transfer-Encoding'] = 'base64'
            part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_filename)
            msg.attach(part)

        client.sendmail(
            params.get(Input.EMAIL_FROM),
            emails,
            msg.as_string(),
        )
        client.quit()
        return {Output.RESULT: 'ok'}

    def test(self, params={}):
        """Test action"""
        client = self.connection.get()
        return {Output.RESULT: 'ok'}