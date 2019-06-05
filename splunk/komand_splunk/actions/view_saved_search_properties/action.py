import komand
from .schema import ViewSavedSearchPropertiesInput, ViewSavedSearchPropertiesOutput
# Custom imports below


class ViewSavedSearchProperties(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='view_saved_search_properties',
                description='Returns the properties for a saved search',
                input=ViewSavedSearchPropertiesInput(),
                output=ViewSavedSearchPropertiesOutput())

    def run(self, params={}):
        saved_search_name = params.get("saved_search_name")

        saved_search = self.connection.client.saved_searches[saved_search_name]
        properties = saved_search.content

        return {"properties": properties}

    def test(self):
        return {}
