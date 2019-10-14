import komand
from .schema import GetEmailFromUserInput, GetEmailFromUserOutput, Input, Output, Component
from komand.exceptions import PluginException
from icon_microsoft_office365_email.util.icon_email import IconEmail
# Custom imports below
import urllib.parse
import requests


class GetEmailFromUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_email_from_user',
                description=Component.DESCRIPTION,
                input=GetEmailFromUserInput(),
                output=GetEmailFromUserOutput())

        self.MESSAGES_FROM_USER_ENDPOINT = "https://graph.microsoft.com/v1.0/{tenant}/users/{mailbox_id}/messages?{kql}"

    def run(self, params={}):
        mailbox_id = params.get(Input.MAILBOX_ID)
        from_contains = params.get(Input.FROM_CONTAINS)
        subject_contains = params.get(Input.SUBJECT_CONTAINS)
        body_contains = params.get(Input.BODY_CONTAINS)
        max_number_to_return = params.get(Input.MAX_NUMBER_TO_RETURN)

        self.logger.info("User: " + mailbox_id)
        self.logger.info("From Contains: " + str(from_contains))
        self.logger.info("Subject Contains: " + str(subject_contains))
        self.logger.info("Body Contains: " + str(body_contains))

        kql = self.make_kql_for_request(from_contains, subject_contains, body_contains, max_number_to_return)

        microsoft_messages = self.get_messages_from_user(mailbox_id, kql)

        icon_emails = []
        icon_email = IconEmail()

        for message in microsoft_messages:
            icon_email_to_return = icon_email.convert_message_to_icon_email(self.logger, message, mailbox_id)
            icon_emails.append(icon_email_to_return.make_serializable())

        return {Output.EMAIL_LIST: icon_emails}

    def make_kql_for_request(self, from_contains, subject_contains, body_contains, max_):
        if (not max_) or (max_ > 250) or (max_ < 0):
            max_ = 250

        if (not from_contains) and (not subject_contains) and (not body_contains):
            raise PluginException(cause="One query parameter is required",
                                  assistance="At least one search input is needed to Get Email From User: "
                                  "From Contains, Subject Contains, and Body Contains were all empty")

        # Quotes vs Double Quotes vs Microsoft: Be careful when quoting and not, it's tricky
        kql_string = "$search=\""

        # urllib.parse.quote_plus - Tried this and it bombs on @ symbol
        if from_contains:
            kql_string += "from:" + urllib.parse.quote_plus(from_contains) + " "
        if subject_contains:
            kql_string += "subject:\'" + urllib.parse.quote_plus(subject_contains) + "\' "
        if body_contains:
            kql_string += "body:\'" + urllib.parse.quote_plus(body_contains) + "\' "

        kql_string = kql_string.rstrip(' ')
        kql_string += "\""
        kql_string += "&$top=" + str(max_)

        self.logger.info("Generated KQL: " + kql_string)
        return kql_string

    def get_messages_from_user(self, mailbox_id, kql):
        headers = self.connection.get_headers(self.connection.get_auth_token())
        endpoint_formatted = self.MESSAGES_FROM_USER_ENDPOINT.format(tenant=self.connection.tenant,
                                                                     mailbox_id=mailbox_id,
                                                                     kql=kql)

        try:
            request = requests.get(endpoint_formatted, headers=headers)
        except Exception as e:
            raise PluginException(cause="Unable to get emails",
                                  assistance="Requests threw an exception, "
                                             "please contact support with the following information.",
                                  data=f"User ID: {mailbox_id}\nGenerated KQL: {kql}\nException:{e}")

        if request.status_code is not 200:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR,
                                  data=request.text)

        self.logger.info("Get Email From User succeed with response code: " + str(request.status_code))

        try:
            microsoft_messages = request.json()['value']
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=e)

        self.logger.info("Number of emails found: " + str(len(microsoft_messages)))

        return microsoft_messages
