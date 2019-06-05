import komand
from .schema import ListAllIncidentsInput, ListAllIncidentsOutput
# Custom imports below
import requests


class ListAllIncidents(komand.Action):

    __URL = "https://api.cloudlock.com/api/v2/incidents"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_all_incidents',
                description='List all incidents triggered by the CloudLock policy engine',
                input=ListAllIncidentsInput(),
                output=ListAllIncidentsOutput())

    def run(self, params={}):
        severity = params.get("severity")
        created_before = params.get("created_before")
        created_after = params.get("created_after")
        offset = params.get("offset")
        limit = params.get("limit")

        params = dict()
        if severity is not None and len(severity) != 0:
            params["severity"] = severity
        if created_before is not None and len(created_before) != 0:
            params["created_before"] = created_before
        if created_after is not None and len(created_after) != 0:
            params["created_after"] = created_after
        params["offset"] = offset
        params["limit"] = limit

        try:
            response = self.connection.CLIENT.get(url=self.__URL, params=params)

            incidents = response.json()["items"]
            incidents = komand.helper.clean(incidents)

        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            raise error

        return {"incidents": incidents}


    def test(self):
        url = "https://api.cloudlock.com/api/v2/activities"
        try:
            response = self.connection.CLIENT.get(url)
        except (requests.ConnectionError, requests.HTTPError) as error:
            raise error
        return {}
