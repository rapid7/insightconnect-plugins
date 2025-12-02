import insightconnect_plugin_runtime
from .schema import FindIssuesInput, FindIssuesOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import normalize_issue


class FindIssues(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="find_issues",
            description=Component.DESCRIPTION,
            input=FindIssuesInput(),
            output=FindIssuesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        jql_str = params.pop(Input.JQL, "")
        max_results = params.pop(Input.MAX)
        get_attachments = params.pop(Input.GET_ATTACHMENTS, False)
        # END INPUT BINDING - DO NOT REMOVE

        # Retrieve issues from Jira, depending on whether it's Cloud or Server
        if not self.connection.is_cloud:
            issues = self.connection.client.search_issues(jql_str=jql_str, maxResults=max_results)
        else:
            issues = self.connection.rest_client.search_issues(jql=jql_str, max_results=max_results).get("issues", [])

        # Normalize issues and return
        results = list(
            map(
                lambda issue: normalize_issue(
                    issue, get_attachments=get_attachments, logger=self.logger, is_cloud=self.connection.is_cloud
                ),
                issues,
            )
        )
        return {Output.ISSUES: insightconnect_plugin_runtime.helper.clean(results)}
