import komand
from .schema import ListAllSuspiciousIPEntriesInput, ListAllSuspiciousIPEntriesOutput
# Custom imports below
import requests


class ListAllSuspiciousIPEntries(komand.Action):
    __URL = "https://api.cloudlock.com/api/v2/ip/suspicious"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_all_suspicious_IP_entries',
                description='Lists all suspicious IP entries',
                input=ListAllSuspiciousIPEntriesInput(),
                output=ListAllSuspiciousIPEntriesOutput())

    def run(self, params={}):
        name = params.get("name")
        q = params.get("q")
        offset = params.get("offset")
        limit = params.get("limit")

        params = dict()
        if name is not None:
            params["name"] = name
        if q is not None:
            params["q"] = q
        params["offset"] = offset
        params["limit"] = limit

        try:
            response = self.connection.CLIENT.get(self.__URL, params=params)
            entries = response.json()["items"]
            entries = komand.helper.clean(entries)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            raise error
        return {"entries": entries}

    def test(self):
        url = "https://api.cloudlock.com/api/v2/activities"
        try:
            response = self.connection.CLIENT.get(url)
        except (requests.ConnectionError, requests.HTTPError) as error:
            raise error
        return {}
