import komand
from .schema import ListAppsInput, ListAppsOutput
# Custom imports below


class ListApps(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_apps',
                description='Fetch app name and app ID for all apps in a customer environment',
                input=ListAppsInput(),
                output=ListAppsOutput())

    def run(self, params={}):
        return self.connection.api.list_apps()

    def test(self):
        return {}
