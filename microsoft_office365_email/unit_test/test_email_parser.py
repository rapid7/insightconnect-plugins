from icon_microsoft_office365_email.util.email_parser import EmailParser, LogAction
from unittest import TestCase
import logging
import email

TEST_MAILBOX_ID = "somedude@hotmail.com"

GET_RAW_ATTACHMENT_PAYLOAD = "./payloads/four_deep_with_pic.txt"
GET_RAW_ATTACHMENT_PAYLOAD2 = "./payloads/get_raw_attachment_test.txt"
GET_RAW_ATTACHMENT_PAYLOAD3 = "./payloads/3_deep_with_text_attachment.txt"
GET_RAW_ATTACHMENT_PAYLOAD4 = "./payloads/basic_email_attachment.txt"
GET_DOUBLE_ATTACHED_WITH_IMAGES = "./payloads/double_attached_with_images.txt"
GET_PAYLOAD_FROM_JARED = "./payloads/payload_from_jared.txt"
GET_BASIC_EMAIL = "./payloads/basic_email.txt"
GET_EML_WITH_EML_ATTACHED = "./payloads/lots_of_eml_attached.eml"
GET_ENCODED_EML = "./payloads/encoded_ms_eml.txt"
GET_UNICODE_EML = "./payloads/Grüße_von_Stefan_Appel.eml"
GET_GOOGLE_SURVEY = "./payloads/API Security Survey (please take this important survey) .eml"

GET_BAD_EMAIL1 = "./payloads/get_raw_attachment_test_no_content_type.txt"


# Get a real payload from file
def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


