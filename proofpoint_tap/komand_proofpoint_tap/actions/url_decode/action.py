import insightconnect_plugin_runtime
from .schema import UrlDecodeInput, UrlDecodeOutput, Input, Output, Component


# Custom imports below


class UrlDecode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="url_decode", description=Component.DESCRIPTION, input=UrlDecodeInput(), output=UrlDecodeOutput()
        )

    def run(self, params={}):
        return {
            Output.RESULTS: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.get_decoded_url({"urls": params.get(Input.URLS)})
            )
        }
