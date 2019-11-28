import komand

from .schema import NewIssueInput, NewIssueOutput
# Custom imports below
import time
from ...util import *
from komand.exceptions import PluginException

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
                output = normalize_issue(issue, get_attachments=self.get_attachments, logger=self.logger)
                self.found[issue.id] = True
                self.logger.debug('found: %s', output)
                self.send({"issue": output})

    def run(self, params={}):
        """Run the trigger"""
        # send a test event
        self.jql = params.get('jql') or ''
        self.get_attachments = params.get('get_attachments', False)
        self.project = params.get('project')

        # Check if project exists
        valid_project = look_up_project(self.project, self.connection.client)
        if not valid_project:
            raise PluginException(cause=f"Project {self.project} does not exist or user don't have permission to access the project.",
                                  assistance='Please provide a valid project ID/name or make sure project is accessible to user.')

        if self.project:
            if self.jql:
                self.jql = 'project=' + self.project + ' and ' + self.jql
            else:
                self.jql = 'project=' + self.project

        self.logger.info('Querying %s', self.jql)

        self.initialize()

        while True:
            self.poll()
            time.sleep(60)
