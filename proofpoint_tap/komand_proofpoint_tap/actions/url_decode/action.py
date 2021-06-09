import insightconnect_plugin_runtime
import quopri
from .schema import UrlDecodeInput, UrlDecodeOutput, Input, Output, Component


# Custom imports below


class UrlDecode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="url_decode", description=Component.DESCRIPTION, input=UrlDecodeInput(), output=UrlDecodeOutput()
        )

    def run(self, params={}):
        params_urls = params.get(Input.URLS, [])
        urls: [str] = []
        for url in params_urls:
            try:
                encoded_url = quopri.decodestring(url).decode("UTF-8")
            except UnicodeDecodeError:
                encoded_url = url

            urls.append(encoded_url)

        return {
            Output.RESULTS: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.get_decoded_url({"urls": urls})
            )
        }
