import komand
from .schema import GetCommentsInput, GetCommentsOutput
# Custom imports below


class GetComments(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_comments',
                description='Get all comments of an incident',
                input=GetCommentsInput(),
                output=GetCommentsOutput())

    def run(self, params={}):
        incident_id = params.get('incident_id')

        comments = self.connection.api.get_comments(incident_id)

        return {'comments': comments}

    def test(self):
        return {
            'comments': [{
                'id': 39639360,
                'body': '<p>Comment comment comment</p>',
                'user': {
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
                },
                'created_at': '2018-11-21T15:20:42.000-05:00',
                'updated_at': '2018-11-21T15:20:42.000-05:00',
                'attachments': [],
                'inline_attachments': [],
                'shared_attachments': [],
                'is_private': False,
                'seen_by': [4238379],
                'isTask': False,
                'task_info': {},
                'commenter_id': 31851783,
                'commenter_type': 'Incident'
            }, {
                'id': 39646936,
                'body': 'A comment',
                'user': {
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
                },
                'created_at': '2018-11-21T18:24:19.000-05:00',
                'updated_at': '2018-11-21T18:24:19.000-05:00',
                'attachments': [],
                'inline_attachments': [],
                'shared_attachments': [],
                'is_private': True,
                'seen_by': [4238379],
                'isTask': False,
                'task_info': {},
                'commenter_id': 31851783,
                'commenter_type': 'Incident'
            }]
        }
