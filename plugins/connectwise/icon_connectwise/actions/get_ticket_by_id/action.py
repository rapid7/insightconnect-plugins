import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import GetTicketByIdInput, GetTicketByIdOutput, Input, Output, Component

# Custom imports below


class GetTicketById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_ticket_by_id",
            description=Component.DESCRIPTION,
            input=GetTicketByIdInput(),
            output=GetTicketByIdOutput(),
        )

    def run(self, params: dict = None) -> dict:
        return clean({Output.TICKET: self.connection.api_client.get_ticket_by_id(params.get(Input.TICKET_ID))})
