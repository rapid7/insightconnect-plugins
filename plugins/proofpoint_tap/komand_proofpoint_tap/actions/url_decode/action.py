import insightconnect_plugin_runtime
import quopri
from .schema import UrlDecodeInput, UrlDecodeOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.helpers import clean


class UrlDecode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="url_decode", description=Component.DESCRIPTION, input=UrlDecodeInput(), output=UrlDecodeOutput()
        )

    def run(self, params={}):
        urls: [str] = []
        for url in params.get(Input.URLS, []):
            try:
                encoded_url = quopri.decodestring(url).decode("UTF-8")
            except UnicodeDecodeError:
                encoded_url = url

            urls.append(encoded_url)

        return {Output.URLS: clean(self.connection.client.get_decoded_url({"urls": urls}).get("urls", []))}
