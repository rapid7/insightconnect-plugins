import komand
from .schema import AddCollaboratorInput, AddCollaboratorOutput
# Custom imports below
import requests


class AddCollaborator(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_collaborator',
                description='Adds a user as a collaborator to a Github repository',
                input=AddCollaboratorInput(),
                output=AddCollaboratorOutput())

    def run(self, params={}):
        r = requests.session()
        try:
            results = r.put(
                "https://api.github.com/repos/{}/{}/collaborators/{}".format(
                    params.get("organization"),
                    params.get("repository"),
                    params.get("username"),
                ),
                auth=self.connection.basic_auth,
                params={"permission": params.get("permission")}
            )
            if results.status_code == 204:
                return {"results": "User is already a collaborator"}
            elif results.status_code == 201:
                return {"results": results.json()}
        except Exception as e:
            self.logger.error("An error has occurred while adding collaborator: ", e)
            raise
