import komand
from .schema import EditIssueInput, EditIssueOutput, Input, Output, Component

# Custom imports below


class EditIssue(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="edit_issue",
            description=Component.DESCRIPTION,
            input=EditIssueInput(),
            output=EditIssueOutput(),
        )

    def run(self, params={}):
        issue_id = params.pop(Input.ID)
        notify = params.pop(Input.NOTIFY)

        clean_params = {}
        for k, v in params.items():
            if v:
                clean_params[k] = v

        self.logger.info(clean_params)

        # https://github.com/pycontribs/jira/blob/master/jira/resources.py#L506
        issue = self.connection.client.issue(id=issue_id)
        try:
            issue.update(notify=notify, **clean_params)
        except Exception as e:
            raise Exception(f"Any error occurred: {e}")

        return {Output.SUCCESS: True}
