import insightconnect_plugin_runtime
import validators
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component


class Blacklist(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='blacklist',
            description=Component.DESCRIPTION,
            input=BlacklistInput(),
            output=BlacklistOutput())

    def run(self, params={}):
        self.logger.info("Running...")
        indicator_state = params.get(Input.INDICATOR_STATE, True)

        return {
            Output.INDICATOR_ACTION_RESPONSE: insightconnect_plugin_runtime.helper.clean(
                self._create_or_update_indicator(params) if indicator_state else self._delete_indicator(params)
            )
        }

    def _delete_indicator(self, params: dict) -> dict:
        indicator = params.get(Input.INDICATOR)
        indicators = self.connection.client.search_indicators(f"?$top=1&$filter=indicatorValue+eq+'{indicator}'").get(
            "value"
        )
        if len(indicators) == 0:
            raise PluginException(
                cause='Did not find indicator to delete',
                assistance='Indicator not deleted'
            )
        if len(indicators) > 1:
            self.logger.info("Multiple indicators found. We will only act upon the first match")

        indicator_id = indicators[0].get("id")
        return self.connection.client.delete_indicator(indicator_id)

    def _create_or_update_indicator(self, params: dict) -> dict:
        return self.connection.client.submit_or_update_indicator(self._create_payload(params))

    @staticmethod
    def _create_payload(params: dict) -> dict:
        indicator = params.get(Input.INDICATOR)
        action = params.get(Input.ACTION, "AlertAndBlock")
        application = params.get(Input.APPLICATION)
        title = params.get(Input.TITLE, indicator)
        description = params.get(Input.DESCRIPTION, indicator)
        expiration_time = params.get(Input.EXPIRATION_TIME)
        severity = params.get(Input.SEVERITY, "High")
        recommended_actions = params.get(Input.RECOMMENDED_ACTIONS)
        rbac_group_names = params.get(Input.RBAC_GROUP_NAMES, [])
        indicator_type = params.get(Input.INDICATOR_TYPE, Blacklist._get_type(indicator))

        payload = {
            "indicatorValue": indicator,
            "indicatorType": indicator_type,
            "action": action,
            "application": application,
            "title": title,
            "description": description,
            "expirationTime": expiration_time,
            "severity": severity,
            "recommendedActions": recommended_actions,
            "rbacGroupNames": rbac_group_names
        }
        return payload

    @staticmethod
    def _get_type(indicator):
        if validators.ipv4(indicator) or validators.ipv6(indicator):
            return "IpAddress"
        elif validators.url(indicator):
            return "Url"
        elif validators.domain(indicator):
            return "DomainName"
        elif validators.sha1(indicator):
            return "FileSha1"
        elif validators.sha256(indicator):
            return "FileSha256"
        raise PluginException(
            cause='Could not determine type of indicator',
            assistance='Indicator not added'
        )
