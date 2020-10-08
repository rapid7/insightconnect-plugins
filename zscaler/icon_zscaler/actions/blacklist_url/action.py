import insightconnect_plugin_runtime
from .schema import BlacklistUrlInput, BlacklistUrlOutput, Input, Output, Component
# Custom imports below
from urllib.parse import urlparse


class BlacklistUrl(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist_url',
                description=Component.DESCRIPTION,
                input=BlacklistUrlInput(),
                output=BlacklistUrlOutput())

    def run(self, params={}):
        blacklist_state = params.get(Input.BLACKLIST_STATE, True)
        if blacklist_state:
            blacklist_step = "ADD_TO_LIST"
        else:
            blacklist_step = "REMOVE_FROM_LIST"

        urls = params.get(Input.URLS)
        normalized_urls = []
        for url in urls:
            if url and not url.startswith("http"):
                url = f"http://{url}"

            normalized_urls.append(
                urlparse(url).hostname
            )

        return {
            Output.SUCCESS: self.connection.client.blacklist_url(blacklist_step, normalized_urls)
        }
