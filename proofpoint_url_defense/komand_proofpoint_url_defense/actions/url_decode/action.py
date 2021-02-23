import insightconnect_plugin_runtime
from .schema import UrlDecodeInput, UrlDecodeOutput, Input, Output

# Custom imports below
from komand_proofpoint_url_defense.util.proofpoint_decoder import URLDefenseDecoder
import re


class UrlDecode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="url_decode",
            description="Decodes an encoded URL",
            input=UrlDecodeInput(),
            output=UrlDecodeOutput(),
        )

    def run(self, params={}):
        in_url = params[Input.ENCODED_URL]
        url_v2 = "https://urldefense.proofpoint.com/"  # This is good for v1 as well
        url_v3 = "https://urldefense.com"
        is_hxxp = in_url.startswith("hxxp")
        in_url = in_url.replace("hxxp", "http").replace("[.]", ".")

        if in_url.startswith(url_v2) or in_url.startswith(url_v3):
            encoded_url = in_url
        elif is_hxxp:
            encoded_url = f"https://urldefense.proofpoint.com/v1/url?u={in_url}&k="
        else:  # We assume a v2 encoded URL, this is legacy behavior
            encoded_url = f"https://urldefense.proofpoint.com/v2/url?u={in_url}&d="

        decoder = URLDefenseDecoder()

        try:
            decoded_url = decoder.decode(encoded_url)
            self.logger.info("URL has been decoded")
            if re.compile("http:/[^/]").match(decoded_url):
                decoded_url = decoded_url.replace("http:/", "http://")
            if re.compile("https:/[^/]").match(decoded_url):
                decoded_url = decoded_url.replace("https:/", "https://")

            return {Output.DECODED_URL: decoded_url, Output.DECODED: True}
        except (Exception, ValueError) as e:
            self.logger.error(f"Unexpected issue occurred decoding URL: {e}")
            return {Output.DECODED_URL: in_url, Output.DECODED: False}
