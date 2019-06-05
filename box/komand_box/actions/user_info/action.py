import komand
from .schema import UserInfoInput, UserInfoOutput
# Custom imports below

class UserInfo(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='user_info',
                description='Retrieve user information',
                input=UserInfoInput(),
                output=UserInfoOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        user = client.user(user_id=params.get('user_id')).get()
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

    def test(self):
        try:
          client = self.connection.box_connection
          return {'status': True }
        except:
          raise
