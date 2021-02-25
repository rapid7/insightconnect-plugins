import insightconnect_plugin_runtime
from .schema import GetBlacklistUrlInput, GetBlacklistUrlOutput, Output, Component

# Custom imports below


class GetBlacklistUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_blacklist_url",
            description=Component.DESCRIPTION,
            input=GetBlacklistUrlInput(),
            output=GetBlacklistUrlOutput(),
        )

    def run(self, params={}):
        return {Output.BLACKLISTED_URLS: self.connection.client.get_blacklist_url().get("blacklistUrls")}
