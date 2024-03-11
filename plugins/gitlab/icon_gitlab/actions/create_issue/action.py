import insightconnect_plugin_runtime
from .schema import CreateIssueInput, CreateIssueOutput, Input, Output, Component

# Custom imports below
from icon_gitlab.util.util import Util


class CreateIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_issue",
            description=Component.DESCRIPTION,
            input=CreateIssueInput(),
            output=CreateIssueOutput(),
        )

    def run(self, params={}):
        project_id = params.get(Input.PROJECT_ID)

        # Required: True inputs
        issue_params = [("title", params.get(Input.TITLE))]

        # Required: False inputs
        if params.get(Input.DESCRIPTION):
            issue_params.append(("description", params.get(Input.DESCRIPTION)))
        if params.get(Input.CONFIDENTIAL):
            issue_params.append(("confidential", params.get(Input.CONFIDENTIAL)))
        if params.get(Input.ASSIGNEE_IDS):
            issue_params.append(("assignee_id", params.get(Input.ASSIGNEE_IDS)))
        if params.get(Input.MILESTONE_ID):
            issue_params.append(("milestone_id", params.get(Input.MILESTONE_ID)))
        if params.get(Input.LABELS):
            issue_params.append(("labels", params.get(Input.LABELS)))
        if params.get(Input.CREATED_AT):
            issue_params.append(("created_at", params.get(Input.CREATED_AT)))
        if params.get(Input.DUE_DATE):
            issue_params.append(("due_date", params.get(Input.DUE_DATE)))
        if params.get(Input.MERGE_REQUEST):
            issue_params.append(("merge_request_to_resolve_discussions_of", params.get(Input.MERGE_REQUEST)))
        if params.get(Input.DISCUSSION_RESOLVE):
            issue_params.append(("discussion_to_resolve", params.get(Input.DISCUSSION_RESOLVE)))

        response = self.connection.client.create_issue(project_id=project_id, issue_params=issue_params)
        response = Util.clean_json(response)

        return {
            Output.ID: response.get("id"),
            Output.TITLE: response.get("title"),
            Output.LABELS: response.get("labels"),
            Output.CREATED_AT: response.get("created_at"),
            Output.DUE_DATE: response.get("due_date"),
            Output.PROJECT_ID: response.get("project_id"),
            Output.STATE: response.get("state"),
            Output.MILESTONE: response.get("milestone"),
            Output.DESCRIPTION: response.get("description"),
            Output.WEB_URL: response.get("web_url"),
            Output.ASSIGNEES: response.get("assignees"),
            Output.AUTHOR: response.get("author"),
            Output.IID: response.get("iid"),
            Output.SUBSCRIBED: response.get("subscribed"),
            Output.UPDATED_AT: response.get("updated_at"),
            Output.USER_NOTES_COUNT: response.get("user_notes_count"),
        }
