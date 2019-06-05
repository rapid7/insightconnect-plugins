import komand
from .schema import CreateUserInput, CreateUserOutput
# Custom imports below


class CreateUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_user',
                description='Create a new user',
                input=CreateUserInput(),
                output=CreateUserOutput())

    def run(self, params={}):
        email = params.get('email')
        name = params.get('name')
        phone = params.get('phone')
        mobile_phone = params.get('mobile_phone')
        role = params.get('role')
        department = params.get('department')

        user = self.connection.api.create_user(
            email, name, phone, mobile_phone, role, department
        )

        return {'user': user}

    def test(self):
        return {
            'user': {
                'id': 4245316,
                'name': 'John Snow',
                'disabled': False,
                'email': 'abc@example.com',
                'created_at': '2018-11-22T15:18:53.337-05:00',
                'phone': '123456',
                'mobile_phone': '0012345',
                'department': {
                    'id': 133365,
                    'name': 'Marketing'
                },
                'role': {
                    'id': 461182,
                    'name': 'Read Only',
                    'portal': False,
                    'show_my_tasks': False
                },
                'salt': 'fc136bca03c6361bf1e564e18d70cc421b1fc582',
                'group_ids': [4492546],
                'custom_fields_values': [],
                'avatar': {
                    'type': 'initials',
                    'color': '#fa7911',
                    'initials': 'JS'
                },
                'mfa_enabled': False
            }
        }
