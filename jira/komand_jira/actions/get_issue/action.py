import komand
from .schema import GetIssueInput, GetIssueOutput
# Custom imports below
from ...util import *


class GetIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_issue',
            description='Get Issue',
            input=GetIssueInput(),
            output=GetIssueOutput())

    def run(self, params={}):
        """ Get an issue by ID """
        issue = self.connection.client.issue(id=params['id'])

        if not issue:
            raise Exception('no issue found: ' + params['id'])

        output = normalize_issue(issue=issue, include_raw_fields=True, logger=self.logger)

        clean_output = komand.helper.clean(output)
        return {'found': True, 'issue': clean_output}

    def test(self):
        t = self.connection.test()
        if t:
            return {'found': True, 'issue': {}}
