import komand
from .schema import UpdateTicketInput, UpdateTicketOutput
# Custom imports below
import datetime


class UpdateTicket(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_ticket',
                description='Update ticket',
                input=UpdateTicketInput(),
                output=UpdateTicketOutput())

    def run(self, params={}):
        client = self.connection.client
        
        ticket = client.tickets(id=params.get("ticket_id"))

        ticket.assignee_id = ticket.assignee_id if params.get('assignee_id') is None else params.get('assignee_id')
        ticket.collaborator_ids = ticket.collaborator_ids if params.get('collaborator_ids') is None else params.get('collaborator_ids')
        ticket.description = ticket.description if params.get('description') is None else params.get('description')
        ticket.due_at = ticket.due_at if params.get('due_at') is None else params.get('due_at')
        ticket.external_id = ticket.external_id if params.get('external_id') is None else params.get('external_id')
        ticket.group_id = ticket.group_id if params.get('group_id') is None else params.get('group_id')
        ticket.problem_id = ticket.problem_id if params.get('problem_id') is None else params.get('problem_id')
        ticket.recipient = ticket.recipient if params.get('recipient') is None else params.get('recipient')
        ticket.requester_id = ticket.requester_id if params.get('requester_id') is None else params.get('requester_id')
        ticket.subject = ticket.subject if params.get('subject') is None else params.get('subject')
        ticket.tags = ticket.tags if params.get('tags') is None else params.get('tags')
        ticket.type = ticket.type if (params.get('type')) is None or params.get('type') == '' else params.get('type').lower()
        ticket.status = ticket.status if (params.get('status')) is None or params.get('status') == '' else params.get('status').lower()
        ticket.priority = ticket.priority if (params.get('priority')) is None or params.get('priority') == '' else params.get('priority').lower()

        client.tickets.update(ticket)

        ticket.priority = ticket.priority.capitalize()
        ticket.status = ticket.status.capitalize()
        ticket.type = ticket.type.capitalize()

        ticket_obj = {
            'assignee_id': ticket.assignee_id, 
            'brand_id': ticket.brand_id, 
            'collaborator_ids': ticket.collaborator_ids, 
            'created_at': ticket.created_at, 
            'description': ticket.description, 
            'due_at': ticket.due_at, 
            'external_id': ticket.external_id, 
            'forum_topic_id': ticket.forum_topic_id, 
            'group_id': ticket.group_id, 
            'has_incidents': ticket.has_incidents, 
            'id': ticket.id, 
            'organization_id': ticket.organization_id, 
            'priority': ticket.priority, 
            'problem_id': ticket.problem_id, 
            'raw_subject': ticket.raw_subject, 
            'recipient': ticket.recipient, 
            'requester_id': ticket.requester_id, 
            'sharing_agreement_ids': ticket.sharing_agreement_ids, 
            'status': ticket.status, 
            'subject': ticket.subject, 
            'submitter_id': ticket.submitter_id, 
            'tags': ticket.tags, 
            'type': ticket.type, 
            'updated_at': ticket.updated_at, 
            'url': ticket.url
        }

        output = dict(UpdateTicketOutput().schema)['definitions']['ticket']['properties']
        for key in ticket_obj:
            if ticket_obj[key] == None:
                if key in output.keys():
                    if output[key]['type'] == 'string':
                        ticket_obj[key] = ''
                    elif '[]' in output[key]['type']:
                        ticket_obj[key] = []
                    elif output[key]['type'] == 'file':
                        ticket_obj[key] = {'filename':'', 'content': ''}
                    elif output[key]['type'] == 'date':
                        ticket_obj[key] = datetime.datetime.now()
                        
        ticket_obj = komand.helper.clean_dict(ticket_obj)
        
        return {"ticket": ticket_obj}        

    def test(self):
        return {"ticket": {}}
