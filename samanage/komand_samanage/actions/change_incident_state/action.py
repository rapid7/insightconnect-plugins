import komand
from .schema import ChangeIncidentStateInput, ChangeIncidentStateOutput
# Custom imports below


class ChangeIncidentState(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='change_incident_state',
                description='Update the state of an incident',
                input=ChangeIncidentStateInput(),
                output=ChangeIncidentStateOutput())

    def run(self, params={}):
        incident_id = params.get('incident_id')
        state = params.get('state')

        incident = self.connection.api.change_incident_state(
            incident_id, state
        )

        return {'incident': incident}

    def test(self):
        return {
            'incident': {
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
            }
        }
