import insightconnect_plugin_runtime
from .schema import CreateIncidentInput, CreateIncidentOutput

# Custom imports below


class CreateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_incident",
            description="Create a new incident",
            input=CreateIncidentInput(),
            output=CreateIncidentOutput(),
        )

    def run(self, params={}):
        name = params.get("name")
        requester = params.get("requester")
        priority = params.get("priority")
        description = params.get("description")
        due_at = params.get("due_at")
        assignee = params.get("assignee")
        incidents = params.get("incidents")
        problem = params.get("problem")
        solutions = params.get("solutions")
        category_name = params.get("category_name")

        incident = self.connection.api.create_incident(
            name,
            requester,
            priority,
            description,
            due_at,
            assignee,
            incidents,
            problem,
            solutions,
            category_name,
        )

        return {"incident": incident}
