import komand
from .schema import AddMembershipInput, AddMembershipOutput
# Custom imports below
import requests


class AddMembership(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_membership',
                description='Add or update users membership in an organization',
                input=AddMembershipInput(),
                output=AddMembershipOutput())

    def run(self, params={}):
        r = requests.session()
        try:
            results = r.put(
                "https://api.github.com/orgs/{}/memberships/{}".format(
                    params.get("organization"),
                    params.get("username")
                ),
                auth=self.connection.basic_auth,
                params={"role": params.get("role")}
            )
            if results.status_code == 403:
                raise Exception("Account may need org permissions added")
            if results.status_code == 404:
                return {"found": False}
            if results.status_code == 200:
                data = results.json()
                data = komand.helper.clean(data)
                return {
                    "found": True,
                    "url": data["url"],
                    "state": data["state"],
                    "role": data["role"],
                    "user": data["user"],
                    "organization": data["organization"],
                    "organization_url": data["organization_url"]
                }
        except Exception as e:
            self.logger.error("An error has occurred while adding collaborator: ", e)
            raise
