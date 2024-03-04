import insightconnect_plugin_runtime
from .schema import CreateIssueInput, CreateIssueOutput, Input, Output, Component

# Custom imports below


class CreateIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_issue",
            description=Component.DESCRIPTION,
            input=CreateIssueInput(),
            output=CreateIssueOutput(),
        )

    # def clean_json(self, obj):
    #     new_json = []
    #     for key, value in obj.items():
    #         if value is None:
    #             value = ""
    #         if key == "assignee" and value == "":
    #             value = {}
    #         if key == "milestone" and value == "":
    #             value = {}
    #         new_json.append((key, value))
    #     output = json.dumps(dict(new_json))
    #     return json.loads(output)

    def run(self, params={}):
        parameters = params.get(Input.PARAMETERS)
        project_id = parameters.get("project_id", 0)

        # TODO - Refactor this so parameters are all separate inputs - only project_id and title are required
        # It doesn't make any sense that user_id is required but then asked 'if' - and also
        # why is it separate from the params type.
        issue_params = {}

        if params.get(Input.ID):
            issue_params["id"] = params.get(Input.ID)
        if parameters.get("title"):
            issue_params["title"] = parameters.get("title")
        if parameters.get("description"):
            issue_params.append(("description", params.get("description")))
        if parameters.get("confidential"):
            issue_params.append(("confidential", params.get("confidential")))
        if parameters.get("assignee_ids"):
            issue_params.append(("assignee_id", params.get("assignee_id")))
        if parameters.get("milestone_id"):
            issue_params.append(("milestone_id", params.get("milestone_id")))
        if parameters.get("labels"):
            issue_params.append(("labels", params.get("labels")))
        if parameters.get("created_at"):
            issue_params.append(("created_at", params.get("created_at")))
        if parameters.get("due_date"):
            issue_params.append(("due_date", params.get("due_date")))
        if parameters.get("merge_request"):
            issue_params.append(("merge_request_to_resolve_discussions_of", params.get("merge_request")))
        if parameters.get("discussion_resolve"):
            issue_params.append(("discussion_to_resolve", params.get("discussion_resolve")))

        response = self.connection.client.create_issue(project_id=project_id, params=issue_params)

        return {}
