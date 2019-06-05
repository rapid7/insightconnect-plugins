import komand
import requests
from .. import utils
from .schema import GetIssuesByRepoInput, GetIssuesByRepoOutput


class GetIssuesByRepo(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_issues_by_repo',
                description='Retrieve all issues currently open on the specified repo',
                input=GetIssuesByRepoInput(),
                output=GetIssuesByRepoOutput())

    def run(self, params={}):
        try:
            title = params.get("title")
            owner = params.get("owner")
            results = requests.get(
                "https://api.github.com/repos/" + owner + "/" + title + "/issues",
                auth=self.connection.basic_auth
            )
            return { "issues": utils.clean(results.json()) }
        except Exception as e:
            self.logger.error("Could not retrieve specified repo's issues. Error: " + str(e))
