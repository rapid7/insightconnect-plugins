import insightconnect_plugin_runtime
from .schema import CreateInput, CreateOutput, Input, Output, Component

# Custom imports below
from typing import Any


class Create(insightconnect_plugin_runtime.Action):
    def __init__(self) -> None:
        super(self.__class__, self).__init__(
            name="create",
            description=Component.DESCRIPTION,
            input=CreateInput(),
            output=CreateOutput(),
        )

    def run(self, params: dict[str, Any] = {}) -> dict[str, Any]:
        # START INPUT BINDING - DO NOT REMOVE
        title = params.get(Input.TITLE, "")
        queue = params.get(Input.QUEUE, "")
        lock = params.get(Input.LOCK, "")
        ticket_type = params.get(Input.TYPE, "")
        service = params.get(Input.SERVICE, "")
        sla = params.get(Input.SLA, "")
        state = params.get(Input.STATE, "")
        priority = params.get(Input.PRIORITY, "")
        pending_time = params.get(Input.PENDINGTIME, "")
        owner = params.get(Input.OWNER, "")
        responsible = params.get(Input.RESPONSIBLE, "")
        customer_user = params.get(Input.CUSTOMERUSER, "")
        article = params.get(Input.ARTICLE, {})
        dynamic_fields = params.get(Input.DYNAMIC_FIELDS, [])
        attachments = params.get(Input.ATTACHMENTS, [])
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.client.create_ticket(
            title=title,
            queue=queue,
            ticket_type=ticket_type,
            state=state,
            priority=priority,
            customer_user=customer_user,
            lock=lock,
            service=service,
            sla=sla,
            pending_time=pending_time,
            owner=owner,
            responsible=responsible,
            article=article,
            attachments=attachments,
            dynamic_fields=dynamic_fields,
        )
        return {Output.TICKET_ID: result.get("TicketID"), Output.TICKET_NUMBER: result.get("TicketNumber")}
