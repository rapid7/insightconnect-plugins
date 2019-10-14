import email
from email.header import decode_header, make_header
import re

from bs4 import UnicodeDammit
from base64 import b64decode
from komand.action import Action

from icon_microsoft_office365_email.util.email_cleaner import get_emails_as_list
from icon_microsoft_office365_email.util.email_cleaner import get_emails_as_string
from icon_microsoft_office365_email.util.icon_email import IconEmail
from icon_microsoft_office365_email.util.icon_file import IconFile
from icon_microsoft_office365_email.util.microsoft_newline_cleaner import remove_microsoft_newlines


class LogAction(Action):
    """
    Stub Action to be used for logging purposes. Doesn't do anything except yield a logger instance for our use
    """

    def __init__(self):
        super(self.__class__, self).__init__(
            name='LogAction',
            description='Log',
            input=None,
            output=None)

    def run(self, params={}):
        pass

    def test(self, params={}):
        pass


class EmailParser(object):
    """
    Handles all the parsing for an email.
    Acts as an abstraction layer to normalize emails into a ICONEmail that is consistent across email plugins
    and usable by Komand.
    """

    def __init__(self):
        self.logger = LogAction().logger

    def make_email_from_raw(self, message, mailbox_id):
        """
        This starts the rabbit hole of death. This is the gateway to converting a raw email string
        into an IconEmail

        :param message: Raw Message Text
        :param mailbox_id: Inbox ID that this email was received from e.g. bob@hotmail.com
        :return: IconEmail
        """

        mail = email.message_from_string(message)  # Use python to break the message up
        mail_formatted = self.format_result(self.logger, mail, mailbox_id)
        return mail_formatted

    # This builds an IconEmail from a python email object
    def format_result(self, logger, msg, mailbox_id):
        """
        This will take a python email and convert it to an IconEmail

        :param logger: logger
        :param msg: Python email
        :param mailbox_id: Mailbox ID that this message was take from
        :return: IconEmail
        """
        result = IconEmail()
        result.account = mailbox_id
        result.date_received = msg['Date']
        result.sender = get_emails_as_string(msg['From'])
        result.subject = str(make_header(decode_header(msg['Subject'])))  # This will decode mime words
        result.is_read = False
        result.recipients = self.get_recipients(logger, msg)
        result.body = self.get_body(logger, msg)
        result.headers = self.get_headers(msg)

        result.attached_files, result.attached_emails, orphan_text_list = self.attachments(msg, logger, mailbox_id)

        if orphan_text_list:
            for orphan in orphan_text_list:
                if orphan not in result.body:
                    result.body += orphan

        result.has_attachments = False
        if len(result.attached_files) > 0 or len(result.attached_emails) > 0:
            result.has_attachments = True

        return result

    def get_headers(self, msg):
        """
        Strip headers out of the message and return them in a list

        :param msg: Raw message to strip
        :return: List of headers
        """

        parser = email.parser.HeaderParser()
        headers = parser.parsestr(msg.as_string())
        header_list = []
        for h in headers.items():
            header_list.append({
                'key': h[0],
                'value': h[1]
            })
        return header_list

    def get_body(self, logger, msg):
        """
        Get the body from a raw message
        :param logger: logger
        :param msg: raw message
        :return: body as String
        """
        bdy = self.decode_body(msg, logger)
        bdy = remove_microsoft_newlines(bdy)
        return bdy

    @staticmethod
    def get_recipients(logger, msg):
        """
        Get the recipients from a raw message

        :param logger: logger
        :param msg: raw message
        :return: List of recipients
        """

        recipients = []
        if 'To' in msg:
            recipients = msg['To']
        elif 'Delivered-To' in msg:
            recipients = msg['Delivered-To']
        if not recipients:
            logger.info("No To address.")
            return []
        recipients = get_emails_as_list(recipients)
        return recipients

    def decode_body(self, msg, log):
        """
        Get the body of an email.

        :param msg: Raw message (String)
        :param log: logger
        :return: Body of the email (String)
        """
        if msg.is_multipart():
            message_content_type = msg.get_content_type()

            # We know the last part of payload is the body we want...
            # multipart alternative gives a list of alternate versions with the last version
            # being the most faithful to the original message
            # http://blog.magiksys.net/parsing-email-using-python-content
            if 'multipart/alternative' == message_content_type.lower():
                body = self.prep_multipart_alt_body(log, msg)
                return body
            else:
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get('Content-Disposition'))

                    if 'multipart/alternative' == content_type.lower():
                        body = self.prep_multipart_alt_body(log, part)
                        return body

                    elif content_type == 'text/plain' and 'attachment' not in content_disposition.lower():
                        body = self.prep_body(log, part)
                        return body

                    elif content_type == 'text/html' and 'attachment' not in content_disposition.lower():
                        body = self.prep_body(log, part)
                        return body

        else:  # NOT MULTIPART MESSAGE
            try:
                return msg.get_payload(decode=True).decode('utf-8')
            except Exception:
                log.debug("Decode failed, attempting to remove offending characters")
                return UnicodeDammit.detwingle(msg.get_payload(decode=True)).decode('utf-8', errors='ignore').replace(
                    '\n', '')

    def prep_multipart_alt_body(self, log, msg):
        """
        Takes a multipart/alternative part, extracts the payload, and decodes it if necissary.

        :param log: logger
        :param msg: multipart/alternative message
        :return: body (string)
        """
        payloads = msg.get_payload(decode=False)
        body = payloads[-1].get_payload()
        content_transfer_encoding = payloads[-1].get('Content-Transfer-Encoding')
        if "base64" == content_transfer_encoding.lower():
            body = body.replace("\n", "")
            try:
                body = b64decode(body).decode('utf-8')
            except Exception as ex:
                log.error("Failed to decode base64 body, retuning the body as is")
                log.error(ex)
                pass

        remove_microsoft_newlines(body)
        return body

    @staticmethod
    def prep_body(log, part):
        """
        This method takes a part, retrieves the payload, and preps that payload by decoding it and removing unnecessary
        newlines.

        :param log: logger
        :param part: html or text message
        :return: body (string)
        """
        try:
            body = part.get_payload(decode=True).decode('utf-8').replace('\n', '')  # decode
        except Exception as ex:
            log.debug(ex)
            log.debug(
                "Failed to parse email as UTF-8, attempting to detwingle first before retrying parse")
            body = UnicodeDammit.detwingle(part.get_payload(decode=True)). \
                decode('utf-8', errors='ignore'). \
                replace('\n', '')
            remove_microsoft_newlines(body)
        return body

    def attachments(self, mail, log, mailbox_id):
        """
        Decode attachments from the raw message

        :param mail: Raw message to decode
        :param log: logger
        :param mailbox_id: Mailbox ID that this message was received from
        :return:
        file_attachments - List of IconFiles
        email_attachments - List of IconEmails
        """

        orphaned_text = []  # For some reason, we will get text parts not associated with any emails
        file_attachments = []
        email_attachments = []

        filename_pattern = re.compile('name=".*"')
        count = 0

        for part in mail.walk():
            count += 1

            content_type = part.get_content_maintype()
            log.info(f"Content main type: {content_type}")

            # can't do anything with these, skip them.
            if not content_type or content_type == 'multipart':
                continue

            ##################
            # Email Attachments
            ##################

            if part.get_content_maintype() == 'message':
                if part.is_multipart():
                    log.info("Parsing attached multipart email")
                    content = part.get_payload()
                    # EMAILCEPTION
                    for message in content:
                        new_message = self.format_result(log, message, mailbox_id)
                        email_attachments.append(new_message)
                else:
                    log.info("Parsing attached email")
                    content = part.get_payload()
                    new_email = self.make_email_from_raw(content, mailbox_id)
                    email_attachments.append(new_email)
                continue

            ##################
            # Orphan Text - Text with no discernible type or associated part.
            ##################

            # content_full_type = part.get_content_type()
            # content_disposition = part.get_content_disposition()
            # if content_full_type == 'text/plain' and not content_disposition == 'attachment':
            #     log.info("Orphaned text found, will append to base email")
            #     orphan_text = part.get_payload()
            #     orphan_text = orphan_text.strip()
            #     orphaned_text.append(orphan_text)
            #     continue

            # We've tried all the message types...

            filename = part.get_filename()

            #################
            # File Attachments
            #################
            if filename is None:
                # Attempt to get filename from Content-Type header
                part_content_type = part.get('Content-Type')
                content_line = []
                if part_content_type:
                    content_line = filename_pattern.findall(part_content_type)
                # Test if array has contents
                if content_line:
                    # Attempt parsing filename, it *might* be here
                    filename = content_line[0].lstrip('name=').strip('"')
                    log.debug('Content-Type filename: %s', filename)

            # If we still don't have a file name, skip this part
            if not filename:
                log.info("Could not find filename of attachment, ignoring attachment.")
                continue
                # filename = 'Attachment-{}'.format(count)
                # log.debug('Dynamic filename: %s', filename)

            content = part.get_payload(decode=False)

            # If not a string
            if not isinstance(content, str):
                content = part.as_string()
                log.debug('Content not string')

            content = content.replace("\r\n", "")

            content_transfer_encoding = part.get("Content-Transfer-Encoding", "")
            if content_transfer_encoding.lower() == 'base64':
                content = content.replace("\n", "")

            icon_file = IconFile(file_name=filename,
                                 content_type=part.get_content_type(),
                                 content=content)

            #################
            #  Attached .eml
            #################
            icon_file.file_name = str(make_header(decode_header(icon_file.file_name)))  # Unicode file names will be encoded
            if icon_file.file_name.endswith(".eml"):
                try:
                    converted_file = self.convert_icon_file_to_email(icon_file, mailbox_id)
                    email_attachments.append(converted_file)
                    continue
                except Exception:  # Conversion failed, attach it as a file.
                    self.logger.info(f"Conversion of {icon_file.file_name} failed, attaching as file")

            file_attachments.append(icon_file)

        # Remove duplicates. Python will have the same orphan at different levels
        # in the email tree
        orphaned_text = list(set(orphaned_text))

        return file_attachments, email_attachments, orphaned_text

    def convert_icon_file_to_email(self, icon_file, mailbox_id):
        """
        This will take an icon file and try to convert it's contents to a IconEmail

        :param icon_file: IconFile
        :param mailbox_id: Mailbox ID that is being operated on
        :return: IconEmail
        """

        self.logger.info(f"{icon_file.file_name} appears to be an .eml. Attempting to convert")
        decoded_bytes = b64decode(icon_file.content)
        decoded_string = decoded_bytes.decode()
        converted_email = self.make_email_from_raw(decoded_string, mailbox_id)
        self.logger.info(f"Conversion of {icon_file.file_name} succeeded")
        return converted_email
