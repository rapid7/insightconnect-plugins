import insightconnect_plugin_runtime
import time
from .schema import UpdatedIssueInput, UpdatedIssueOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import normalize_issue, look_up_project
from insightconnect_plugin_runtime.exceptions import PluginException


class UpdatedIssue(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="updated_issue",
            description=Component.DESCRIPTION,
            input=UpdatedIssueInput(),
            output=UpdatedIssueOutput(),
        )
        self.get_attachments = None
        self.projects = []
        self.jql = ""

    def poll(self):
        new_issues = self.connection.client.search_issues(self.jql, startAt=0, maxResults=False, fields="*all")
        for issue in new_issues:
            if issue.id:
                output = normalize_issue(issue, get_attachments=self.get_attachments, logger=self.logger)
                self.logger.debug(f"Found: {output}")
                self.send({Output.ISSUE: output})

    def validate_projects(self, projects):
        for i in range(len(projects)):
            valid_project = look_up_project(projects[i], self.connection.client)
            if not valid_project:
                raise PluginException(
                    cause=f"Project '{projects[i]}' does not exist or the user does not have permission to access the "
                    "project.",
                    assistance="Please provide a valid project ID/name or make sure the project is accessible to the "
                    "user.",
                )

    def run(self, params={}):
        """Run the trigger"""
        self.jql = params.get(Input.JQL)
        self.projects = params.get(Input.PROJECTS)
        self.get_attachments = params.get(Input.GET_ATTACHMENTS, False)

        jql = "(created>=-10m or updated>=-10m)"
        if self.projects:
            self.validate_projects(self.projects)
            project_list = f"project='{self.projects[0]}'"
            for i in range(1, len(self.projects)):
                project_list += f" or project='{self.projects[i]}'"
            jql += f" and ({project_list})"
        if self.jql:
            jql += f" and ({self.jql})"
        self.jql = jql

        self.logger.info(f"Querying {self.jql}")

        while True:
            self.poll()
            time.sleep(params.get(Input.POLL_TIMEOUT, 60))
