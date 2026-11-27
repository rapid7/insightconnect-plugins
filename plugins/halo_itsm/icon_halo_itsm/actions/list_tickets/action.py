import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument
from .schema import ListTicketsInput, ListTicketsOutput, Input, Output, Component
from icon_halo_itsm.util.helpers import clean_ticket


class ListTickets(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_tickets",
            description=Component.DESCRIPTION,
            input=ListTicketsInput(),
            output=ListTicketsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        status_id = params.get(Input.STATUS_ID)
        tickettype_id = params.get(Input.TICKETTYPE_ID)
        agent_id = params.get(Input.AGENT_ID)
        client_id = params.get(Input.CLIENT_ID)
        count = params.get(Input.COUNT, 50)
        search = params.get(Input.SEARCH)
        # END INPUT BINDING - DO NOT REMOVE

        query_params = {"count": count}

        if status_id:
            query_params["status_id"] = status_id
        if tickettype_id:
            query_params["tickettype_id"] = tickettype_id
        if agent_id:
            query_params["agent_id"] = agent_id
        if client_id:
            query_params["client_id"] = client_id
        if search:
            query_params["search"] = search

        self.logger.info("Listing tickets, filters set: %s", sorted(query_params))
        results = self.connection.client.list_tickets(query_params)

        return {Output.TICKETS: [clean_ticket(ticket) for ticket in results]}
