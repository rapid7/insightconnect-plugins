import komand
from .schema import FindIssuesInput, FindIssuesOutput
# Custom imports below
from ...util import *


class FindIssues(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='find_issues',
            description='Find Issues',
            input=FindIssuesInput(),
            output=FindIssuesOutput())

    def run(self, params={}):
        """Search for issues"""
        max = params.get('max')
        issues = self.connection.client.search_issues(jql_str=params['jql'], maxResults=max)

        results = list(map(lambda issue: normalize_issue(issue, logger=self.logger), issues))
        results = komand.helper.clean(results)

        return {'issues': results}
