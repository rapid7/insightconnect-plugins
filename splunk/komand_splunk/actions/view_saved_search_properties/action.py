import komand
from .schema import ViewSavedSearchPropertiesInput, ViewSavedSearchPropertiesOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class ViewSavedSearchProperties(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='view_saved_search_properties',
                description=Component.DESCRIPTION,
                input=ViewSavedSearchPropertiesInput(),
                output=ViewSavedSearchPropertiesOutput())

    def run(self, params={}):
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)

        try:
            saved_search = self.connection.client.saved_searches[saved_search_name]
        except KeyError as error:
            raise PluginException(cause=f"Saved search {saved_search_name} was not found!",
                                  assistance="Ensure the saved search exists.",
                                  data=error)

        properties = saved_search.content

        return {Output.PROPERTIES: properties}
