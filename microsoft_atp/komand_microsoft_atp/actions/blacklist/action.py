import insightconnect_plugin_runtime
import validators
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component
from datetime import datetime
from datetime import timedelta


class Blacklist(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='blacklist',
            description=Component.DESCRIPTION,
            input=BlacklistInput(),
            output=BlacklistOutput())

    def run(self, params={}):
        self.logger.info("Running...")
        indicator_state = params.get(Input.INDICATOR_STATE)

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
                cause='Did not find indicator to delete.',
                assistance='Indicator not deleted.'
            )
        if len(indicators) > 1:
            self.logger.info("Multiple indicators found. We will only act upon the first match.")

        self.connection.client.delete_indicator(indicators[0].get("id"))
        return indicators[0]

    def _create_or_update_indicator(self, params: dict) -> dict:
        payload = self._create_payload(params)
        self.logger.info(f"payload: {payload}")
        return self.connection.client.submit_or_update_indicator(payload)

    @staticmethod
    def _create_payload(params: dict) -> dict:
        indicator = params.get(Input.INDICATOR)
        title = params.get(Input.TITLE)
        if not title:
            title = indicator

        expiration_time = params.get(Input.EXPIRATION_TIME)
        if not expiration_time:
            one_year_from_now = datetime.now() + timedelta(days=365)
            date_formatted = one_year_from_now.strftime("%Y-%m-%dT%H:%M:%SZ")
            expiration_time = date_formatted

        description = params.get(Input.DESCRIPTION)
        if not description:
            description = "Indicator Blacklisted from InsightConnect"

        return {
            "indicatorValue": params.get(Input.INDICATOR),
            "indicatorType": Blacklist._get_type(indicator),
            "action": params.get(Input.ACTION, "AlertAndBlock"),
            "application": params.get(Input.APPLICATION),
            "title": title,
            "description": description,
            "expirationTime": expiration_time,
            "severity": params.get(Input.SEVERITY, "High"),
            "recommendedActions": params.get(Input.RECOMMENDED_ACTIONS),
            "rbacGroupNames": params.get(Input.RBAC_GROUP_NAMES, [])
        }

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
        elif validators.md5(indicator):
            raise PluginException(
                cause="MD5 hash is not supported.",
                assistance="API supported only SHA256 and SHA1. Please check provided hash and try again."
            )
        raise PluginException(
            cause='Could not determine type of indicator.',
            assistance='Indicator not added.'
        )
