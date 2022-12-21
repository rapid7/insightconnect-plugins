import insightconnect_plugin_runtime
from .schema import UpdateTicketTaskInput, UpdateTicketTaskOutput, Input, Output, Component

# Custom imports below
from icon_freshservice.util.constants import task_status
from insightconnect_plugin_runtime.helper import clean
from icon_freshservice.util.helpers import dict_keys_to_camel_case


class UpdateTicketTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket_task",
            description=Component.DESCRIPTION,
            input=UpdateTicketTaskInput(),
            output=UpdateTicketTaskOutput(),
        )

    def run(self, params={}):
        title = params.get(Input.TITLE)
        description = params.get(Input.DESCRIPTION)
        due_date = params.get(Input.DUEDATE)
        group_id = params.get(Input.GROUPID)
        json_data = {
            "title": title if title else None,
            "description": description if description else None,
            "status": task_status.get(params.get(Input.STATUS)),
            "notify_before": params.get(Input.NOTIFYBEFORE),
            "due_date": due_date if due_date else None,
            "group_id": group_id if group_id else None,
        }
        return {
            Output.TASK: dict_keys_to_camel_case(
                self.connection.api.update_ticket_task(
                    params.get(Input.TICKETID), params.get(Input.TASKID), clean(json_data)
                ).get("task", {})
            )
        }
