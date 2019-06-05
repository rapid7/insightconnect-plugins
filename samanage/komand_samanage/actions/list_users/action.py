import komand
from .schema import ListUsersInput, ListUsersOutput
# Custom imports below


class ListUsers(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_users',
                description='List all users',
                input=ListUsersInput(),
                output=ListUsersOutput())

    def run(self, params={}):
        return {'users': self.connection.api.list_users()}

    def test(self):
        return {
            'users': [{
                'id': 4245115,
                'name': 'Anon',
                'disabled': False,
                'email': '123@service.hmail.eu',
                'created_at': '2018-11-22T08:13:00.000-05:00',
                'role': {
                    'id': 461180,
                    'name': 'Requester',
                    'description': 'Requester role to view and submit service request.',
                    'portal': True,
                    'show_my_tasks': False
                },
                'salt': '04f20390ecf0c97571167c6c3350782663b6a7e0',
                'group_ids': [4492327],
                'custom_fields_values': [],
                'avatar': {
                    'type': 'initials',
                    'color': '#dfcd00',
                    'initials': 'AN'
                },
                'mfa_enabled': False
            }, {
                'id': 4244043,
                'name': 'Tom',
                'disabled': False,
                'title': 'Panic',
                'email': '20180913dp@gmail.com',
                'created_at': '2018-11-21T12:28:31.000-05:00',
                'phone': '12345678',
                'mobile_phone': '87654321',
                'department': {
                    'id': 133361,
                    'name': 'Information Technology',
                    'default_assignee_id': 4485265
                },
                'role': {
                    'id': 461179,
                    'name': 'Service Agent User',
                    'description': 'Almost like an administrator but no access to setup.',
                    'portal': False,
                    'show_my_tasks': False
                },
                'salt': 'b3e360e65de5b592ce1ff92e1d90acedbaddbcf7',
                'group_ids': [4491226],
                'custom_fields_values': [],
                'avatar': {
                    'type': 'initials',
                    'color': '#dfcd00',
                    'initials': 'TO'
                },
                'mfa_enabled': False,
                'reports_to': {
                    'id': 4485266,
                    'name': 'Helpdesk',
                    'disabled': False,
                    'is_user': False,
                    'reports_to': {
                        'id': -1,
                        'href': 'https://api.samanage.com/groups/-1.json'
                    },
                    'avatar': {
                        'type': 'group',
                        'color': '#0bc46f'
                    }
                },
                'site': {
                    'id': 96691,
                    'name': 'Headquarters',
                    'location': 'Main Office'
                }
            }, {
                'id': 4238379,
                'name': 'WW WW',
                'disabled': False,
                'email': 'wwww@service.hmail.eu',
                'created_at': '2018-11-20T05:29:00.000-05:00',
                'last_login': '2018-11-21T17:20:46.000-05:00',
                'phone': '+37254312367',
                'role': {
                    'id': 461178,
                    'name': 'Administrator',
                    'description': 'This is the all powerful administrator user!',
                    'portal': False,
                    'show_my_tasks': False
                },
                'salt': '7e2c35f51cc6ccdf727f7e48bc42403adbf6534d',
                'group_ids': [
                    4485265,
                    4485266
                ],
                'custom_fields_values': [],
                'avatar': {
                    'type': 'initials',
                    'color': '#dfcd00',
                    'initials': 'WW'
                },
                'mfa_enabled': False
            }]
        }
