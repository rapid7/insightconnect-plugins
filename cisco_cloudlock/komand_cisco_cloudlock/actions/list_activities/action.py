import komand
from .schema import ListActivitiesInput, ListActivitiesOutput
# Custom imports below
import requests


class ListActivities(komand.Action):

    __URL = "https://api.cloudlock.com/api/v2/activities"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_activities',
                description='Lists the UBA (User Behavioral Analysis) activities',
                input=ListActivitiesInput(),
                output=ListActivitiesOutput())

    def run(self, params={}):
        try:
            response = self.connection.CLIENT.get(self.__URL, params=params)
            activities = response.json()["items"]
            activities = komand.helper.clean(activities)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            raise error
        return {"activities": activities}

    def test(self):
        url = "https://api.cloudlock.com/api/v2/activities"
        try:
            response = self.connection.CLIENT.get(url)
        except (requests.ConnectionError, requests.HTTPError) as error:
            raise error
        return {}
