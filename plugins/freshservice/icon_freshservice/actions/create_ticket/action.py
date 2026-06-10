import insightconnect_plugin_runtime
from .schema import CreateTicketInput, CreateTicketOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_freshservice.util.helpers import clean_dict, dict_keys_to_camel_case, dict_keys_to_snake_case


class CreateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket",
            description=Component.DESCRIPTION,
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    def run(self, params={}):
        requester_id = params.get(Input.REQUESTERID)
        email = params.get(Input.EMAIL)
        phone = params.get(Input.PHONE)
        attachments = params.get(Input.ATTACHMENTS)
        if not phone and not requester_id and not email:
            raise PluginException(
                cause="The requester has not been provided.",
                assistance="Please provide phone, ID or email of the requester.",
            )

        json_data = clean_dict(dict_keys_to_snake_case(params))
        json_data.pop("attachments", None)

        response = self.connection.api.create_ticket(json_data).get("ticket", {})
        if attachments:
            response = self.connection.api.update_ticket(response.get("id"), attachments=attachments).get("ticket", {})
        return {Output.TICKET: dict_keys_to_camel_case(response)}
