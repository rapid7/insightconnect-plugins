import insightconnect_plugin_runtime
from .schema import RetrieveInput, RetrieveOutput, Input, Output, Component

# Custom imports below
from typing import Any


class Retrieve(insightconnect_plugin_runtime.Action):
    def __init__(self) -> None:
        super(self.__class__, self).__init__(
            name="retrieve",
            description=Component.DESCRIPTION,
            input=RetrieveInput(),
            output=RetrieveOutput(),
        )

    def run(self, params: dict[str, Any] = {}) -> dict[str, Any]:
        # START INPUT BINDING - DO NOT REMOVE
        ticket_id = params.get(Input.TICKET_ID, 0)
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.TICKET: self.connection.client.get_ticket(ticket_id)}
