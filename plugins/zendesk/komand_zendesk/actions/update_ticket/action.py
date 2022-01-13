import insightconnect_plugin_runtime
from .schema import UpdateTicketInput, UpdateTicketOutput, Input, Output

# Custom imports below
import datetime


class UpdateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket",
            description="Update ticket",
            input=UpdateTicketInput(),
            output=UpdateTicketOutput(),
        )

    def run(self, params={}):
        client = self.connection.client

        ticket = client.tickets(id=params.get(Input.TICKET_ID))

        # I am aware that the below code is gross- I considered doing a loop over the params passed in
        # with values. But to do that we'd have to map them 1:1 to the zenpy params and I don't want to be locked into
        # that type of situation

        ticket.assignee_id = (
            ticket.assignee_id if params.get(Input.ASSIGNEE_ID) is None else params.get(Input.ASSIGNEE_ID)
        )
        ticket.collaborator_ids = (
            ticket.collaborator_ids
            if params.get(Input.COLLABORATOR_IDS) is None
            else params.get(Input.COLLABORATOR_IDS)
        )
        ticket.due_at = ticket.due_at if params.get(Input.DUE_AT) is None else params.get(Input.DUE_AT)
        ticket.external_id = (
            ticket.external_id if params.get(Input.EXTERNAL_ID) is None else params.get(Input.EXTERNAL_ID)
        )
        ticket.group_id = ticket.group_id if params.get(Input.GROUP_ID) is None else params.get(Input.GROUP_ID)
        ticket.problem_id = ticket.problem_id if params.get(Input.PROBLEM_ID) is None else params.get(Input.PROBLEM_ID)
        ticket.recipient = ticket.recipient if params.get(Input.RECIPIENT) is None else params.get(Input.RECIPIENT)
        ticket.requester_id = (
            ticket.requester_id if params.get(Input.REQUESTER_ID) is None else params.get(Input.REQUESTER_ID)
        )
        ticket.subject = ticket.subject if params.get(Input.SUBJECT) is None else params.get(Input.SUBJECT)
        ticket.tags = ticket.tags if params.get(Input.TAGS) is None else params.get(Input.TAGS)
        ticket.type = (
            ticket.type
            if (params.get(Input.TYPE)) is None or params.get(Input.TYPE) == ""
            else params.get(Input.TYPE).lower()
        )
        ticket.status = (
            ticket.status
            if (params.get(Input.STATUS)) is None or params.get(Input.STATUS) == ""
            else params.get(Input.STATUS).lower()
        )
        ticket.priority = (
            ticket.priority
            if (params.get(Input.PRIORITY)) is None or params.get(Input.PRIORITY) == ""
            else params.get(Input.PRIORITY).lower()
        )

        if params.get(Input.COMMENT) is not None:
            ticket.comment = params.get(Input.COMMENT)
            if ticket.comment.get("author_id") == "":
                # Avoid bad request error from Zendesk for empty author_id
                del ticket.comment["author_id"]

        client.tickets.update(ticket)
        ticket.priority = None if ticket.priority is None else ticket.priority.capitalize()
        ticket.status = None if ticket.status is None else ticket.status.capitalize()
        ticket.type = None if ticket.type is None else ticket.type.capitalize()

        ticket_obj = {
            "assignee_id": ticket.assignee_id,
            "brand_id": ticket.brand_id,
            "collaborator_ids": ticket.collaborator_ids,
            "created_at": ticket.created_at,
            "due_at": ticket.due_at,
            "external_id": ticket.external_id,
            "forum_topic_id": ticket.forum_topic_id,
            "group_id": ticket.group_id,
            "has_incidents": ticket.has_incidents,
            "id": ticket.id,
            "organization_id": ticket.organization_id,
            "priority": ticket.priority,
            "problem_id": ticket.problem_id,
            "raw_subject": ticket.raw_subject,
            "recipient": ticket.recipient,
            "requester_id": ticket.requester_id,
            "sharing_agreement_ids": ticket.sharing_agreement_ids,
            "status": ticket.status,
            "subject": ticket.subject,
            "submitter_id": ticket.submitter_id,
            "tags": ticket.tags,
            "type": ticket.type,
            "updated_at": ticket.updated_at,
            "url": ticket.url,
        }

        if params.get(Input.COMMENT) is not None:
            ticket_obj["comment"] = ticket.comment

        # I believe this section is for filling out blank properties that ARE blank in the ticket but we need to
        # then conform to our schema still (e.g. None is not string errors)
        output = dict(UpdateTicketOutput().schema)["definitions"]["ticket"]["properties"]
        for key in ticket_obj:
            if ticket_obj[key] == None:
                if key in output.keys():
                    if output[key]["type"] == "string":
                        ticket_obj[key] = ""
                    elif "[]" in output[key]["type"]:
                        ticket_obj[key] = []
                    elif output[key]["type"] == "file":
                        ticket_obj[key] = {"filename": "", "content": ""}
                    elif output[key]["type"] == "date":
                        ticket_obj[key] = datetime.datetime.now()

        ticket_obj = insightconnect_plugin_runtime.helper.clean_dict(ticket_obj)

        return {Output.TICKET: ticket_obj}

    def test(self):
        return {Output.TICKET: {}}
