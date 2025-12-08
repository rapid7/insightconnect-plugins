import insightconnect_plugin_runtime
import time
from .schema import MonitorIssuesInput, MonitorIssuesOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import normalize_issue, look_up_project
from insightconnect_plugin_runtime.exceptions import PluginException
import datetime


class MonitorIssues(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_issues",
            description=Component.DESCRIPTION,
            input=MonitorIssuesInput(),
            output=MonitorIssuesOutput(),
        )
        self.get_attachments = None
        self.projects = []
        self.jql = ""
        self.issues = {}
        self.minutes = 20
        self.include_fields = False

    def poll(self):
        # Depending on if it's running in the cloud or server
        if not self.connection.is_cloud:
            new_issues = self.connection.client.search_issues(self.jql, startAt=0, maxResults=False, fields="*all")
        else:
            new_issues = self.connection.rest_client.search_issues(self.jql, max_results=5000).get("issues", [])

        # Loop through issues and send new ones
        for issue in new_issues:
            issue_id = issue.id if not self.connection.is_cloud else issue.get("id", "")
            if issue_id and issue_id not in self.issues:
                output = normalize_issue(
                    issue,
                    get_attachments=self.get_attachments,
                    include_raw_fields=self.include_fields,
                    logger=self.logger,
                    is_cloud=self.connection.is_cloud,
                )
                self.issues[issue_id] = datetime.datetime.now()
                self.logger.debug(f"Found: {output}")
                self.send({Output.ISSUE: output})

    def validate_projects(self, projects):
        for project in projects:
            valid_project = look_up_project(
                project, self.connection.client, self.connection.rest_client, is_cloud=self.connection.is_cloud
            )
            if not valid_project:
                raise PluginException(
                    cause=f"Project '{project}' does not exist or the user does not have permission to access the "
                    "project.",
                    assistance="Please provide a valid project ID/name or make sure the project is accessible to the "
                    "user.",
                )

    def clear_issues(self):
        now = datetime.datetime.now()
        issues_to_remove = []
        for key in self.issues:
            issue_date = self.issues.get(key)
            minutes = (now - issue_date).total_seconds() / 60
            if minutes > self.minutes:
                issues_to_remove.append(key)
        for i in issues_to_remove:
            self.issues.pop(i, None)

    def run(self, params={}):
        """Run the trigger"""
        self.jql = params.get(Input.JQL)
        self.projects = params.get(Input.PROJECTS)
        self.get_attachments = params.get(Input.GET_ATTACHMENTS, False)
        self.include_fields = params.get(Input.INCLUDE_FIELDS, False)

        jql = f"(created>=-{self.minutes}m or updated>=-{self.minutes}m)"
        if self.projects:
            self.validate_projects(self.projects)
            project_list = ""
            for i, project in enumerate(self.projects):
                if i == 0:
                    project_list = f"project='{project}'"
                else:
                    project_list += f" or project='{project}'"
            jql += f" and ({project_list})"

        if self.jql:
            jql += f" and ({self.jql})"
        self.jql = jql

        self.logger.info(f"Querying {self.jql}")

        while True:
            self.clear_issues()
            self.poll()
            time.sleep(params.get(Input.INTERVAL, 10))
