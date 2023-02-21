import insightconnect_plugin_runtime
from .schema import UpdateTicketInput, UpdateTicketOutput, Input, Output

# Custom imports below
import datetime
from icon_zendesk.util.objects import Objects
from icon_zendesk.util.exceptions import detect_type_exception


class UpdateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket",
            description="Update ticket",
            input=UpdateTicketInput(),
            output=UpdateTicketOutput(),
        )

    def run(self, params={}):  # noqa: C901
        ticket_id = params.get(Input.TICKET_ID)
        assignee_id = params.get(Input.ASSIGNEE_ID)
        collaborator_ids = params.get(Input.COLLABORATOR_IDS)
        due_at = params.get(Input.DUE_AT)
        external_id = params.get(Input.EXTERNAL_ID)
        group_id = params.get(Input.GROUP_ID)
        problem_id = params.get(Input.PROBLEM_ID)
        recipient = params.get(Input.RECIPIENT)
        requester_id = params.get(Input.REQUESTER_ID)
        subject = params.get(Input.SUBJECT)
        tags = params.get(Input.TAGS)
        ticket_type = params.get(Input.TYPE, "").lower()
        status = params.get(Input.STATUS, "").lower()
        priority = params.get(Input.PRIORITY, "").lower()
        comment = params.get(Input.COMMENT)

        try:
            ticket = self.connection.client.tickets(id=ticket_id)
        except Exception as error:
            self.logger.debug(error)
            detect_type_exception(error)

        # I am aware that the below code is gross- I considered doing a loop over the params passed in
        # with values. But to do that we'd have to map them 1:1 to the zenpy params and I don't want to be locked into
        # that type of situation

        ticket.assignee_id = ticket.assignee_id if not ticket_id else assignee_id
        ticket.collaborator_ids = ticket.collaborator_ids if not collaborator_ids else collaborator_ids
        ticket.due_at = ticket.due_at if not due_at else due_at
        ticket.external_id = ticket.external_id if not external_id else external_id
        ticket.group_id = ticket.group_id if not group_id else group_id
        ticket.problem_id = ticket.problem_id if not problem_id else problem_id
        ticket.recipient = ticket.recipient if not recipient else recipient
        ticket.requester_id = ticket.requester_id if not requester_id else requester_id
        ticket.subject = ticket.subject if not subject else subject
        ticket.tags = ticket.tags if not tags else tags
        ticket.type = ticket.type if not ticket_type else ticket_type
        ticket.status = ticket.status if not status else status
        ticket.priority = ticket.priority if priority else priority

        if comment:
            ticket.comment = comment
            if ticket.comment.get("author_id") == "":
                # Avoid bad request error from Zendesk for empty author_id
                del ticket.comment["author_id"]

        try:
            self.connection.client.tickets.update(ticket)
        except Exception as error:
            self.logger.debug(error)
            detect_type_exception(error)

        ticket.priority = None if ticket.priority is None else ticket.priority.capitalize()
        ticket.status = None if ticket.status is None else ticket.status.capitalize()
        ticket.type = None if ticket.type is None else ticket.type.capitalize()

        ticket_object = Objects.create_ticket_object(ticket)

        if comment:
            ticket_object["comment"] = ticket.comment

        # I believe this section is for filling out blank properties that ARE blank in the ticket but we need to
        # then conform to our schema still (e.g. None is not string errors)
        output = dict(UpdateTicketOutput().schema)["definitions"]["ticket"]["properties"]
        for key in ticket_object:  # pylint: disable=consider-using-dict-items
            if ticket_object[key] is None:
                if key in output.keys():
                    if output[key]["type"] == "string":
                        ticket_object[key] = ""
                    elif "[]" in output[key]["type"]:
                        ticket_object[key] = []
                    elif output[key]["type"] == "file":
                        ticket_object[key] = {"filename": "", "content": ""}
                    elif output[key]["type"] == "date":
                        ticket_object[key] = datetime.datetime.now()

        ticket_object = insightconnect_plugin_runtime.helper.clean_dict(ticket_object)
        return {Output.TICKET: ticket_object}
