import komand
from .schema import ListAllOrganizationPoliciesInput, ListAllOrganizationPoliciesOutput
# Custom imports below
import requests


class ListAllOrganizationPolicies(komand.Action):

    __URL = "https://api.cloudlock.com/api/v2/policies"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_all_organization_policies',
                description='Lists all of an organizations configured policies',
                input=ListAllOrganizationPoliciesInput(),
                output=ListAllOrganizationPoliciesOutput())

    def run(self, params={}):
        input_state = params.get("state")
        offset = params.get("offset")
        limit = params.get("limit")

        params = dict()
        if input_state is not None:
            params["state"] = input_state.upper()  # CloudLock input is case-sensitive
        params["offset"] = offset
        params["limit"] = limit

        try:
            response = self.connection.CLIENT.get(self.__URL, params=params)

            policies = response.json()
            policies = komand.helper.clean(policies)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            raise error

        return {"policies": policies}

    def test(self):
        url = "https://api.cloudlock.com/api/v2/activities"
        try:
            response = self.connection.CLIENT.get(url)
        except (requests.ConnectionError, requests.HTTPError) as error:
            raise error
        return {}
