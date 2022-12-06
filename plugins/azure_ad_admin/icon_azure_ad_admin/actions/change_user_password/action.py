import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ChangeUserPasswordInput, ChangeUserPasswordOutput, Input, Output, Component
from ...util.constans import Endpoint


class ChangeUserPassword(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="change_user_password",
            description=Component.DESCRIPTION,
            input=ChangeUserPasswordInput(),
            output=ChangeUserPasswordOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)
        user_uri = Endpoint.USER_ID
        endpoint = user_uri.format(self.connection.tenant, user_id)

        self.logger.info(f"Enabling user: {user_id}")

        headers = self.connection.get_headers(self.connection.get_auth_token())
        data = {"passwordProfile": {"password": params.get(Input.NEW_PASSWORD)}}
        result = requests.patch(endpoint, headers=headers, json=data)

        if not result.status_code == 204:
            raise PluginException(
                cause="Change User Password failed. Check your permission.",
                assistance="Unexpected return code from server.",
                data=result.text,
            )

        return {Output.SUCCESS: True}
