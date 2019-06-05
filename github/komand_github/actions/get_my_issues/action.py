import komand
import requests
from .. import utils
from .schema import GetMyIssuesInput, GetMyIssuesOutput


class GetMyIssues(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_my_issues',
                description='Retrieve all issues assigned to the currently authenticated user',
                input=GetMyIssuesInput(),
                output=GetMyIssuesOutput())

    def run(self, params={}):
        try:
            results = requests.get(
                'https://api.github.com/issues',
                auth=self.connection.basic_auth
            )
            return { "issues": utils.clean(results.json()) }
        except Exception as e:
            self.logger.error("Could not retrieve current user's assigned issues. Error: " + str(e))
