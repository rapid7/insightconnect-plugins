import insightconnect_plugin_runtime
from .schema import CreateTicketWithAttachmentsInput, CreateTicketWithAttachmentsOutput, Input, Output, Component

# Custom imports below
from icon_happyfox.util.helpers import (
    convert_dict_keys_case,
    prepare_ticket_payload,
    prepare_attachments,
    compare_custom_fields,
)
from icon_happyfox.util.constants import TextCase


class CreateTicketWithAttachments(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket_with_attachments",
            description=Component.DESCRIPTION,
            input=CreateTicketWithAttachmentsInput(),
            output=CreateTicketWithAttachmentsOutput(),
        )

    def run(self, params={}):
        custom_fields = params.get(Input.CUSTOMFIELDS)
        if custom_fields:
            compare_custom_fields(
                custom_fields, self.connection.api.get_available_custom_fields(params.get(Input.CATEGORY))
            )
        parameters = params.copy()
        parameters.pop("attachments")
        return {
            Output.TICKET: convert_dict_keys_case(
                self.connection.api.create_ticket_with_attachments(
                    prepare_ticket_payload(parameters), prepare_attachments(params.get(Input.ATTACHMENTS))
                ),
                TextCase.CAMEL_CASE,
            )
        }
