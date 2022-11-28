import insightconnect_plugin_runtime
from .schema import ListTicketsInput, ListTicketsOutput, Input, Output, Component

# Custom imports below
from icon_freshservice.util.helpers import process_list


class ListTickets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_tickets", description=Component.DESCRIPTION, input=ListTicketsInput(), output=ListTicketsOutput()
        )

    def run(self, params={}):
        predefined_filter = params.get(Input.FILTER)
        requester_id = params.get(Input.REQUESTERID)
        email = params.get(Input.EMAIL)
        updated_since = params.get(Input.UPDATEDSINCE)
        ticket_type = params.get(Input.TYPE)
        order_type = params.get(Input.ORDERTYPE)
        page = params.get(Input.PAGE)
        per_page = params.get(Input.PERPAGE)
        parameters = {
            "filter": predefined_filter if predefined_filter else None,
            "requester_id": requester_id if requester_id else None,
            "email": email if email else None,
            "updated_since": updated_since if updated_since else None,
            "type": ticket_type if ticket_type != "All" else None,
            "order_type": order_type,
            "page": page if page else None,
            "per_page": per_page if 0 < per_page <= 100 else 100,
        }
        return {Output.TICKETS: process_list(self.connection.api.list_tickets(parameters).get("tickets", []))}
