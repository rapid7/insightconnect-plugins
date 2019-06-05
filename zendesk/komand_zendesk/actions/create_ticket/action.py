import komand
from .schema import CreateTicketInput, CreateTicketOutput
# Custom imports below
import json
import zenpy
from zenpy.lib.api_objects import Comment, Ticket

class CreateTicket(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_ticket',
                description='Create ticket',
                input=CreateTicketInput(),
                output=CreateTicketOutput())

    def run(self, params={}):
        client = self.connection.client

        assignee_id = params.get('assignee_id') or None
        collaborator_ids = params.get('collaborator_ids') or None
        description = params.get('description') or None
        due_at = params.get('due_at') or None
        external_id = params.get('external_id') or None
        group_id = params.get('group_id') or None
        priority = (params.get('priority')) or None
        if priority:
            priority = priority.lower()
        problem_id = params.get('problem_id') or None
        recipient = params.get('recipient') or None
        requester_id = params.get('requester_id') or None
        status = (params.get('status')) or None
        if status:
            status = status.lower()
        subject = params.get('subject') or None
        tags = params.get('tags') or None
        t_type = (params.get('type')) or None
        if t_type:
            t_type = t_type.lower()
        ticket = Ticket(
        assignee_id=assignee_id, collaborator_ids=collaborator_ids, 
        description=description, due_at=due_at, external_id=external_id, 
        group_id=group_id, priority=priority, 
        problem_id=problem_id, recipient=recipient, requester_id=requester_id, 
        status=status, subject=subject, tags=tags, type=t_type)
        if params.get('attachment'):
            if params.get('attachment')['content']: 
                upload_instance = client.attachments.upload(params.get('attachment')['content'], target_name=params.get('attachment')['filename']) #  content_type=None, content_url=None, file_name=None
                ticket.comment = Comment(body=params.get('description'), uploads=[upload_instance.token])


        returned_ticket = client.tickets.create(ticket).ticket
        ticket_obj = {
                'assignee_id': returned_ticket.assignee_id, 
                'brand_id': returned_ticket.brand_id, 
                'collaborator_ids': returned_ticket.collaborator_ids, 
                'created_at': returned_ticket.created_at, 
                'description': returned_ticket.description, 
                'due_at': returned_ticket.due_at, 
                'external_id': returned_ticket.external_id, 
                'forum_topic_id': returned_ticket.forum_topic_id, 
                'group_id': returned_ticket.group_id, 
                'has_incidents': returned_ticket.has_incidents, 
                'id': returned_ticket.id, 
                'organization_id': returned_ticket.organization_id, 
                'priority': returned_ticket.priority, 
                'problem_id': returned_ticket.problem_id, 
                'raw_subject': returned_ticket.raw_subject, 
                'recipient': returned_ticket.recipient, 
                'requester_id': returned_ticket.requester_id, 
                'sharing_agreement_ids': returned_ticket.sharing_agreement_ids, 
                'status': returned_ticket.status, 
                'subject': returned_ticket.subject, 
                'submitter_id': returned_ticket.submitter_id, 
                'tags': returned_ticket.tags, 
                'type': returned_ticket.type, 
                'updated_at': returned_ticket.updated_at, 
                'url': returned_ticket.url
            }
        return ticket_obj

    def test(self):
        try:
          test = self.connection.client.users.me().email
          return { 'success': test }
        except:
          raise
