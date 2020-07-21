import insightconnect_plugin_runtime
from .schema import UpdateExternalDynamicListInput, UpdateExternalDynamicListOutput, Input, Output, Component
# Custom imports below
import validators
from insightconnect_plugin_runtime.exceptions import PluginException


class UpdateExternalDynamicList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_external_dynamic_list',
                description=Component.DESCRIPTION,
                input=UpdateExternalDynamicListInput(),
                output=UpdateExternalDynamicListOutput())

    def run(self, params={}):
        list_name = params.get(Input.LIST_NAME)
        indicators_list = self.connection.client.get_indicators(list_name).get("result")
        indicator = params.get(Input.INDICATOR)
        operation = params.get(Input.OPERATION, "Add")

        if operation == "Add":
            updated_indicators_list = self._add_indicator(indicators_list, indicator, list_name)
        else:
            updated_indicators_list = self._remove_indicator(indicators_list, indicator, list_name)

        return {
            Output.SUCCESS: self.connection.client.update_external_dynamic_list(list_name, updated_indicators_list)
                                .get("result") == "ok"
        }

    def _add_indicator(self, indicators_list: list, indicator: str, list_name: str):
        updated_indicators_list = indicators_list.copy()
        for list_indicator in indicators_list:
            if list_indicator.get("indicator") == indicator:
                raise PluginException(
                    cause="Duplicate indicator.",
                    assistance=f"Indicator already exists in {list_name}."
                )

        updated_indicators_list.append({
            "indicator": indicator,
            "type": self._get_indicator_type(indicator)
        })

        return updated_indicators_list

    @staticmethod
    def _remove_indicator(indicators_list: list, indicator: str, list_name: str):
        updated_indicators_list = []
        for list_indicator in indicators_list:
            if list_indicator.get("indicator") == indicator:
                continue

            updated_indicators_list.append(list_indicator)

        if len(updated_indicators_list) == len(indicators_list):
            raise PluginException(
                cause="Not exist.",
                assistance=f"Indicator does not exist in {list_name}."
            )

        return updated_indicators_list

    @staticmethod
    def _get_indicator_type(indicator):
        if validators.ipv4(indicator):
            return "IPv4"
        elif validators.ipv6(indicator):
            return "IPv6"
        elif validators.url(indicator):
            return "URL"

        return "domain"
