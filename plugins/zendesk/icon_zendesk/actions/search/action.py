import insightconnect_plugin_runtime
from .schema import SearchInput, SearchOutput, Output, Input

# Custom imports below
from typing import Optional, List, Any
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_zendesk.util.objects import Objects
from icon_zendesk.util.exceptions import detect_type_exception


class Search(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search", description="Search Zendesk", input=SearchInput(), output=SearchOutput()
        )

    def run(self, params={}):
        search_type = params.get(Input.TYPE)
        search_item = params.get(Input.ITEM)

        objects = []
        results = []
        try:
            results = self.connection.client.search(search_item, type=search_type.lower())
        except Exception as error:
            self.logger.debug(error)
            detect_type_exception(error)

        if not results:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)

        for item in results:
            if search_type == "Organization" and results is not None:
                organization_object = Objects.create_organization_object(item)
                objects.append(organization_object)

            if search_type == "Ticket" and results is not None:
                ticket_object = Objects.create_ticket_object(item)
                objects.append(ticket_object)

            if search_type == "User" and results is not None:
                user_object = Objects.create_user_object(item)
                objects.append(user_object)

            if search_type == "Organization":
                return {Output.ORGANIZATIONS: insightconnect_plugin_runtime.helper.clean(objects)}
            elif search_type == "Ticket":
                return {Output.TICKETS: insightconnect_plugin_runtime.helper.clean(objects)}
            else:
                return {Output.USERS: insightconnect_plugin_runtime.helper.clean(objects)}

    @staticmethod
    def convert_to_string(values: Optional[int]) -> Optional[str]:
        if not values:
            return None
        return str(values)

    @staticmethod
    def convert_array(values: Optional[List[Any]]) -> Optional[List[str]]:
        converted_array = []
        for item in values:
            converted_array.append(str(item))
        return converted_array
