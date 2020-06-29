import komand
from .schema import FindIssuesInput, FindIssuesOutput, Input, Output, Component
# Custom imports below
from komand_jira.util.util import normalize_issue


class FindIssues(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='find_issues',
            description=Component.DESCRIPTION,
            input=FindIssuesInput(),
            output=FindIssuesOutput())

    def run(self, params={}):
        """Search for issues"""
        max_results = params.get(Input.MAX)
        get_attachments = params.get(Input.GET_ATTACHMENTS, False)
        issues = self.connection.client.search_issues(jql_str=params[Input.JQL], maxResults=max_results)

        results = list(
            map(lambda issue: normalize_issue(issue, get_attachments=get_attachments, logger=self.logger), issues))
        results = komand.helper.clean(results)

        return {Output.ISSUES: results}
