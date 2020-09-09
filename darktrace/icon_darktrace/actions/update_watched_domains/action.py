# Custom imports below
import datetime

import insightconnect_plugin_runtime
from .schema import UpdateWatchedDomainsInput, UpdateWatchedDomainsOutput, Input, Output, Component


class UpdateWatchedDomains(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='update_watched_domains',
            description=Component.DESCRIPTION,
            input=UpdateWatchedDomainsInput(),
            output=UpdateWatchedDomainsOutput())

    def run(self, params={}):
        response = self.connection.client.update_intelfeed(
            params.get(Input.WATCHED_DOMAIN_STATUS),
            params.get(Input.ENTRY),
            self._get_default(params, Input.DESCRIPTION, "Watched Domains managed by InsightConnect"),
            self._get_default(params, Input.SOURCE, "InsightConnect"),
            self._get_default(
                params,
                Input.EXPIRATION_TIME,
                (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
            ),
            params.get(Input.HOSTNAME, False)
        )

        return {
            Output.SUCCESS: response.get("response") == "SUCCESS",
            Output.ADDED: response.get("added", 0),
            Output.UPDATED: response.get("updated", 0)
        }

    @staticmethod
    def _get_default(params, key, default: str = None):
        entry = params.get(key, default)
        if not entry:
            entry = default

        return entry
