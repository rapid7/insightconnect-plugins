import komand
import requests
from .. import utils
from .schema import GetRepoInput, GetRepoOutput


class GetRepo(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_repo',
                description='Retrieve details, including ID, about a specific repo',
                input=GetRepoInput(),
                output=GetRepoOutput())

    def run(self, params={}):
        try:
            title = params.get("title")
            owner = params.get("owner")
            results = requests.get(
                "https://api.github.com/repos/" + owner + "/" + title,
                auth=self.connection.basic_auth
            )
            return {"data": utils.clean(results.json())}
        except Exception as e:
            self.logger.error("Repo retreival failed. Error: " + str(e))
