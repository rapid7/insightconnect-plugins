import komand
from .schema import ListIncidentsInput, ListIncidentsOutput
# Custom imports below


class ListIncidents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_incidents',
                description='List all incidents',
                input=ListIncidentsInput(),
                output=ListIncidentsOutput())

    def run(self, params={}):
        incidents = self.connection.api.list_incidents()
        return {'incidents': incidents}

    def test(self):
        return {
            'incidents': [{
                'id': 31851784,
                'number': 5,
                'name': 'Set up your new service desk',
                'description': 'Service desk',
                'description_no_html': 'Service desk',
                'state': 'Assigned',
                'priority': 'Medium',
                'assignee': {
                    'group_id': 4485265,
                    'is_user': True,
                    'id': 4238379,
                    'name': 'WW WW',
                    'disabled': False,
                    'email': 'wwww@service.hmail.eu',
                    'created_at': '2018-11-20T05:29:00.000-05:00',
                    'last_login': '2018-11-20T05:33:33.000-05:00',
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
                'requester': {
                    'id': 4204395,
                    'account_id': 63582,
                    'user_id': 4238379,
                    'email': 'wwww@service.hmail.eu',
                    'name': 'WW WW',
                    'disabled': False,
                    'has_gravatar': False,
                    'avatar': {
                        'type': 'initials',
                        'color': '#dfcd00',
                        'initials': 'WW'
                    }
                },
                'created_at': '2018-11-20T05:29:03.000-05:00',
                'updated_at': '2018-11-21T10:26:43.000-05:00',
                'due_at': '2018-11-22T05:29:02.000-05:00',
                'sla_violations': [],
                'number_of_comments': 0,
                'user_saw_all_comments': True,
                'is_service_request': False,
                'created_by': {
                    'id': 4204395,
                    'account_id': 63582,
                    'user_id': 4238379,
                    'email': 'wwww@service.hmail.eu',
                    'name': 'WW WW',
                    'disabled': False,
                    'has_gravatar': False,
                    'avatar': {
                        'type': 'initials',
                        'color': '#dfcd00',
                        'initials': 'WW'
                    }
                },
                'href': 'https://api.samanage.com/incidents/31851784-set-up-your-new-service-desk.json',
                'cc': [],
                'custom_fields_values': [],
                'incidents': [],
                'changes': [],
                'tasks': [],
                'time_tracks': [],
                'solutions': [],
                'assets': [],
                'mobiles': [],
                'other_assets': [],
                'configuration_items': [],
                'purchase_orders': []
            }, {
                'id': 31851783,
                'number': 4,
                'name': 'Import contracts and software licenses',
                'description': '<p><a href=\"https://wwwwSerivice.samanage.com/contracts?import=True\">https://wwwwSerivice.samanage.com/contracts?import=True</a></p>',
                'description_no_html': 'https://wwwwSerivice.samanage.com/contracts?import=True',
                'state': 'Assigned',
                'priority': 'Medium',
                'assignee': {
                    'group_id': 4485265,
                    'is_user': True,
                    'id': 4238379,
                    'name': 'WW WW',
                    'disabled': False,
                    'email': 'wwww@service.hmail.eu',
                    'created_at': '2018-11-20T05:29:00.000-05:00',
                    'last_login': '2018-11-20T05:33:33.000-05:00',
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
                'requester': {
                    'id': 4204395,
                    'account_id': 63582,
                    'user_id': 4238379,
                    'email': 'wwww@service.hmail.eu',
                    'name': 'WW WW',
                    'disabled': False,
                    'has_gravatar': False,
                    'avatar': {
                        'type': 'initials',
                        'color': '#dfcd00',
                        'initials': 'WW'
                    }
                },
                'created_at': '2018-11-20T05:29:03.000-05:00',
                'updated_at': '2018-11-21T12:17:59.000-05:00',
                'due_at': '2018-11-21T05:29:02.000-05:00',
                'sla_violations': [],
                'number_of_comments': 0,
                'user_saw_all_comments': True,
                'is_service_request': False,
                'created_by': {
                    'id': 4204395,
                    'account_id': 63582,
                    'user_id': 4238379,
                    'email': 'wwww@service.hmail.eu',
                    'name': 'WW WW',
                    'disabled': False,
                    'has_gravatar': False,
                    'avatar': {
                        'type': 'initials',
                        'color': '#dfcd00',
                        'initials': 'WW'
                    }
                },
                'href': 'https://api.samanage.com/incidents/31851783-import-contracts-and-software-licenses.json',
                'cc': [],
                'custom_fields_values': [],
                'incidents': [],
                'changes': [],
                'tasks': [],
                'time_tracks': [],
                'solutions': [],
                'assets': [],
                'mobiles': [],
                'other_assets': [],
                'configuration_items': [],
                'purchase_orders': []
            }]
        }
