import komand
from .schema import ListEntitiesInput, ListEntitiesOutput
# Custom imports below
import requests


class ListEntities(komand.Action):
    __URL = "https://api.cloudlock.com/api/v2/entities"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_entities',
                description='List all asset list pages and exports',
                input=ListEntitiesInput(),
                output=ListEntitiesOutput())

    def run(self, params={}):
        try:
            response = self.connection.CLIENT.get(self.__URL, params=params)
            entities = response.json()["items"]
            entities = komand.helper.clean(entities)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            raise error
        return {"entities": entities}

    def test(self):
        url = "https://api.cloudlock.com/api/v2/activities"
        try:
            response = self.connection.CLIENT.get(url)
        except (requests.ConnectionError, requests.HTTPError) as error:
            raise error
        return {}
