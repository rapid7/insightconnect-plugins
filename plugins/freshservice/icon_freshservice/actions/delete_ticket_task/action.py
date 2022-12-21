import insightconnect_plugin_runtime
from .schema import DeleteTicketTaskInput, DeleteTicketTaskOutput, Input, Output, Component

# Custom imports below


class DeleteTicketTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_ticket_task",
            description=Component.DESCRIPTION,
            input=DeleteTicketTaskInput(),
            output=DeleteTicketTaskOutput(),
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.api.delete_ticket_task(params.get(Input.TICKETID), params.get(Input.TASKID))
        }
