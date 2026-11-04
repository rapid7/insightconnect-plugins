import insightconnect_plugin_runtime
from .schema import SearchInput, SearchOutput, Component, Input, Output

# Custom imports below
from typing import Any


class Search(insightconnect_plugin_runtime.Action):
    def __init__(self) -> None:
        super(self.__class__, self).__init__(
            name="search",
            description=Component.DESCRIPTION,
            input=SearchInput(),
            output=SearchOutput(),
        )

    def run(self, params: dict[str, Any] = {}) -> dict[str, Any]:
        # START INPUT BINDING - DO NOT REMOVE
        customer_id = params.get(Input.CUST_ID, "")
        external_parameters = params.get(Input.EXTERNAL_PARAMS, [])
        queue = params.get(Input.QUEUE, "")
        dynamic_fields = params.get(Input.DYNAMIC_FIELDS, [])
        # END INPUT BINDING - DO NOT REMOVE

        tickets = self.connection.client.search_tickets(
            queue=queue,
            customer_id=customer_id,
            external_parameters=external_parameters,
            dynamic_fields=dynamic_fields,
        )
        return {Output.TICKET_IDS: tickets}
