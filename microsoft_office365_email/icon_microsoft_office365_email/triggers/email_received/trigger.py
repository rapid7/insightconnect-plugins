import re
import time

import komand
import maya
# Custom imports below
import requests
from komand.exceptions import PluginException

from icon_microsoft_office365_email.util.email_parser import EmailParser
from icon_microsoft_office365_email.util.icon_email import IconEmail
from icon_microsoft_office365_email.util.icon_file import IconFile
from .schema import EmailReceivedInput, EmailReceivedOutput, Input, Output, Component


class EmailReceived(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='email_received',
            description=Component.DESCRIPTION,
            input=EmailReceivedInput(),
            output=EmailReceivedOutput())

        self.MESSAGES_ENDPOINT = "https://graph.microsoft.com/v1.0/{tenant_id}/users/{mailbox_id}/messages"
        self.MESSAGES_WITH_FOLDER_ENDPOINT = "https://graph.microsoft.com/v1.0/{tenant_id}/users/{mailbox_id}/mailFolders/{folder_id}/messages"
        self.GET_FOLDERS_ENDPOINT = "https://graph.microsoft.com/v1.0/{tenant_id}/users/{mailbox_id}/mailFolders"
        self.GET_ATTACHMENTS_ENDPOINT = "https://graph.microsoft.com/v1.0/{tenant_id}/users/{mailbox_id}/messages/{message_id}/attachments?$expand=microsoft.graph.itemattachment/item"
        self.GET_RAW_ATTACHMENT_ENDPOINT = "https://graph.microsoft.com/beta/{tenant_id}/users/{mailbox_id}/messages/{message_id}/attachments/{attachment_id}/$value"
        self.HEADERS_ENDPOINT = "https://graph.microsoft.com/v1.0/{tenant_id}/users/{mailbox_id}/messages/{message_id}/?$select=internetMessageHeaders"

    def run(self, params={}):
        interval = params.get(Input.INTERVAL, 15)
        mailbox_id = params.get(Input.MAILBOX_ID, "")
        folder_name = params.get(Input.FOLDER_NAME, "")
        folder_id = ""
        subject_query = params.get(Input.SUBJECT_QUERY, "")

        self.current_time = maya.now()

        if folder_name:
            folder_id = self.find_folder(folder_name, mailbox_id)

        """Run the trigger"""
        while True:
            messages = self.get_microsoft_messages(tenant_id=self.connection.tenant,
                                                   mailbox_id=mailbox_id,
                                                   folder_id=folder_id)

            # check for new messages and reset current time if needed
            new_messages = self.get_new_messages(messages, self.current_time)

            # filter by subject
            new_messages = self.filter_messages_by_subject(subject_query, new_messages)

            if new_messages:
                for message in new_messages:
                    icon_email_ready_to_send = self.make_message_ready_to_send(mailbox_id,
                                                                               message,
                                                                               params.get(Input.FLATTEN_ATTACHMENTS, False))

                    self.send({Output.ICON_EMAIL: icon_email_ready_to_send})
                    self.logger.info("\n")  # Send doesn't end with a newline, this helps break up the log
            else:
                self.logger.info("No new messages found.")

            self.logger.info(f"Sleeping for {interval} seconds.\n\n")
            time.sleep(interval)

    def make_message_ready_to_send(self, mailbox_id, message, flatten):
        message["file_attachments"], message["message_attachments"] = self.get_attachments(message,
                                                                                           mailbox_id)
        icon_email_to_send = IconEmail.convert_message_to_icon_email(self.logger, message, mailbox_id)
        icon_email_to_send.headers = self.get_microsoft_message_headers(tenant=self.connection.tenant,
                                                                        mailbox_id=mailbox_id,
                                                                        message_id=icon_email_to_send.id)
        if flatten:
            icon_email_to_send.flatten()
        icon_email_ready_to_send = icon_email_to_send.make_serializable()
        return icon_email_ready_to_send

    # output: Files, Email
    def get_attachments(self, message, mailbox_id) -> (list, list):
        """
        This function will return all attachments associated with a microsoft message.

        It returns two lists, file attachments and email attachments
        :param message: A Microsoft Message
        :param mailbox_id: The account used to retrieve this message. e.g. Bob@hotmail.com
        :return:
        file-attachments: A list of IconFiles
        email-attachments: A list of IconEmails
        """
        if not message.get("hasAttachments"):
            return [], []

        message_id = message.get("id")
        headers = self.connection.get_headers(self.connection.get_auth_token())
        get_attachment_endpoint_formatted = self.GET_ATTACHMENTS_ENDPOINT.format(tenant_id=self.connection.tenant,
                                                                                 mailbox_id=mailbox_id,
                                                                                 message_id=message_id)

        self.logger.info(f"Getting attachments from: {get_attachment_endpoint_formatted}")
        response = requests.get(get_attachment_endpoint_formatted, headers=headers)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR,
                                  data=response.text) from e

        microsoft_attachments = []
        try:
            microsoft_attachments = response.json().get("value")
        except Exception as e:
            PluginException(preset=PluginException.Preset.INVALID_JSON,
                            data=e)

        file_attachments = []
        email_attachments = []

        for microsoft_attachment in microsoft_attachments:
            self.set_attachments(microsoft_attachment, file_attachments, email_attachments, mailbox_id, message_id)

        return file_attachments, email_attachments

    def set_attachments(self, attachment, file_attachments, email_attachments, mailbox_id, message_id):
        """
        This function takes the file_attachments and email_attachments lists and adds respective attachments if
        available.

        :param attachment: A microsoft attachment (dict)
        :param file_attachments: A mutable list
        :param email_attachments: A mutable list
        :param mailbox_id: Target mailbox for this operation
        :param message_id: Message ID that is being acted on
        :return:
        None
        """

        email_parser = EmailParser()

        ###########
        # Email Attachments
        ###########
        if "itemAttachment" in attachment.get("@odata.type"):  # Email Attachment
            self.logger.info("Email attachment found")
            self.logger.info(f"Attached email has attachments: {attachment.get('item').get('hasAttachments')}")

            # Here we have a decision to make. If the attachment has more attachments, we can't use the
            # regular Microsoft API, it won't allow us to get attachments of attachments.
            # What this does:
            # If there are no attachments, go ahead and return what we have
            # If there are attachments, we need to get the attachment as a raw object and try to parse it
            if attachment.get("item").get("hasAttachments"):
                # Go get the raw attachment.
                raw_email_attachment = self.get_raw_attachment(self.connection.tenant,
                                                               mailbox_id,
                                                               message_id,
                                                               attachment.get("id"))

                email_attachment = email_parser.make_email_from_raw(raw_email_attachment, mailbox_id)
                email_attachment.id = attachment.get("id")
                email_attachments.append(email_attachment)
            else:
                email_attachments.append(IconEmail.convert_item_attachment(self.logger, attachment, mailbox_id))

        ###########
        # File Attachments
        ###########
        elif "fileAttachment" in attachment.get("@odata.type"):  # File Attachment
            self.logger.info("File attachment found")
            content_type = attachment.get("contentType", "")
            file_name = attachment.get("name", "")
            content_bytes = attachment.get("contentBytes", "")

            self.logger.info(f"Filename: {file_name}")
            self.logger.info(f"Content-type: {content_type}")

            icon_file = IconFile(file_name, content_type, content_bytes)

            ###########
            # Check for email attachments and try to convert those back to IconEmails
            ###########
            if icon_file.file_name.endswith(".eml"):
                try:
                    converted_file = email_parser.convert_icon_file_to_email(icon_file, mailbox_id)
                    email_attachments.append(converted_file)
                except Exception:  # Conversion failed, attach it as a file.
                    self.logger.info(f"Conversion of {icon_file.file_name} failed, attaching as file")
                    file_attachments.append(icon_file)
            else:
                file_attachments.append(icon_file)  # Not an email

        else:  # Contact type attachment - can't really deal with this
            pass

    def get_raw_attachment(self, tenant, mailbox_id, message_id, attachment_id):
        """
        This function will retrieve an attachment as raw text using the Microsoft beta endpoint for
        getting raw email text.

        :param tenant: Tenant ID
        :param mailbox_id: Mailbox ID to retrieve messages from
        :param message_id: Message ID that we are looking for attachments from
        :param attachment_id: Attachment ID to get
        :return:
        Raw Attachment Text (String)
        """
        headers = self.connection.get_headers(self.connection.get_auth_token())
        raw_message_endpoint_formatted = self.GET_RAW_ATTACHMENT_ENDPOINT.format(tenant_id=tenant,
                                                                                 mailbox_id=mailbox_id,
                                                                                 message_id=message_id,
                                                                                 attachment_id=attachment_id)

        self.logger.info(f"Getting raw attachment from: {raw_message_endpoint_formatted}")
        raw_attachment_response = requests.get(raw_message_endpoint_formatted, headers=headers)
        try:
            raw_attachment_response.raise_for_status()
        except requests.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR,
                                  data=raw_attachment_response.text) from e

        return raw_attachment_response.text

    def filter_messages_by_subject(self, subject_query, messages):
        """
        Will take a list of messages and filter them based on the subject query. It will only return
        those messages that salinity the subject query.

        :param subject_query: Regular Expression to match messages against
        :param messages: List of messages to query against
        :return:
        Messages - List of IconEmails that match the subject query
        """
        if not subject_query:
            return messages

        messages_to_return = []
        for message in messages:
            try:
                subject_regex_object = re.compile(subject_query)
            except re.error:
                raise PluginException(
                    cause="Invalid subject_query regular expression",
                    assistance="Check the subject_query input and verify it is a valid regular expression.")
            subject = message.get('subject')
            self.logger.info(f"Checking regex: {subject_query}\nin subject: {subject}")
            if subject_regex_object.search(subject):
                messages_to_return.append(message)

        return messages_to_return

    def get_new_messages(self, messages, time_):
        """
        This function looks for new messages, and updates the most recent time we looked for messages

        :param messages: A list of messages
        :param time_: The most recent time we've looked for messages
        :return:
        List of Messages that are more recent than the time parameter
        """
        messages_to_return = []

        if messages and (len(messages) > 0):  # Need this in case we had an empty mailbox
            most_recent_time = self.convert_to_time(messages[0].get("receivedDateTime"))
            if most_recent_time > time_:  # we have new messages
                self.logger.info("New emails received")
                self.current_time = most_recent_time
                for message in messages:
                    if self.convert_to_time(message.get("receivedDateTime")) > time_:
                        messages_to_return.append(message)

        return messages_to_return

    def convert_to_time(self, time):
        """
        Convert time to a MayaDT
        :param time: String to convert
        :return:
        MayaDT
        """
        return maya.MayaDT.from_iso8601(time)

    def find_folder(self, folder_name, mailbox_id):
        """
        Find the folder ID specified by the user

        :param folder_name: Folder name to look for e.g. Inobx, Phishy Stuff
        :param mailbox_id: The Mailbox ID to check for folders e.g. bob@hotmail.com
        :return:
        Mailbox ID (String)
        """

        headers = self.connection.get_headers(self.connection.get_auth_token())
        folders_endpoint_formatted = self.GET_FOLDERS_ENDPOINT.format(tenant_id=self.connection.tenant,
                                                                      mailbox_id=mailbox_id)
        try:
            request = requests.get(folders_endpoint_formatted, headers=headers)
            response = request.json()
            folders_list = response.get('value')

            # See if we have more than 10 folders, if so the API sends the link to get the next 10
            next_link = response.get('@odata.nextLink')
            while next_link:
                self.logger.info(f"Looking for additional folders: {next_link}")
                request = requests.get(next_link, headers=headers)
                response = request.json()
                folders_list.extend(response.get('value'))
                next_link = response.get('@odata.nextLink')
        except Exception as e:
            raise PluginException(cause="Unable to get folders.",
                                  assistance="Folder name or connection settings may be incorrect, see following error for more information.",
                                  data=e)
        self.logger.info(f"Looking for {folder_name}")
        for folder in folders_list:
            self.logger.info(f"Checking {folder.get('displayName')}")
            if folder_name == folder.get("displayName"):
                self.logger.info(f"Folder found")
                return folder.get("id")

        raise PluginException(cause=f"Folder named {folder_name} was not found",
                              assistance=f"Please check the folder name and verify it exists in {mailbox_id}")

    def get_microsoft_messages(self, tenant_id, mailbox_id, folder_id=""):
        """
        Get all Microsoft Messages from the target Inbox in Descending order by date received

        :param tenant_id: Tenant ID
        :param mailbox_id: Mailbox ID to check
        :param folder_id: Folder ID to retrieve messages from
        :return:
        A list of microsoft messages in descending order of date received
        """
        if folder_id:
            message_endpoint_formatted = self.MESSAGES_WITH_FOLDER_ENDPOINT. \
                format(tenant_id=self.connection.tenant, mailbox_id=mailbox_id, folder_id=folder_id)
        else:
            message_endpoint_formatted = self.MESSAGES_ENDPOINT.format(tenant_id=tenant_id, mailbox_id=mailbox_id)

        message_endpoint_formatted += "?$orderby=receivedDateTime DESC"
        headers = self.connection.get_headers(self.connection.get_auth_token())

        self.logger.info(f"Getting emails from: {message_endpoint_formatted}")

        try:
            response = requests.get(message_endpoint_formatted, headers=headers)
        except requests.exceptions.ConnectionError as e:
            self.logger.info(f"Exception was thrown while attempting to retrieve emails. Forcing sleep then retrying.")
            self.logger.info(f"Exception: {e}")
            self.logger.info("Sleeping for 5 seconds")
            time.sleep(5)
            self.logger.info("Attempting to get emails again.")
            response = requests.get(message_endpoint_formatted, headers=headers)

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR,
                                  data=response.text) from e

        try:
            messages = response.json().get("value")
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON) from e

        return messages

    def get_microsoft_message_headers(self, tenant, mailbox_id, message_id):
        """
        This will get the headers for a Microsoft Message, these are not returned by default.

        :param tenant: Tenant ID that the message is in
        :param mailbox_id: Mailbox ID that the message is in
        :param message_id: Message ID to get headers from
        :return:
        A list of headers
        """
        headers = self.connection.get_headers(self.connection.get_auth_token())
        headers_endpoint_formatted = self.HEADERS_ENDPOINT.format(tenant_id=tenant,
                                                                  mailbox_id=mailbox_id,
                                                                  message_id=message_id)

        self.logger.info(f"Getting internet headers from: {headers_endpoint_formatted}")
        headers_response = requests.get(headers_endpoint_formatted, headers=headers)
        try:
            headers_response.raise_for_status()
        except requests.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR,
                                  data=headers_response.text) from e

        try:
            headers = headers_response.json().get("internetMessageHeaders")
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON) from e

        return headers
