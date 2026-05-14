"""TeamDynamix InsightConnect Plugin package."""

import insightconnect_plugin_runtime
from icon_teamdynamix.connection.connection import Connection
from icon_teamdynamix.actions.create_ticket.action import CreateTicket
from icon_teamdynamix.actions.get_ticket.action import GetTicket
from icon_teamdynamix.actions.update_ticket.action import UpdateTicket
from icon_teamdynamix.actions.search_tickets.action import SearchTickets


class ICONTeamDynamix(insightconnect_plugin_runtime.Plugin):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="teamdynamix",
            vendor="your_org",
            version="1.0.0",
            description="TeamDynamix ITSM ticketing plugin for InsightConnect",
            connection=Connection(),
        )
        self.add_action(CreateTicket())
        self.add_action(GetTicket())
        self.add_action(UpdateTicket())
        self.add_action(SearchTickets())


def main():
    """Run plugin."""
    ICONTeamDynamix().start()
