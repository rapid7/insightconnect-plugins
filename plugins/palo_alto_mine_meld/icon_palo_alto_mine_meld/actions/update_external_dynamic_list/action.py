import insightconnect_plugin_runtime
from .schema import (
    UpdateExternalDynamicListInput,
    UpdateExternalDynamicListOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import validators
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from typing import List, Dict, Any


class UpdateExternalDynamicList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_external_dynamic_list",
            description=Component.DESCRIPTION,
            input=UpdateExternalDynamicListInput(),
            output=UpdateExternalDynamicListOutput(),
        )

    def run(self, params={}):
        list_name = params.get(Input.LIST_NAME, "")
        indicator = params.get(Input.INDICATOR, "")
        operation = params.get(Input.OPERATION, "Add")
        direction = params.get(Input.DIRECTION, "").lower()
        share_level = params.get(Input.SHARE_LEVEL, "").lower()
        comment = params.get(Input.COMMENT, "")

        if operation == "Add":
            updated_indicators_list = self._add_indicator(list_name, indicator, direction, share_level, comment)
        else:
            updated_indicators_list = self._remove_indicator(list_name, indicator)

        return {
            Output.SUCCESS: self.connection.client.update_external_dynamic_list(list_name, updated_indicators_list).get(
                "result"
            )
            == "ok"
        }

    def _add_indicator(
        self, list_name: str, indicator: str, direction: str = None, share_level: str = None, comment: str = None
    ) -> List[Dict[str, Any]]:
        indicator_type = self._get_indicator_type(indicator)
        indicators_list = self.connection.client.get_indicators(list_name).get("result", [])
        for list_indicator in indicators_list:
            if list_indicator.get("indicator") == indicator:
                raise PluginException(
                    cause="Duplicate indicator.",
                    assistance=f"Indicator already exists in {list_name}.",
                )
        indicators_list.append(
            clean(
                {
                    "indicator": indicator,
                    "type": indicator_type,
                    "direction": direction,
                    "share_level": share_level,
                    "comment": comment,
                }
            )
        )
        return indicators_list

    def _remove_indicator(self, list_name: str, indicator: str) -> List[Dict[str, Any]]:
        indicators_list = self.connection.client.get_indicators(list_name).get("result", [])
        updated_indicators_list = []
        for list_indicator in indicators_list:
            if list_indicator.get("indicator") == indicator:
                continue
            updated_indicators_list.append(list_indicator)
        if len(updated_indicators_list) == len(indicators_list):
            raise PluginException(cause="Not exist.", assistance=f"Indicator does not exist in {list_name}.")
        return updated_indicators_list

    @staticmethod
    def _get_indicator_type(indicator):
        if validators.ipv4(indicator, cidr=False):
            return "IPv4"
        elif validators.ipv6(indicator, cidr=False):
            return "IPv6"
        elif validators.ipv4(indicator, cidr=True, strict=False):
            return "IPv4 CIDR"
        elif validators.ipv6(indicator, cidr=True, strict=False):
            return "IPv6 CIDR"
        elif validators.url(indicator):
            return "URL"
        elif validators.domain(indicator):
            return "domain"
        raise PluginException(
            cause=f"The provided indicator {indicator} is invalid.",
            assistance="The provided indicator must be a domain, IPv4 address, IPv6 address, or URL.",
        )
