import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import GetTicketsInput, GetTicketsOutput, Input, Output, Component

# Custom imports below


class GetTickets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_tickets", description=Component.DESCRIPTION, input=GetTicketsInput(), output=GetTicketsOutput()
        )

    def run(self, params: dict = None) -> dict:
        return {
            Output.TICKETS: clean(
                self.connection.api_client.get_tickets(
                    page_size=params.get(Input.PAGESIZE),
                    page=params.get(Input.PAGE),
                    conditions=params.get(Input.CONDITIONS),
                )
            )
        }
