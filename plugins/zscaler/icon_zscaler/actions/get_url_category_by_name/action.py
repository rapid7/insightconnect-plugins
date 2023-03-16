import insightconnect_plugin_runtime
from .schema import GetUrlCategoryByNameInput, GetUrlCategoryByNameOutput, Input, Output, Component

# Custom imports below
from icon_zscaler.util.constants import URL_CATEGORORIES_NAMES, Cause, Assistance
from icon_zscaler.util.helpers import convert_dict_keys_to_camel_case, find_custom_url_category_by_name
from insightconnect_plugin_runtime.exceptions import PluginException


class GetUrlCategoryByName(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_url_category_by_name",
            description=Component.DESCRIPTION,
            input=GetUrlCategoryByNameInput(),
            output=GetUrlCategoryByNameOutput(),
        )

    def run(self, params={}):
        url_category_name = params.get(Input.URLCATEGORYNAME)
        custom_url_category_name = params.get(Input.CUSTOMURLCATEGORYNAME)

        if custom_url_category_name:
            url_category_id = find_custom_url_category_by_name(
                custom_url_category_name, self.connection.client.list_url_categories(custom_only=True)
            ).get("id")
        else:
            url_category_id = URL_CATEGORORIES_NAMES.get(url_category_name)

        return {
            Output.URLCATEGORY: convert_dict_keys_to_camel_case(
                self.connection.client.get_url_category_by_id(url_category_id)
            )
        }
