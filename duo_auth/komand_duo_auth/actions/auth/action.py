import komand
import urllib

from komand.exceptions import PluginException
from .schema import AuthInput, AuthOutput, Input


class Auth(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='auth',
            description='Perform second-factor authentication',
            input=AuthInput(),
            output=AuthOutput())

    def run(self, params={}):
        """Run action"""
        opts = params.get(Input.OPTIONS) or {}
        push_info = opts.get('pushinfo')

        if push_info:
            push_info = urllib.parse.urlencode(push_info)

        user_id = None
        if params.get(Input.USER_ID):
            user_id = params.get(Input.USER_ID)

        username = None
        if params.get(Input.USERNAME):
            username = params.get(Input.USERNAME)

        if (username and user_id) or (user_id is None and username is None):
            raise PluginException(cause="Wrong input", assistance="Only user_id or username should be used. Not both.")

        response = self.connection.auth_api.auth(
            factor=params[Input.FACTOR],
            username=username,
            user_id=user_id,
            ipaddr=params.get(Input.IPADDR),
            async_txn=params.get(Input.ASYNC),
            type=opts.get('type'),
            display_username=username,
            pushinfo=push_info,
            device=params.get(Input.DEVICE),
            passcode=opts.get('passcode')
        )
        return response

    def test(self):
        pass
