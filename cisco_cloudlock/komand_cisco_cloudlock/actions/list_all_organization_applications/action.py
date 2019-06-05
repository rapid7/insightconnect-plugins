import komand
from .schema import ListAllOrganizationApplicationsInput, ListAllOrganizationApplicationsOutput
# Custom imports below
import requests


class ListAllOrganizationApplications(komand.Action):

    __URL = "https://api.cloudlock.com/api/v2/apps"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_all_organization_applications',
                description='Lists an organizations installed applications',
                input=ListAllOrganizationApplicationsInput(),
                output=ListAllOrganizationApplicationsOutput())

    def run(self, params={}):
        input_classification = params.get("classification")
        offset = params.get("offset")
        limit = params.get("limit")

        params = dict()
        if input_classification is not None:
            params["classification"] = input_classification
        params["offset"] = offset
        params["limit"] = limit

        try:
            response = self.connection.CLIENT.get(self.__URL, params=params)
            applications = response.json()["items"]
            applications = komand.helper.clean(applications)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            raise error

        return {"applications": applications}

    def test(self):
        url = "https://api.cloudlock.com/api/v2/activities"
        try:
            response = self.connection.CLIENT.get(url)
        except (requests.ConnectionError, requests.HTTPError) as error:
            raise error
        return {}
