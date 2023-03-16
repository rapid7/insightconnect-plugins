import insightconnect_plugin_runtime
from .schema import UpdateUrlsOfUrlCategoryInput, UpdateUrlsOfUrlCategoryOutput, Input, Output, Component

# Custom imports below
from icon_zscaler.util.helpers import (
    convert_dict_keys_to_camel_case,
    find_custom_url_category_by_name,
    filter_dict_keys,
    find_url_category_by_id,
)
from icon_zscaler.util.constants import URL_CATEGORY_UPDATE_ACTIONS, URL_CATEGORORIES_NAMES, Cause, Assistance
from insightconnect_plugin_runtime.exceptions import PluginException


class UpdateUrlsOfUrlCategory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_urls_of_url_category",
            description=Component.DESCRIPTION,
            input=UpdateUrlsOfUrlCategoryInput(),
            output=UpdateUrlsOfUrlCategoryOutput(),
        )

    def run(self, params={}):
        url_category_name = params.get(Input.URLCATEGORYNAME)
        custom_url_category_name = params.get(Input.CUSTOMURLCATEGORYNAME)
        url_list = [url for url in params.get(Input.URLLIST) if url]
        action = params.get(Input.ACTION)

        if not url_list:
            raise PluginException(
                cause=Cause.URL_LIST_NOT_PROVIDED,
                assistance=Assistance.VERIFY_INPUT,
            )

        if custom_url_category_name:
            custom_url_category = find_custom_url_category_by_name(
                custom_url_category_name, self.connection.client.list_url_categories(custom_only=True)
            )
            url_category_id = custom_url_category.get("id")
            url_category_data_to_send = filter_dict_keys(
                custom_url_category, ["configuredName", "description", "scopes", "keywordsRetainingParentCategory"]
            )
        else:
            url_category = find_url_category_by_id(
                URL_CATEGORORIES_NAMES.get(url_category_name), self.connection.client.list_url_categories()
            )
            url_category_id = url_category.get("id")
            url_category_data_to_send = filter_dict_keys(url_category, ["keywordsRetainingParentCategory"])

        url_category_data_to_send.update({"urls": url_list})

        return {
            Output.URLCATEGORY: convert_dict_keys_to_camel_case(
                self.connection.client.update_urls_in_url_category(
                    url_category_id, URL_CATEGORY_UPDATE_ACTIONS.get(action), url_category_data_to_send
                )
            )
        }
