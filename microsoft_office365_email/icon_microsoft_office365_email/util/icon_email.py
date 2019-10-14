import base64
import datetime
import json
from komand.exceptions import PluginException

from komand import helper


class IconEmail(object):
    """
    Base class to hold plugin-usable information for a common Email type
    """

    def __init__(self, **kwargs):
        self.account = kwargs.get("account", None)
        self.recipients = kwargs.get("recipients", None)
        self.is_read = kwargs.get("is_read", None)
        self.id = kwargs.get("id", None)
        self.sender = kwargs.get("sender", None)
        self.subject = kwargs.get("subject", None)
        self.body = kwargs.get("body", None)
        self.categories = kwargs.get("categories", None)
        self.date_received = kwargs.get("date_received", None)
        self.headers = kwargs.get("headers", None)
        self.attached_files = kwargs.get("attached_files", [])
        self.attached_emails = kwargs.get("attached_emails", [])
        self.has_attachments = kwargs.get("has_attachments", False)
        self.flattened_attached_files = []
        self.flattened_attached_emails = []

    @staticmethod
    def convert_item_attachment(logger, attachment, account_id=""):
        """
        This method will convert a raw Microsoft ItemAttachment to an IconEmail

        :param logger: Logger
        :param attachment: Item to convert
        :param account_id: Account ID this item was retrieved from
        :return:
        IconEmail
        """
        base_item = attachment.get("item")

        try:
            sender = base_item.get('from').get('emailAddress').get('address')
        except Exception:
            logger.info("No from value found in attached email")
            sender = ""

        try:
            toRecipients = []
            for recipient in base_item.get('toRecipients'):
                toRecipients.append(recipient.get('emailAddress').get('address'))
        except Exception:
            toRecipients = ['']

        try:
            body = base_item.get('body').get('content')
        except Exception:
            body = ""

        # This is an attached email, we have no clue what account it's associated with, using the target mailbox instead
        icon_email = IconEmail(account=account_id,
                               recipients=toRecipients,
                               is_read=base_item.get('isRead', False),
                               id=base_item.get('id', ""),  # item attachemns have blank IDs.
                               sender=sender,
                               subject=base_item.get('subject', ""),
                               body=body,
                               categories=[],
                               file_attachments=[],
                               has_attachments=base_item.get('hasAttachments', False),
                               email_attachments=[],
                               date_received=base_item.get('receivedDateTime', ""),
                               headers=base_item.get('internetMessageHeaders', []),
                               )
        return icon_email

    @staticmethod
    def json_handler(obj):
        """
        This is used by the make serialization class to help convert odd attachments to JSON.

        :param obj: Object - Anything json.dumps can't handle will be passed as this
        :return:
        A serializable dictionary
        """
        try:
            if isinstance(obj, bytes):
                return base64.b64encode(obj).decode()

            dict_obj = obj.__dict__

            for key in list(dict_obj.keys()):
                if isinstance(dict_obj.get(key), datetime.datetime):
                    dict_obj[key] = dict_obj.get(key).isoformat()

            return dict_obj

        except Exception as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=e)

    def make_serializable(self) -> dict:
        """
        Converts the Email to a JSON-serializable, cleaned dict
        :return:
        dict
        """
        message_json = json.dumps(self, default=self.json_handler, sort_keys=True, indent=4)
        message_json = json.loads(message_json, strict=False)

        message_json_clean = helper.clean(message_json)
        return message_json_clean

    def flatten(self):
        """
        This will go through all the attachments and return them as a flat list instead of a
        nested list of emails
        :return:
        None - (Will flatten self.attached_emails and self.attached_files)
        """
        if self.attached_emails:
            self.flattened_attached_emails = self.flatten_email(self.attached_emails)
        self.flattened_attached_files.extend(self.attached_files)

        # Nuke duplicates
        self.flattened_attached_emails = list(set(self.flattened_attached_emails))
        self.flattened_attached_files = list(set(self.flattened_attached_files))

        # Need to sort the list for testability
        # python hash adds a random seed to all hashes on launch, which makes these pop out in random order
        self.flattened_attached_emails.sort()
        self.flattened_attached_files.sort()

    def flatten_email(self, email_list: list):
        """
        Recursive function that will flatten email_attachments and file attachments

        As it marches through the tree of emails, it will also add any files found to the
        flattened_attached_files list as well.

        :param email_list: List of emails to flatten
        :return:
        Flat list of emails
        * Modifies file_attachments to be a list of all attachments in the email tree that is being flattened
        """
        ret_val = []

        for email in email_list:
            if len(email.attached_emails) > 0:
                ret_val.extend(self.flatten_email(email.attached_emails))

            ret_val.append(email)

            if len(email.attached_files) > 0:
                self.flattened_attached_files.extend(email.attached_files)

        return ret_val

    @classmethod
    def convert_message_to_icon_email(cls, logger, message, mailbox_id):
        """
        Takes a Microsoft Message and converts it to an IconEmail

        :param logger: logger
        :param message: Message to convert
        :param mailbox_id: Mailbox ID that this message came from
        :return:
        IconEmail
        """
        base_item = message

        try:
            sender = base_item.get('from').get('emailAddress').get('address')
        except Exception:
            logger.info("No from value found in attached email")
            sender = ''

        try:
            toRecipients = []
            for recipient in base_item.get('toRecipients'):
                toRecipients.append(recipient.get('emailAddress').get('address'))
        except Exception:
            toRecipients = ['']

        has_attachments = False
        if (base_item.get('file_attachments')):
            logger.info("Setting file attachments")
            file_attachments = base_item.get('file_attachments')
        else:
            file_attachments = []

        if base_item.get('message_attachments'):
            logger.info("Setting email attachments")
            email_attachments = base_item.get('message_attachments')
        else:
            email_attachments = []

        if len(file_attachments) > 0 or len(email_attachments) > 0:
            has_attachments = True

        try:
            body = base_item.get('body').get('content')
        except Exception:
            body = ""

        # This is an attached email, we have no clue what account it's associated with, using the target mailbox instead
        icon_email = cls(account=mailbox_id,
                         recipients=toRecipients,
                         is_read=base_item.get('isRead', False),
                         id=base_item.get('id', ""),  # item attachemns have blank IDs.
                         sender=sender,
                         subject=base_item.get('subject', ""),
                         body=body,
                         categories=base_item.get('categories', []),
                         attached_files=file_attachments,
                         has_attachments=has_attachments,
                         attached_emails=email_attachments,
                         date_received=base_item.get('receivedDateTime', ""),
                         headers=base_item.get('internetMessageHeaders', []),
                         )

        return icon_email

    # These functions are needed for equality and hashing. They
    # are used to remove duplicates in the flattened lists.

    def __eq__(self, other):
        """ Check for equality """
        return (self.id == other.id
                and self.subject == other.subject
                and self.body == other.body
                and self.date_received == other.date_received
                and self.recipients == other.recipients
                and self.sender == other.sender
                and self.account == other.account
                and self.categories == other.categories)

    def __hash__(self):
        """ Return a unique hash """

        # 'Tue, 13 Aug 2019 12:56:31 -0500'
        return hash(('id', self.id,
                     'subject', str(self.subject),
                     'body', self.body,
                     'date_received', self.date_received,
                     'recipients', str(self.recipients),
                     'sender', self.sender,
                     'account', self.account,
                     'categories', str(self.categories)))

    def __lt__(self, other):
        """ Less than, allows class to be sorted"""
        return self.subject < other.subject
