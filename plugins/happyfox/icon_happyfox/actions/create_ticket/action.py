import insightconnect_plugin_runtime
from .schema import CreateTicketInput, CreateTicketOutput, Input, Output, Component

# Custom imports below
from icon_happyfox.util.helpers import convert_dict_keys_case, prepare_ticket_payload, compare_custom_fields
from icon_happyfox.util.constants import TextCase


class CreateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket",
            description=Component.DESCRIPTION,
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    def run(self, params={}):
        custom_fields = params.get(Input.CUSTOMFIELDS)
        if custom_fields:
            compare_custom_fields(
                custom_fields, self.connection.api.get_available_custom_fields(params.get(Input.CATEGORY))
            )
        return {
            Output.TICKET: convert_dict_keys_case(
                self.connection.api.create_ticket(prepare_ticket_payload(params.copy())), TextCase.CAMEL_CASE
            )
        }
