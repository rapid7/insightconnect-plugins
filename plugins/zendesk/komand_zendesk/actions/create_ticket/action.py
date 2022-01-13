import insightconnect_plugin_runtime
from .schema import CreateTicketInput, CreateTicketOutput, Input

# Custom imports below
import json
import zenpy
from zenpy.lib.api_objects import Comment, Ticket


class CreateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket",
            description="Create ticket",
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    def run(self, params={}):
        client = self.connection.client

        assignee_id = params.get(Input.ASSIGNEE_ID) or None
        collaborator_ids = params.get(Input.COLLABORATOR_IDS) or None
        description = params.get(Input.DESCRIPTION) or None
        due_at = params.get(Input.DUE_AT) or None
        external_id = params.get(Input.EXTERNAL_ID) or None
        group_id = params.get(Input.GROUP_ID) or None
        priority = (params.get(Input.PRIORITY)) or None
        if priority:
            priority = priority.lower()
        problem_id = params.get(Input.PROBLEM_ID) or None
        recipient = params.get(Input.RECIPIENT) or None
        requester_id = params.get(Input.REQUESTER_ID) or None
        status = (params.get(Input.STATUS)) or None
        if status:
            status = status.lower()
        subject = params.get(Input.SUBJECT) or None
        tags = params.get(Input.TAGS) or None
        t_type = (params.get(Input.TYPE)) or None
        if t_type:
            t_type = t_type.lower()
        ticket = Ticket(
            assignee_id=assignee_id,
            collaborator_ids=collaborator_ids,
            description=description,
            due_at=due_at,
            external_id=external_id,
            group_id=group_id,
            priority=priority,
            problem_id=problem_id,
            recipient=recipient,
            requester_id=requester_id,
            status=status,
            subject=subject,
            tags=tags,
            type=t_type,
        )
        if params.get(Input.ATTACHMENT):
            if params.get(Input.ATTACHMENT)["content"]:
                upload_instance = client.attachments.upload(
                    params.get(Input.ATTACHMENT)["content"],
                    target_name=params.get(Input.ATTACHMENT)["filename"],
                )  #  content_type=None, content_url=None, file_name=None
                ticket.comment = Comment(body=params.get(Input.DESCRIPTION), uploads=[upload_instance.token])

        returned_ticket = client.tickets.create(ticket).ticket
        ticket_obj = {
            "assignee_id": returned_ticket.assignee_id,
            "brand_id": returned_ticket.brand_id,
            "collaborator_ids": returned_ticket.collaborator_ids,
            "created_at": returned_ticket.created_at,
            "description": returned_ticket.description,
            "due_at": returned_ticket.due_at,
            "external_id": returned_ticket.external_id,
            "forum_topic_id": returned_ticket.forum_topic_id,
            "group_id": returned_ticket.group_id,
            "has_incidents": returned_ticket.has_incidents,
            "id": returned_ticket.id,
            "organization_id": returned_ticket.organization_id,
            "priority": returned_ticket.priority,
            "problem_id": returned_ticket.problem_id,
            "raw_subject": returned_ticket.raw_subject,
            "recipient": returned_ticket.recipient,
            "requester_id": returned_ticket.requester_id,
            "sharing_agreement_ids": returned_ticket.sharing_agreement_ids,
            "status": returned_ticket.status,
            "subject": returned_ticket.subject,
            "submitter_id": returned_ticket.submitter_id,
            "tags": returned_ticket.tags,
            "type": returned_ticket.type,
            "updated_at": returned_ticket.updated_at,
            "url": returned_ticket.url,
        }
        return ticket_obj

    def test(self):
        try:
            test = self.connection.client.users.me().email
            return {"success": test}
        except:
            raise
