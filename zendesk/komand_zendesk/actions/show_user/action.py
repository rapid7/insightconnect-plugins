import komand
from .schema import ShowUserInput, ShowUserOutput
# Custom imports below
import json

class ShowUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='show_user',
                description='Retrieve user information',
                input=ShowUserInput(),
                output=ShowUserOutput())

    def run(self, params={}):
        user = self.connection.client.users(id=params.get('user_id'))
        user_obj = {
            'active': user.active, 
            'alias': user.alias,
            'chat_only': user.chat_only, 
            'created_at': user.created_at, 
            'custom_role_id': user.custom_role_id, 
            'details': user.details, 
            'email': user.email, 
            'external_id': user.external_id, 
            'id': user.id, 
            'last_login_at': user.last_login_at, 
            'locale': user.locale, 
            'locale_id': user.locale_id, 
            'moderator': user.moderator, 
            'name': user.name, 
            'notes': user.notes, 
            'only_private_comments': user.only_private_comments, 
            'organization_id': user.organization_id, 
            'phone': user.phone, 
            'photo': user.photo, 
            'restricted_agent': user.restricted_agent, 
            'role': user.role, 
            'shared': user.shared, 
            'shared_agent': user.shared_agent, 
            'signature': user.signature, 
            'suspended': user.suspended, 
            'tags': user.tags, 
            'ticket_restriction': user.ticket_restriction, 
            'time_zone': user.time_zone, 
            'two_factor_auth_enabled': user.two_factor_auth_enabled, 
            'updated_at': user.updated_at, 
            'url': user.url, 
            'verified': user.verified
        }
        return user_obj

    def test(self):
        try:
          test = self.connection.client.users.me().email
          return { 'success': test }
        except:
          raise
