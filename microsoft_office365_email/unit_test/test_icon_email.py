from komand.exceptions import PluginException
from unittest import TestCase
from icon_microsoft_office365_email.util.icon_email import IconEmail
from icon_microsoft_office365_email.util.icon_file import IconFile
from icon_microsoft_office365_email.util.email_parser import EmailParser
import json
import logging
import datetime

BASIC_MESSAGE_PAYLOAD = "./payloads/get_messages_payload_one_basic_message.json"
BASIC_ATTACHMENT_PAYLOAD = "./payloads/get_attachment_email_payload.json"


# Get a real payload from file
def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


class test_icon_email(TestCase):
    def setUp(self) -> None:
        self.logger = logging.getLogger("Test")
        pass

    def test_create_blank_email(self):
        email = IconEmail()
        self.assertEqual(email.id, None)
        self.assertEqual(email.recipients, None)
        self.assertEqual(email.is_read, None)
        self.assertEqual(email.sender, None)
        self.assertEqual(email.subject, None)

    def test_create_email(self):
        params = {
            "account": "test_account@test.com",
            "recipients": "[test@test.com]",
            "is_read": True,
            "id": "test_id",
            "sender": "someguy@test.com",
            "body": "This is some text",
            "categories": ["Foo", "Bar"],
            "date_received": "Today",
            "headers": [{"header1": "value1"}]
        }

        email = IconEmail(**params)
        self.assertEqual(email.account, "test_account@test.com")
        self.assertEqual(email.recipients, "[test@test.com]")
        self.assertEqual(email.is_read, True)
        self.assertEqual(email.id, "test_id")
        self.assertEqual(email.sender, "someguy@test.com")
        self.assertEqual(email.body, "This is some text")
        self.assertEqual(email.categories, ["Foo", "Bar"])
        self.assertEqual(email.date_received, "Today")
        self.assertEqual(email.headers, [{"header1": "value1"}])
        self.assertEqual(email.has_attachments, False)
        self.assertEqual(email.attached_files, [])
        self.assertEqual(email.attached_emails, [])
        self.assertEqual(email.flattened_attached_emails, [])
        self.assertEqual(email.flattened_attached_files, [])

    def test_convert_message_to_icon_email(self):
        basic_message = json.loads(read_file_to_string(BASIC_MESSAGE_PAYLOAD)).get('value')[0]
        icon_email = IconEmail()
        email = icon_email.convert_message_to_icon_email(self.logger, basic_message, "mclovin")

        self.assertEqual(email.account, "mclovin")
        self.assertEqual(email.recipients, ["jschipp@komanddev.onmicrosoft.com"])
        self.assertEqual(email.is_read, False)
        self.assertEqual(email.id, 'AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAAAAEKAAC8UQDN7ObVSLWQuxHJ-dDTAAE4BZLGAAA=')
        self.assertEqual(email.sender, 'joey_mcadams@rapid7.com')
        self.assertEqual(email.body, "This is some test text for the body.")
        self.assertEqual(email.categories, [])
        self.assertEqual(email.date_received, '2019-08-09T15:56:16Z')
        self.assertEqual(email.headers, [])  # This is OK, we get headers in the main loop, they don't come by default
        self.assertEqual(email.has_attachments, False)
        self.assertEqual(email.attached_files, [])
        self.assertEqual(email.attached_emails, [])
        self.assertEqual(email.flattened_attached_emails, [])
        self.assertEqual(email.flattened_attached_files, [])

    def test_convert_item_attachment(self):
        basic_message = json.loads(read_file_to_string(BASIC_ATTACHMENT_PAYLOAD)).get('value')[0]
        icon_email = IconEmail()
        email = icon_email.convert_item_attachment(self.logger, basic_message, "mclovin")

        self.assertEqual(email.account, "mclovin")
        self.assertEqual(email.recipients, ["chakan2@hotmail.com"])
        self.assertEqual(email.is_read, True)
        self.assertEqual(email.id, "")
        self.assertEqual(email.sender, 'chakan2@hotmail.com')
        expected_body = "<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n<style type=\"text/css\" style=\"display:none;\"> P {margin-top:0;margin-bottom:0;} </style>\r\n</head>\r\n<body dir=\"ltr\">\r\n<div style=\"font-family: Calibri, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0);\">\r\nAttachment Body</div>\r\n</body>\r\n</html>\r\n"
        self.assertEqual(email.body, expected_body)
        self.assertEqual(email.categories, [])
        self.assertEqual(email.date_received, '2019-08-06T19:19:47Z')
        self.assertEqual(len(email.headers), 72)
        self.assertEqual(email.has_attachments, False)
        self.assertEqual(email.attached_files, [])
        self.assertEqual(email.attached_emails, [])
        self.assertEqual(email.flattened_attached_emails, [])
        self.assertEqual(email.flattened_attached_files, [])

    def test_convert_item_attachment_with_null_values(self):
        basic_message = {
            "item": {
                "value": [{

                }]
            }
        }

        icon_email = IconEmail()
        actual = icon_email.convert_item_attachment(self.logger, basic_message, "some_fake_account")

        self.assertEqual(actual.sender, "")
        self.assertEqual(actual.recipients, [""])
        self.assertEqual(actual.body, "")

    def test_convert_message_to_icon_email_with_null_values(self):
        basic_message = {
            "value": [{
            }]
        }

        icon_email = IconEmail()
        actual = icon_email.convert_message_to_icon_email(self.logger, basic_message, "some_fake_account")

        self.assertEqual(actual.sender, "")
        self.assertEqual(actual.recipients, [""])
        self.assertEqual(actual.body, "")

    def test_make_serializable(self):
        icon_email = IconEmail()
        actual = icon_email.make_serializable()

        expected = {'attached_emails': [], 'attached_files': [], 'flattened_attached_emails': [], 'flattened_attached_files': [], 'has_attachments': False}

        self.assertEqual(actual, expected)

    def test_flatten(self):
        email_with_nested_attachments_text = read_file_to_string("./payloads/email_with_nested_attachments_python_object.txt")
        email_with_nested_attachments = eval(email_with_nested_attachments_text)

        icon_email = IconEmail(**email_with_nested_attachments)

        # This is a LOT of work to make a complex mocked object
        # At this point, before flattening...all sub emails and files should be
        # IconFiles and IconEmails respectively...thus this mass of garbage
        for i, attached_file in enumerate(icon_email.attached_files):
            new_file = IconFile(**attached_file)
            icon_email.attached_files[i] = new_file

        for i, attached_email in enumerate(icon_email.attached_emails):
            new_email = IconEmail(**attached_email)
            icon_email.attached_emails[i] = new_email
            if len(icon_email.attached_emails[i].attached_files) > 0:
                icon_email.attached_emails[i].attached_files[0] = IconFile(**icon_email.attached_emails[i].attached_files[0])
            if len(icon_email.attached_emails[i].attached_emails) > 0:
                for j, sub_attached_email in enumerate(icon_email.attached_emails[i].attached_emails):
                    new_sub_email = IconEmail(**sub_attached_email)
                    icon_email.attached_emails[i].attached_emails[j] = new_sub_email
                    if len(icon_email.attached_emails[i].attached_emails[j].attached_files) > 0:
                        icon_email.attached_emails[i].attached_emails[j].attached_files[0] = IconFile(**icon_email.attached_emails[i].attached_emails[j].attached_files[0])

        icon_email.flatten()
        self.assertEqual(icon_email.has_attachments, True)

        self.assertEqual(len(icon_email.attached_emails), 2)
        self.assertEqual(len(icon_email.attached_files), 1)

        self.assertEqual(icon_email.attached_files[0].file_name, 'olleg.png')

        self.assertEqual(icon_email.attached_emails[0].subject, 'Level 2 subject')
        self.assertEqual(icon_email.attached_emails[1].subject, 'Pic attached')
        self.assertEqual(icon_email.subject, 'level 3')

        self.assertEqual(len(icon_email.flattened_attached_emails), 2)
        attached_email0 = icon_email.flattened_attached_emails[0]
        attached_email1 = icon_email.flattened_attached_emails[1]

        self.assertEqual(attached_email0.subject, 'Level 2 subject')
        self.assertEqual(attached_email1.subject, 'Pic attached')

        attached_file0 = icon_email.flattened_attached_files[0]
        self.assertEqual(attached_file0.file_name, 'olleg.png')

    def test_flatten_real_data(self):
        email_with_nested_attachments_text = read_file_to_string("./payloads/2 level deep email attached.eml")
        email_parser = EmailParser()
        icon_email = email_parser.make_email_from_raw(email_with_nested_attachments_text, "fake_account")

        icon_email.flatten()
        self.assertEqual(icon_email.subject, 'Fw: 2 level deep email attached')
        self.assertEqual(len(icon_email.flattened_attached_emails), 2)
        self.assertEqual(len(icon_email.flattened_attached_files), 0)

        attached_email0 = icon_email.flattened_attached_emails[0]
        attached_email1 = icon_email.flattened_attached_emails[1]

        self.assertEqual(attached_email0.subject, 'Attachment')
        self.assertEqual(attached_email1.subject, 'Test Message Attachment Subject')

    def test_convert_message_to_icon_email_with_email_attachemnt(self):
        fake_email_attachment = IconEmail()
        fake_email_attachment.subject = "FIND ME"
        fake_file_attachment = IconFile()
        fake_file_attachment.file_name = "FIND ME.txt"
        message = {'@odata.etag': 'W/"CQAAABYAAAC8UQDN7ObVSLWQuxHJ/dDTAAE33TEP"', 'id': 'AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAAAAEMAAC8UQDN7ObVSLWQuxHJ-dDTAAE4BRqiAAA=', 'createdDateTime': '2019-08-12T14:02:20Z', 'lastModifiedDateTime': '2019-08-12T14:02:21Z', 'changeKey': 'CQAAABYAAAC8UQDN7ObVSLWQuxHJ/dDTAAE33TEP', 'categories': [], 'receivedDateTime': '2019-08-12T14:02:20Z', 'sentDateTime': '2019-08-12T14:02:10Z', 'hasAttachments': True, 'internetMessageId': '<cdd3c06a-b912-5a77-6692-1a6f99b64e6f@rapid7.com>', 'subject': 'Jared Test', 'bodyPreview': '-------- Forwarded Message --------\r\nSubject:        Fwd: Fwd: Jared Test\r\nDate:   Mon, 12 Aug 2019 08:56:22 -0500\r\nFrom:   Joey McAdams <jmcadams@rapid7.com>\r\nTo:     Jon Schipp <jschipp@komanddev.onmicrosoft.com>\r\n\r\n\r\n\r\n\r\n\r\n\r\n-------- Forwarded Me', 'importance': 'normal', 'parentFolderId': 'AQMkADI3Mzc1ZTg3LTIzYWEALTQzZjYtYWQ0OS0wYjIwM2MwN2U4YWMALgAAAzEO_s9zyrpKoYtMn2IH9IYBALxRAM3s5tVItZC7Ecn90NMAAAIBDAAAAA==', 'conversationId': 'AAQkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwAQAKKyBRUie_lMt0icG_c0I6c=', 'isDeliveryReceiptRequested': None, 'isReadReceiptRequested': False, 'isRead': False, 'isDraft': False, 'webLink': 'https://outlook.office365.com/owa/?ItemID=AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB%2FSGBwC8UQDN7ObVSLWQuxHJ%2FdDTAAAAAAEMAAC8UQDN7ObVSLWQuxHJ%2FdDTAAE4BRqiAAA%3D&exvsurl=1&viewmodel=ReadMessageItem', 'inferenceClassification': 'focused', 'body': {'contentType': 'html', 'content': '<html>\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\r\n<meta content="text/html; charset=utf-8">\r\n</head>\r\n<body bgcolor="#FFFFFF">\r\n<p>&nbsp;&nbsp;&nbsp; <br>\r\n</p>\r\n<div class="moz-forward-container"><br>\r\n<br>\r\n-------- Forwarded Message --------\r\n<table class="moz-email-headers-table" cellspacing="0" cellpadding="0" border="0">\r\n<tbody>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">Subject: </th>\r\n<td>Fwd: Fwd: Jared Test</td>\r\n</tr>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">Date: </th>\r\n<td>Mon, 12 Aug 2019 08:56:22 -0500</td>\r\n</tr>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">From: </th>\r\n<td>Joey McAdams <a class="moz-txt-link-rfc2396E" href="mailto:jmcadams@rapid7.com">\r\n&lt;jmcadams@rapid7.com&gt;</a></td>\r\n</tr>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">To: </th>\r\n<td>Jon Schipp <a class="moz-txt-link-rfc2396E" href="mailto:jschipp@komanddev.onmicrosoft.com">\r\n&lt;jschipp@komanddev.onmicrosoft.com&gt;</a></td>\r\n</tr>\r\n</tbody>\r\n</table>\r\n<br>\r\n<br>\r\n<p>&nbsp;&nbsp; <br>\r\n</p>\r\n<div class="moz-forward-container"><br>\r\n<br>\r\n-------- Forwarded Message --------\r\n<table class="moz-email-headers-table" cellspacing="0" cellpadding="0" border="0">\r\n<tbody>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">Subject: </th>\r\n<td>Fwd: Jared Test</td>\r\n</tr>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">Date: </th>\r\n<td>Mon, 12 Aug 2019 08:49:25 -0500</td>\r\n</tr>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">From: </th>\r\n<td>Joey McAdams <a class="moz-txt-link-rfc2396E" href="mailto:jmcadams@rapid7.com">\r\n&lt;jmcadams@rapid7.com&gt;</a></td>\r\n</tr>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">To: </th>\r\n<td>Jon Schipp <a class="moz-txt-link-rfc2396E" href="mailto:jschipp@komanddev.onmicrosoft.com">\r\n&lt;jschipp@komanddev.onmicrosoft.com&gt;</a></td>\r\n</tr>\r\n</tbody>\r\n</table>\r\n<br>\r\n<br>\r\n<p><br>\r\n</p>\r\n<div class="moz-forward-container"><br>\r\n<br>\r\n-------- Forwarded Message --------\r\n<table class="moz-email-headers-table" cellspacing="0" cellpadding="0" border="0">\r\n<tbody>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">Subject: </th>\r\n<td>Jared Test</td>\r\n</tr>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">Date: </th>\r\n<td>Mon, 12 Aug 2019 08:39:40 -0500</td>\r\n</tr>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">From: </th>\r\n<td>Joey McAdams <a class="moz-txt-link-rfc2396E" href="mailto:jmcadams@rapid7.com">\r\n&lt;jmcadams@rapid7.com&gt;</a></td>\r\n</tr>\r\n<tr>\r\n<th valign="BASELINE" nowrap="nowrap" align="RIGHT">To: </th>\r\n<td>Jon Schipp <a class="moz-txt-link-rfc2396E" href="mailto:jschipp@komanddev.onmicrosoft.com">\r\n&lt;jschipp@komanddev.onmicrosoft.com&gt;</a></td>\r\n</tr>\r\n</tbody>\r\n</table>\r\n<br>\r\n<br>\r\n<br>\r\nSome body text goes here.<br>\r\n<br>\r\n<br>\r\n</div>\r\n</div>\r\n</div>\r\n<br>\r\n<span style="color:rgb(17,17,17); font-family:jaf-bernina-sans,tahoma,geneva,sans-serif; font-size:16px; background-color:rgb(255,255,255)">NOTICE OF CONFIDENTIALITY: At Rapid7, the privacy of our customers, partners, and employees is paramount. If you received\r\n this email in error, please notify the sender and delete it from your inbox right away. Learn how Rapid7 handles privacy at&nbsp;</span><a href="https://www.rapid7.com/privacy-policy/" target="_blank" style="color:rgb(0,103,179); font-family:jaf-bernina-sans,tahoma,geneva,sans-serif; font-size:16px; background-color:rgb(255,255,255)">rapid7.com/privacy-policy</a><span style="color:rgb(17,17,17); font-family:jaf-bernina-sans,tahoma,geneva,sans-serif; font-size:16px; background-color:rgb(255,255,255)">.\r\n To opt-out of Rapid7 marketing emails, please&nbsp;</span><a href="https://information.rapid7.com/manage-subscription.html" target="_blank" style="color:rgb(0,103,179); font-family:jaf-bernina-sans,tahoma,geneva,sans-serif; font-size:16px; background-color:rgb(255,255,255)">click\r\n here</a><span style="color:rgb(17,17,17); font-family:jaf-bernina-sans,tahoma,geneva,sans-serif; font-size:16px; background-color:rgb(255,255,255)">&nbsp;or email&nbsp;</span><a href="mailto:mailto:privacy@rapid7.com" target="_blank" style="color:rgb(0,103,179); font-family:jaf-bernina-sans,tahoma,geneva,sans-serif; font-size:16px; background-color:rgb(255,255,255)">privacy@rapid7.com</a><span style="color:rgb(17,17,17); font-family:jaf-bernina-sans,tahoma,geneva,sans-serif; font-size:16px; background-color:rgb(255,255,255)">.</span>\r\n</body>\r\n</html>\r\n'}, 'sender': {'emailAddress': {'name': 'Joey McAdams', 'address': 'joey_mcadams@rapid7.com'}}, 'from': {'emailAddress': {'name': 'Joey McAdams', 'address': 'joey_mcadams@rapid7.com'}}, 'toRecipients': [{'emailAddress': {'name': 'Jon Schipp', 'address': 'jschipp@komanddev.onmicrosoft.com'}}], 'ccRecipients': [], 'bccRecipients': [], 'replyTo': [], 'flag': {'flagStatus': 'notFlagged'}, 'message_attachments': [fake_email_attachment], 'file_attachments': [fake_file_attachment]}
        icon_email = IconEmail()

        actual = icon_email.convert_message_to_icon_email(self.logger, message, "FAKE_ID")
        self.assertEqual(len(actual.attached_emails), 1)
        self.assertEqual(actual.attached_emails[0].subject, "FIND ME")
        self.assertEqual(actual.has_attachments, True)
        self.assertEqual(actual.attached_files[0].file_name, "FIND ME.txt")

    def test_json_handler(self):
        icon_email = IconEmail()
        actual = icon_email.json_handler(b'some_bytes')
        self.assertEqual(actual, 'c29tZV9ieXRlcw==')

        actual = icon_email.json_handler(IconFile())
        self.assertEqual(actual, {'file_name': '', 'content': '', 'content_type': ''})

        bad_test_object = dict(int_list=[1, 2, 3])

        with self.assertRaises(PluginException):
            icon_email.json_handler(bad_test_object)

        class GarbageObject:
            def __init__(self, object):
                self.data = object

        object_with_datetime = GarbageObject(datetime.datetime.now())

        actual = icon_email.json_handler(object_with_datetime)
        self.assertIsNotNone(actual)  # It's very difficult to test an actual value with time

    def test_hash(self):
        email_with_nested_attachments_text = read_file_to_string("./payloads/hash_crash.eml")
        email_parser = EmailParser()
        icon_email = email_parser.make_email_from_raw(email_with_nested_attachments_text, "fake_account")

        actual = icon_email.__hash__()

        print(type(actual))
        self.assertIsInstance(actual, int)
