import insightconnect_plugin_runtime
from .schema import CreateTicketTaskInput, CreateTicketTaskOutput, Input, Output, Component

# Custom imports below
from icon_freshservice.util.constants import task_status
from insightconnect_plugin_runtime.helper import clean
from icon_freshservice.util.helpers import dict_keys_to_camel_case


class CreateTicketTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket_task",
            description=Component.DESCRIPTION,
            input=CreateTicketTaskInput(),
            output=CreateTicketTaskOutput(),
        )

    def run(self, params={}):
        due_date = params.get(Input.DUEDATE)
        group_id = params.get(Input.GROUPID)
        json_data = {
            "title": params.get(Input.TITLE),
            "description": params.get(Input.DESCRIPTION),
            "status": task_status.get(params.get(Input.STATUS)),
            "notify_before": params.get(Input.NOTIFYBEFORE),
            "due_date": due_date if due_date else None,
            "group_id": group_id if group_id else None,
        }
        return {
            Output.TASK: dict_keys_to_camel_case(
                self.connection.api.create_ticket_task(params.get(Input.TICKETID), clean(json_data)).get("task", {})
            )
        }
