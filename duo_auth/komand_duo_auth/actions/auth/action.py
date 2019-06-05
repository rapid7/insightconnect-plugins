import komand
import urllib
from .schema import AuthInput, AuthOutput


class Auth(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='auth',
                description='Perform second-factor authentication',
                input=AuthInput(),
                output=AuthOutput())

    def run(self, params={}):
        """Run action"""
        username = None
        passcode = None
        opts = params.get('options') or {}
        username = opts.get('username')
        passcode = opts.get('passcode')
        pushinfo = opts.get('pushinfo')
        if pushinfo:
            pushinfo = urllib.parse.urlencode(pushinfo)

        userid = None 
        if params.get('user_id'):
            userid = params['user_id']

        username = None 
        if params.get('username'):
            username = params['username']

        response = self.connection.auth_api.auth(
               params['factor'],
             username=username,
             user_id=userid,
             ipaddr=params.get('ipaddr'),
             async=params.get('async'),
             display_username=username,
             device=params.get('device'),
             passcode=passcode,
             pushinfo=pushinfo,
             )
        return response

    def test(self):
        """TODO: Test action"""
        return {}
