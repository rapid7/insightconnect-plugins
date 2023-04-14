import insightconnect_plugin_runtime
from .schema import CreateProblemInvestigationInput, CreateProblemInvestigationOutput, Input, Output, Component

# Custom imports below
from icon_bmc_helix_itsm.util.constants import ProblemRequest


class CreateProblemInvestigation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="createProblemInvestigation",
            description=Component.DESCRIPTION,
            input=CreateProblemInvestigationInput(),
            output=CreateProblemInvestigationOutput(),
        )

    def run(self, params={}):
        problem_parameters = {
            ProblemRequest.SITE_GROUP: params.get(Input.SITEGROUP),
            ProblemRequest.REGION: params.get(Input.REGION),
            ProblemRequest.SITE: params.get(Input.SITE),
            ProblemRequest.DESCRIPTION: params.get(Input.DESCRIPTION),
            ProblemRequest.COMPANY: params.get(Input.COMPANY),
            ProblemRequest.LAST_NAME: params.get(Input.LASTNAME),
            ProblemRequest.FIRST_NAME: params.get(Input.FIRSTNAME),
            ProblemRequest.URGENCY: params.get(Input.URGENCY),
            ProblemRequest.IMPACT: params.get(Input.IMPACT),
            ProblemRequest.INVESTIGATION_DRIVER: params.get(Input.INVESTIGATIONDRIVER),
            ProblemRequest.COORDINATOR_SUPPORT_COMPANY: params.get(Input.COORDINATORSUPPORTCOMPANY),
            ProblemRequest.COORDINATOR_SUPPORT_ORGANIZATION: params.get(Input.COORDINATORSUPPORTORGANIZATION),
            ProblemRequest.COORDINATOR_GROUP: params.get(Input.COORDINATORGROUP),
            ProblemRequest.COORDINATOR: params.get(Input.COORDINATOR),
            ProblemRequest.ASSIGNEE_SUPPORT_COMPANY: params.get(Input.ASSIGNEESUPPORTCOMPANY),
            ProblemRequest.ASSIGNEE_SUPPORT_ORGANIZATION: params.get(Input.ASSIGNEESUPPORTORGANIZATION),
            ProblemRequest.ASSIGNEE_GROUP: params.get(Input.ASSIGNEEGROUP),
            ProblemRequest.ASSIGNEE: params.get(Input.ASSIGNEE),
            ProblemRequest.Z1D_ACTION: "PROBLEM",
        }
        return {
            Output.PROBLEMINVESTIGATIONNUMBER: self.connection.api_client.create_problem_investigation(
                problem_parameters
            )
        }
