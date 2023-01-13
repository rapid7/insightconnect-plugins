import insightconnect_plugin_runtime

from .schema import NewIssueInput, NewIssueOutput, Input, Output

# Custom imports below
import time
from komand_jira.util.util import normalize_issue, look_up_project
from insightconnect_plugin_runtime.exceptions import PluginException


class NewIssue(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_issue",
            description="Trigger which indicates that a new issue has been created",
            input=NewIssueInput(),
            output=NewIssueOutput(),
        )

        self.get_attachments = None
        self.project = None
        self.jql = ""
        self.max = 10
        self.found = {}
        self.include_fields = False

    def poll(self):
        new_issues = self.connection.client.search_issues(self.jql, startAt=0, maxResults=False, fields="*all")
        for issue in new_issues:
            if issue.id not in self.found:
                output = normalize_issue(
                    issue,
                    get_attachments=self.get_attachments,
                    include_raw_fields=self.include_fields,
                    logger=self.logger
                )
                self.found[issue.id] = True
                self.logger.debug(f"Found: {output}")
                self.send({Output.ISSUE: output})

    def run(self, params={}):
        """Run the trigger"""
        self.jql = params.get(Input.JQL)
        self.get_attachments = params.get(Input.GET_ATTACHMENTS, False)
        self.project = params.get(Input.PROJECT)
        self.include_fields = params.get(Input.INCLUDE_FIELDS, False)

        valid_project = look_up_project(self.project, self.connection.client)
        if not valid_project and self.project:
            raise PluginException(
                cause=f"Project '{self.project}' does not exist or the user does not have permission to access the "
                f"project.",
                assistance="Please provide a valid project ID/name or make sure the project is accessible to the user.",
            )

        jql = "created>=-20m"
        if self.project:
            jql += f" and project='{self.project}'"
        if self.jql:
            jql += f" and ({self.jql})"
        self.jql = jql

        self.logger.info(f"Querying {self.jql}")

        while True:
            self.poll()
            time.sleep(params.get(Input.POLL_TIMEOUT, 60))
