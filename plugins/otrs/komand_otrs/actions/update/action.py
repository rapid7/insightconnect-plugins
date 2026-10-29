import insightconnect_plugin_runtime
from .schema import UpdateInput, UpdateOutput, Input, Output, Component

# Custom imports below
from typing import Any


class Update(insightconnect_plugin_runtime.Action):
    def __init__(self) -> None:
        super(self.__class__, self).__init__(
            name="update",
            description=Component.DESCRIPTION,
            input=UpdateInput(),
            output=UpdateOutput(),
        )

    def run(self, params: dict[str, Any] = {}) -> dict[str, Any]:
        # START INPUT BINDING - DO NOT REMOVE
        ticket_id = params.get(Input.TICKETID, 0)
        priority = params.get(Input.PRIORITY, "")
        pending_time = params.get(Input.PENDINGTIME, "")
        lock = params.get(Input.LOCK, "")
        service = params.get(Input.SERVICE, "")
        sla = params.get(Input.SLA, "")
        queue = params.get(Input.QUEUE, "")
        responsible = params.get(Input.RESPONSIBLE, "")
        title = params.get(Input.TITLE, "")
        customer_user = params.get(Input.CUSTOMERUSER, "")
        ticket_type = params.get(Input.TYPE, "")
        no_article = params.get(Input.NOARTICLE, False)
        article = params.get(Input.ARTICLE, {})
        dynamic_fields = params.get(Input.DYNAMICFIELDS, [])
        attachments = params.get(Input.ATTACHMENTS, [])
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.client.update_ticket(
            ticket_id=ticket_id,
            priority=priority,
            pending_time=pending_time,
            lock=lock,
            service=service,
            sla=sla,
            queue=queue,
            responsible=responsible,
            title=title,
            customer_user=customer_user,
            ticket_type=ticket_type,
            no_article=no_article,
            article=article,
            attachments=attachments,
            dynamic_fields=dynamic_fields,
        )
        return {Output.TICKET_ID: result.get("TicketID"), Output.TICKET_NUMBER: result.get("TicketNumber")}
