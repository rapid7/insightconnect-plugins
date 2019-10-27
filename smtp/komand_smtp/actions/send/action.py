import komand
import json
from .schema import SendInput, SendOutput

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

        msg['Subject'] = params.get('subject')
        msg['From'] = params['email_from']
        msg['To'] = params['email_to']
        html = params['html']
        emails.append(params['email_to'])

        cc_emails = []
        bcc_emails = []
        if params.get('cc'):
            msg['CC'] = ', '.join(params['cc'])
            cc_emails = params['cc']
            emails = emails + cc_emails
        if params.get('bcc'):
            bcc_emails = params['bcc']
            emails = emails + bcc_emails

        msg.attach(MIMEText(params.get('message'), 'plain' if not html else 'html'))

        # Check if attachment exists. If it does, attach it!
        attachment = params.get("attachment", {"content": "", "filename": ""})
        if attachment is not None and len(attachment.get("content")) > 0:
            self.logger.info("Found attachment! Attaching...")
            attachment_base64 = params.get("attachment").get("content")
            attachment_filename = params.get("attachment").get("filename")

            # Prepare the attachment. Parts of this code below pulled out of encoders.encode_base64.
            # Since we already have base64, don't bother calling that func since it does too much.
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment_base64)
            part['Content-Transfer-Encoding'] = 'base64'
            part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_filename)
            msg.attach(part)

        client.sendmail(
            params['email_from'],
            emails,
            msg.as_string(),
        )
        client.quit()
        return {'result': 'ok'}

    def test(self, params={}):
        """Test action"""
        client = self.connection.get()
        return {'result': 'ok'}