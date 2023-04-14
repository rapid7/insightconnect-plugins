import insightconnect_plugin_runtime
from .schema import CreateTicketInput, CreateTicketOutput, Input, Output

# Custom imports below
from icon_zendesk.util.objects import Objects
from icon_zendesk.util.exceptions import detect_type_exception
from insightconnect_plugin_runtime.helper import clean
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
        assignee_id = params.get(Input.ASSIGNEE_ID) or None
        collaborator_ids = params.get(Input.COLLABORATOR_IDS) or None
        description = params.get(Input.DESCRIPTION) or None
        due_at = params.get(Input.DUE_AT) or None
        external_id = params.get(Input.EXTERNAL_ID) or None
        group_id = params.get(Input.GROUP_ID) or None
        priority = params.get(Input.PRIORITY, "").lower() or None
        problem_id = params.get(Input.PROBLEM_ID) or None
        recipient = params.get(Input.RECIPIENT) or None
        requester_id = params.get(Input.REQUESTER_ID) or None
        status = params.get(Input.STATUS, "").lower() or None
        subject = params.get(Input.SUBJECT) or None
        tags = params.get(Input.TAGS) or None
        ticket_type = params.get(Input.TYPE, "").lower() or None
        attachment = params.get(Input.ATTACHMENT, {})

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
            type=ticket_type,
        )

        try:
            if all((attachment.get("content"), attachment.get("filename"))):
                upload_instance = self.connection.client.attachments.upload(
                    attachment.get("content"),
                    target_name=attachment.get("filename"),
                )
                ticket.comment = Comment(body=description, uploads=[upload_instance.token])
            returned_ticket = self.connection.client.tickets.create(ticket).ticket
            ticket_object = Objects.create_ticket_object(returned_ticket)
            return {Output.TICKET: clean(ticket_object)}
        except Exception as error:
            self.logger.debug(error)
            detect_type_exception(error)
