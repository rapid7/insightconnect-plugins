import insightconnect_plugin_runtime
import time
from .schema import GetNewIssueInput, GetNewIssueOutput, Input, Output, Component

# Custom imports below
from icon_gitlab.util.util import Util
from typing import List, Tuple, Any


class GetNewIssue(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="issue", description=Component.DESCRIPTION, input=GetNewIssueInput(), output=GetNewIssueOutput()
        )

    def run(self, params={}):
        new_issues = []
        seen = []
        issue_params = self.get_issue_params(params=params)

        while True:
            self.logger.info("Searching for new issues.. ")

            issues = self.connection.client.get_issues(issue_params=issue_params)

            for issue in issues:
                issue = Util.clean_json(issue)
                if Util.is_issue_new(issue.get("updated_at", "")):
                    new_issues.append(issue)

            if len(new_issues) > 0:
                if new_issues[0] not in seen:
                    self.send({Output.ISSUE: new_issues[0]})
                    seen.append(new_issues[0])
                else:
                    self.logger.info("No new issues found..")
                    time.sleep(60)
                    continue

            time.sleep(params.get(Input.INTERVAL, 5))

    @staticmethod
    def get_issue_params(params: dict) -> List[Tuple[str, Any]]:
        """
        Helper method to retrieve inputs and reduce 'run' method complexity

        :param params:
        :return:
        """
        issue_params = []

        # Required: False
        if params.get(Input.LABELS):
            issue_params.append(("labels", params.get(Input.LABELS)))
        if params.get(Input.MILESTONE):
            issue_params.append(("milestone", params.get(Input.MILESTONE)))
        if params.get(Input.STATE):
            issue_params.append(("state", params.get(Input.STATE).lower()))
        if params.get(Input.SEARCH):
            issue_params.append(("search", params.get(Input.SEARCH)))
        if params.get(Input.IIDS):
            issue_params.append(("iid", params.get(Input.IIDS)))

        return issue_params
