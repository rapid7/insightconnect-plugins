import komand
from komand.exceptions import PluginException

from .schema import UserInfoFromLoginInput, UserInfoFromLoginOutput, Input, Component
# Custom imports below


class UserInfoFromLogin(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='user_info_from_login',
                description=Component.DESCRIPTION,
                input=UserInfoFromLoginInput(),
                output=UserInfoFromLoginOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        user_login = params.get(Input.LOGIN)

        self.logger.info(f"Looking for user with login: {user_login}")
        user_list = client.users(filter_term=user_login)

        if not user_list:
            raise PluginException(cause="User login not found.",
                                  assistance=f"The user with login {user_login} can not be found.")

        user = user_list[0]
        info = {
                "address": user.address,
                "avatar_url": user.avatar_url,
                "id": user.id,
                "job_title": user.job_title,
                "login": user.login,
                "name": user.name,
                "phone": user.phone,
                "space_amount": user.space_amount,
                "space_used": user.space_used,
                "timezone": user.timezone
        }

        return info
