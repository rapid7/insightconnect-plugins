import komand
from .schema import CreateIncidentInput, CreateIncidentOutput
# Custom imports below


class CreateIncident(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_incident',
                description='Create a new incident',
                input=CreateIncidentInput(),
                output=CreateIncidentOutput())

    def run(self, params={}):
        name = params.get('name')
        requester = params.get('requester')
        priority = params.get('priority')
        description = params.get('description')
        due_at = params.get('due_at')
        assignee = params.get('assignee')
        incidents = params.get('incidents')
        problem = params.get('problem')
        solutions = params.get('solutions')
        category_name = params.get('category_name')

        incident = self.connection.api.create_incident(
            name, requester, priority, description, due_at, assignee,
            incidents, problem, solutions, category_name
        )

        return {'incident': incident}

    def test(self):
        return {
            'incident': {
                'id': 31931440,
                'number': 14,
                'name': 'An incident',
                'description': 'More text',
                'description_no_html': 'More text',
                'state': 'New',
                'priority': 'Medium',
                'category': {
                    'id': 875706,
                    'name': 'Hardware',
                    'default_tags': 'hardware',
                    'children': [{
                        'id': 875708,
                        'name': 'Desktop',
                        'default_tags': 'desktop',
                        'parent_id': 875706
                    }, {
                        'id': 875707,
                        'name': 'Laptop',
                        'default_tags': 'laptop',
                        'parent_id': 875706
                    }, {
                        'id': 875709,
                        'name': 'Peripherals',
                        'default_tags': 'peripherals',
                        'parent_id': 875706
                    }]
                },
                'assignee': {
                    'group_id': 4485265,
                    'is_user': True,
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
                'created_at': '2018-11-21T17:28:30.393-05:00',
                'updated_at': '2018-11-21T17:28:30.393-05:00',
                'due_at': '2022-11-11T00:00:00.000-05:00',
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
                'href': 'https://api.samanage.com/incidents/31931440-an-incident.json',
                'cc': [],
                'custom_fields_values': [],
                'comments': [],
                'attachments': [],
                'statistics': [{
                    'statistic_type': 'State Changed',
                    'time': '00:01',
                    'time_elapsed': '00:01',
                    'business_time_elapsed': '00:01',
                    'value': '2018-11-21 22:28:30 UTC'
                }],
                'tags': [{
                    'id': 18482,
                    'name': 'hardware',
                    'taggings_count': 337059
                }],
                'incidents': [{
                    'id': 31851783,
                    'href': 'https://api.samanage.com/incidents/31851783.json'
                }],
                'changes': [],
                'solutions': [{
                    'id': 795104,
                    'href': 'https://api.samanage.com/solutions/795104.json'
                }],
                'associated_sla_names': [],
                'total_time_spent': 0,
                'tasks': [],
                'time_tracks': [],
                'assets': [],
                'mobiles': [],
                'other_assets': [],
                'configuration_items': [],
                'purchase_orders': [],
                'audits': [],
                'request_variables': []
            }
        }