class test_email_parser(TestCase):
    def setUp(self) -> None:
        self.log = logging.getLogger("stuff")

    # This is dumb, I just needed it for coverage
    def test_LogAction(self):
        log = LogAction()
        log.run({})
        log.test({})

    def test_parse_from_raw(self):
        raw_email = read_file_to_string(GET_RAW_ATTACHMENT_PAYLOAD)
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        self.assertEqual(email.account, TEST_MAILBOX_ID)
        self.assertEqual(email.subject, "level 3")
        self.assertEqual(len(email.attached_emails), 2)
        self.assertEqual(len(email.attached_files), 1)

        self.assertEqual(email.date_received, "Thu, 8 Aug 2019 17:29:14 +0000")
        self.assertEqual(len(email.headers), 73)
        self.assertEqual(email.is_read, False)
        self.assertEqual(email.recipients, ["chakan2@hotmail.com"])
        self.assertEqual(email.sender, "chakan2@hotmail.com")
        self.assertTrue("level 3" in email.body)

        attached_email = email.attached_emails[0]
        self.assertEqual(attached_email.subject, 'Level 2 subject')
        self.assertEqual(attached_email.sender, 'chakan2@hotmail.com')
        self.assertEqual(attached_email.recipients, ['chakan2@hotmail.com'])
        self.assertTrue("Level 2 body" in attached_email.body)

        attached_email_of_attached_email = attached_email.attached_emails[0]
        self.assertEqual(attached_email_of_attached_email.subject, "Pic attached")

        attached_file = email.attached_files[0]
        self.assertEqual(attached_file.content[:5], 'iVBOR')
        self.assertEqual(attached_file.content_type, 'image/png')
        self.assertEqual(attached_file.file_name, 'olleg.png')

    def test_parse_from_raw2(self):
        raw_email = read_file_to_string(GET_RAW_ATTACHMENT_PAYLOAD2)
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        self.assertEqual(email.account, TEST_MAILBOX_ID)
        self.assertEqual(email.subject, "Attachment")
        self.assertEqual(len(email.attached_emails), 1)
        self.assertEqual(len(email.attached_files), 0)

        self.assertTrue("Attachment Body" in email.body)
        attached_email = email.attached_emails[0]
        self.assertTrue("Test Message Attachment Body" in attached_email.body)

        self.assertEqual(email.date_received, "Tue, 6 Aug 2019 19:19:40 +0000")
        self.assertEqual(len(email.headers), 75)
        self.assertEqual(email.is_read, False)
        self.assertEqual(email.recipients, ["chakan2@hotmail.com"])
        self.assertEqual(email.sender, "chakan2@hotmail.com")

    def test_parse_from_raw3(self):
        raw_email = read_file_to_string(GET_RAW_ATTACHMENT_PAYLOAD3)
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        self.assertEqual(email.account, TEST_MAILBOX_ID)
        self.assertEqual(email.subject, "Text Attachment")
        self.assertEqual(len(email.attached_emails), 0)
        self.assertEqual(len(email.attached_files), 1)

        self.assertTrue("Here is a text attachment" in email.body)
        self.assertEqual(email.date_received, 'Thu, 8 Aug 2019 20:16:38 +0000')
        self.assertEqual(len(email.headers), 76)
        self.assertEqual(email.is_read, False)
        self.assertEqual(email.recipients, ["chakan2@hotmail.com"])
        self.assertEqual(email.sender, "chakan2@hotmail.com")

        attachment = email.attached_files[0]
        self.assertEqual(attachment.content_type, "text/plain")
        expected_content = 'VGhpcyBpcyBhIHRlc3QgYXR0YWNobWVudA0KDQpJdCBoYXMgc29tZSB0ZXh0IGluIGl0LiANCg0KYWFkcm9pZC5uZXQNCg=='
        self.assertEqual(attachment.content, expected_content)
        self.assertEqual(attachment.file_name, 'test_attachment.txt')

    def test_parse_from_raw4(self):
        raw_email = read_file_to_string(GET_RAW_ATTACHMENT_PAYLOAD4)
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        self.assertEqual(email.account, TEST_MAILBOX_ID)
        self.assertEqual(email.subject, "Basic Message Attachment")
        self.assertEqual(len(email.attached_emails), 0)
        self.assertEqual(len(email.attached_files), 0)

        expected_body = """<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<style type="text/css" style="display:none;"> P {margin-top:0;margin-bottom:0;} </style>
</head>
<body dir="ltr">
<div style="font-family: Calibri, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0);">
Nothing here, just this text</div>
</body>
</html>
"""
        self.assertEqual(email.body, expected_body)
        self.assertEqual(email.date_received, 'Thu, 8 Aug 2019 21:19:37 +0000')
        self.assertEqual(len(email.headers), 76)
        self.assertEqual(email.is_read, False)
        self.assertEqual(email.recipients, ["chakan2@hotmail.com"])
        self.assertEqual(email.sender, "chakan2@hotmail.com")

    def test_parse_from_raw_jared(self):
        raw_email = read_file_to_string(GET_PAYLOAD_FROM_JARED)
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        self.assertEqual(email.account, TEST_MAILBOX_ID)
        self.assertEqual(email.subject, "FW: [POTENTIAL PHISH] MESINC")
        self.assertEqual(len(email.attached_emails), 2)
        self.assertEqual(len(email.attached_files), 4)

        self.assertEqual(email.date_received, 'Thu, 1 Aug 2019 10:36:33 +0000')
        self.assertEqual(len(email.headers), 69)
        self.assertEqual(email.is_read, False)
        self.assertEqual(email.recipients, ['d444e537.acuitybrandsinc.onmicrosoft.com@amer.teams.ms', 'd444e537.acuitybrandsinc.onmicrosoft.com@amer.teams.ms'])
        self.assertEqual(email.sender, 'incidentresponse@acuitybrands.com')

    def test_parse_google_link_garbled(self):
        raw_email = read_file_to_string(GET_GOOGLE_SURVEY)
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        self.assertTrue('<a href="http://aadroid.net/" rel="nofollow" target="_blank">' in email.body)

    def test_parse_raw_with_unicode(self):
        raw_email = read_file_to_string(GET_UNICODE_EML)
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        self.assertEqual(email.subject, "Grüße von Stefan Appel")

    # This is likely an invalid test...the python
    # email will ALWAYS have a content-type
    # If it doesn't, we're not going to return anything meaningful.

    # def test_parse_from_raw_missing_content_type(self):
    #     raw_email = read_file_to_string(GET_BAD_EMAIL1)
    #     email_parser = EmailParser()
    #     email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)
    #
    #     self.assertEqual(email.account, TEST_MAILBOX_ID)
    #     self.assertEqual(email.subject, "Attachment")
    #     self.assertEqual(len(email.attached_emails), 1)
    #     self.assertEqual(len(email.attached_files), 0)
    #
    #     # This is ok, we removed the content type so stuff gets weird
    #     expected_body = """"""
    #
    #     self.assertEqual(email.body, expected_body)
    #     self.assertEqual(email.date_received, "Tue, 6 Aug 2019 19:19:40 +0000")
    #     self.assertEqual(len(email.headers), 75)
    #     self.assertEqual(email.is_read, False)
    #     self.assertEqual(email.recipients, ["chakan2@hotmail.com"])
    #     self.assertEqual(email.sender, "chakan2@hotmail.com")

    def test_parse_double_attached_with_images(self):
        raw_email = read_file_to_string(GET_DOUBLE_ATTACHED_WITH_IMAGES)
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        self.assertEqual(email.account, TEST_MAILBOX_ID)
        self.assertEqual(email.subject, 'Fw: Joey Test')
        self.assertEqual(len(email.attached_emails), 2)
        self.assertEqual(len(email.attached_files), 2)

        self.assertEqual(email.date_received, 'Tue, 13 Aug 2019 20:05:12 +0000')
        self.assertEqual(len(email.headers), 53)
        self.assertEqual(email.is_read, False)
        self.assertEqual(email.recipients, ['joey_mcadams@rapid7.com'])
        self.assertEqual(email.sender, 'jschipp@komanddev.onmicrosoft.com')

        self.assertEqual(len(email.attached_emails), 2)
        self.assertEqual(len(email.attached_files), 2)

        email1 = email.attached_emails[0]
        email2 = email.attached_emails[1]

        self.assertTrue(email1.subject, "Pic and eml attached")
        self.assertTrue(email2.subject, "Test Email")

    def test_single_recipient(self):
        email_parser = EmailParser()
        msg = {
            "To": "bob@hotmail.com"
        }
        rcpt = email_parser.get_recipients(self.log, msg)
        self.assertEqual(rcpt, ["bob@hotmail.com"])

    def test_no_recipients(self):
        email_parser = EmailParser()
        msg = {
            "To": ""
        }
        rcpt = email_parser.get_recipients(self.log, msg)
        self.assertEqual(rcpt, [])

    def test_multiple_recipients(self):
        email_parser = EmailParser()
        msg = {
            "To": "<someguy@microsoft.com> bob smith, <someotherguy@gmail.com> robert the bruce"
        }
        rcpt = email_parser.get_recipients(self.log, msg)
        self.assertEqual(rcpt, ["someguy@microsoft.com", "someotherguy@gmail.com"])

    def test_multiple_recipients_delivered_to(self):
        email_parser = EmailParser()
        msg = {
            "Delivered-To": "<someguy@microsoft.com> bob smith, <someotherguy@gmail.com> robert the bruce"
        }
        rcpt = email_parser.get_recipients(self.log, msg)
        self.assertEqual(rcpt, ["someguy@microsoft.com", "someotherguy@gmail.com"])

    def test_recipients_not_available(self):
        email_parser = EmailParser()
        msg = {}
        rcpt = email_parser.get_recipients(self.log, msg)
        self.assertEqual(rcpt, [])

    def test_decode_body(self):
        basic_email_text = read_file_to_string(GET_BASIC_EMAIL)
        test_email = email.message_from_string(basic_email_text)

        email_parser = EmailParser()
        actual_body = email_parser.decode_body(test_email, self.log)

        self.assertEqual(actual_body, "Test\n")

    def test_decode_body_unicode(self):
        basic_email_text = read_file_to_string(GET_BASIC_EMAIL)
        test_email = email.message_from_string(basic_email_text)
        test_email._payload = "u\"é"

        email_parser = EmailParser()
        actual_body = email_parser.decode_body(test_email, self.log)

        self.assertEqual(actual_body, 'u"')

    def test_decode_multipart_body_unicode(self):
        raw_text = read_file_to_string(GET_DOUBLE_ATTACHED_WITH_IMAGES)
        test_email = email.message_from_string(raw_text)

        email_parser = EmailParser()
        test_email._payload[0]._payload[0]._payload = test_email._payload[0]._payload[0]._payload.replace("chakan2@hotmail.com", "u\"é")
        actual_body = email_parser.decode_body(test_email._payload[0]._payload[0], self.log)

        expected_body = """________________________________From: Jon Schipp <jschipp@komanddev.onmicrosoft.com>Sent: Tuesday, August 13, 2019 3:56 PMTo: Jon Schipp <jschipp@komanddev.onmicrosoft.com>Subject: Joey Test________________________________From: Joey McAdams <u">Sent: Tuesday, August 13, 2019 10:55 AMTo: Jon Schipp <jschipp@komanddev.onmicrosoft.com>Subject: Fw: Short Test Email________________________________From: Joey McAdamsSent: Tuesday, August 13, 2019 9:30 AMTo: jschipp@komanddev.onmicrosoft.com <jschipp@komanddev.onmicrosoft.com>Subject: Short Test Email"""
        self.assertEqual(expected_body, actual_body)

    def test_decode_multipart_body_html_unicode(self):
        raw_text = read_file_to_string(GET_DOUBLE_ATTACHED_WITH_IMAGES)
        test_email = email.message_from_string(raw_text)

        email_parser = EmailParser()
        test_email._payload[0]._payload[1]._payload = "<html>FOO u\"é BAR</html>"
        actual_body = email_parser.decode_body(test_email._payload[0], self.log)

        expected_body = '<html>FOO u"é BAR</html>'
        self.assertEqual(expected_body, actual_body)

    def test_parse_attached_eml(self):
        raw_email = read_file_to_string(GET_EML_WITH_EML_ATTACHED)
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        self.assertEqual(len(email.attached_emails), 6)
        self.assertEqual(len(email.attached_files), 0)

    def test_decode_quoted_printable(self):
        raw_email = read_file_to_string("./payloads/quoted_printable.eml")
        email_parser = EmailParser()
        email = email_parser.make_email_from_raw(raw_email, TEST_MAILBOX_ID)

        expected = '<a href="http://aadroid.net" title="http://protect-us.mimecast.com/s/414KCXDXZofXVRNRZT6ai-n?domain=aadroid.net">http://aadroid.net</a><o:p></o:p></p>'
        self.assertTrue(expected in email.body)
