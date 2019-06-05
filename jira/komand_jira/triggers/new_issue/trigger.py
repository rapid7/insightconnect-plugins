import komand
from .schema import NewIssueInput, NewIssueOutput
# Custom imports below
import time
from ...util import *


class NewIssue(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='new_issue',
            description='Trigger which indicates that a new issue has been created',
            input=NewIssueInput(),
            output=NewIssueOutput())

        self.jql = ''
        self.max = 10
        self.found = {}

    def initialize(self):
        new_issues = self.connection.client.search_issues(self.jql, startAt=0)
        for issue in new_issues:
            self.found[issue.id] = True

    def poll(self):
        new_issues = self.connection.client.search_issues(self.jql, startAt=0)
        for issue in new_issues:
            if issue.id not in self.found:
                output = normalize_issue(issue, logger=self.logger)
                self.found[issue.id] = True
                self.logger.debug('found: %s', output)
                self.send({"issue": output})

    def run(self, params={}):
        """Run the trigger"""
        # send a test event
        self.jql = params.get('jql') or ''
        if self.connection.parameters.get('project'):
            if self.jql:
                self.jql = 'project=' + self.connection.parameters['project'] + ' and ' + self.jql
            else:
                self.jql = 'project=' + self.connection.parameters['project']

        self.logger.info('Querying %s', self.jql)

        self.initialize()

        while True:
            self.poll()
            time.sleep(60)

    def test(self):
        t = self.connection.test()
        if t:
            return {'issue': {}}
