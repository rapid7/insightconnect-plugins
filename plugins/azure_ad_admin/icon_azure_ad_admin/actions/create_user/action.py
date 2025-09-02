import insightconnect_plugin_runtime
from .schema import CreateUserInput, CreateUserOutput, Input, Output, Component

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import string
import random


def _pw_gen(size: int = 16, chars: [str] = string.ascii_letters + string.digits + string.punctuation) -> str:
    # pylint: disable=unused-argument
    def gen(size: int = 16) -> str:
        return "".join(random.choice(chars) for _ in range(size))  # noqa: B311

    while True:
        password = gen(size=16)

        has_lower, has_upper, has_num, has_punc = False, False, False, False
        for character in password:
            if character in string.ascii_lowercase:
                has_lower = True
                continue
            if character in string.ascii_uppercase:
                has_upper = True
                continue
            if character in string.digits:
                has_num = True
                continue
            if character in string.punctuation:
                has_punc = True
                continue

        if has_lower and has_upper and has_num and has_punc:
            return password


class CreateUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_user",
            description=Component.DESCRIPTION,
            input=CreateUserInput(),
            output=CreateUserOutput(),
        )

    def run(self, params={}):
        passwd = _pw_gen()

        self._create_user(params, passwd)

        message_to_send = self._compose_email(params, passwd)
        self.send_message(message_to_send, params.get(Input.NOTIFY_FROM))
        self.logger.info("API call complete")

        return {"success": True}

    def _create_user(self, params, passwd):
        account_enabled = params.get(Input.ACCOUNT_ENABLED, True)
        display_name = params.get(Input.DISPLAY_NAME)
        mail_nickname = params.get(Input.MAIL_NICKNAME, display_name)
        user_principal_name = params.get(Input.USER_PRINCIPAL_NAME)

        user = {
            "accountEnabled": account_enabled,
            "displayName": display_name,
            "mailNickname": mail_nickname,
            "userPrincipalName": user_principal_name,
            "passwordProfile": {"forceChangePasswordNextSignIn": True, "password": passwd},
        }

        headers = self.connection.get_headers(self.connection.get_auth_token())
        endpoint_formatted = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/"
        result = requests.post(endpoint_formatted, headers=headers, json=user, timeout=60)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=result.text) from e

        # 201 Created is the response according to MS.
        # https://docs.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0&tabs=http#response-1
        return result.status_code == 201

    def _compose_email(self, params: dict, passwd: str) -> str:
        email_from = params.get(Input.NOTIFY_FROM)
        email_to = params.get(Input.NOTIFY_RECIPIENT)
        subject = "New user created"
        message = params.get(Input.NOTIFY_EMAIL_BODY, "$password")

        message = message.replace("$password", passwd)

        message = {
            "message": {
                "subject": subject,
                "body": {"contentType": "text", "content": message},
                "from": {"emailAddress": {"address": email_from}},
                "toRecipients": [{"emailAddress": {"address": email_to}}],
                "ccRecipients": [],
                "bccRecipients": [],
            },
            "saveToSentItems": "false",
        }

        return json.dumps(message)

    def send_message(self, message: dict, mailbox_id: str) -> bool:
        headers = self.connection.get_headers(self.connection.get_auth_token())
        from_user = mailbox_id
        endpoint_formatted = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{from_user}/sendMail"
        result = requests.post(endpoint_formatted, headers=headers, data=message, timeout=60)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=result.text) from e

        # 202 Accepted is the response according to MS.
        # https://docs.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0&tabs=http
        return result.status_code == 202
