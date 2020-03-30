import komand
from .schema import UrlDecodeInput, UrlDecodeOutput, Input, Output
# Custom imports below
from komand_proofpoint_url_defense.util.proofpoint_decoder import URLDefenseDecoder


class UrlDecode(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='url_decode',
                description='Decodes an encoded URL',
                input=UrlDecodeInput(),
                output=UrlDecodeOutput())

    def run(self, params={}):
        in_url = params[Input.ENCODED_URL]
        url_v2 = 'https://urldefense.proofpoint.com/'  # This is good for v1 as well
        url_v3 = 'https://urldefense.com'

        if in_url.startswith(url_v2) or in_url.startswith(url_v3):
            encoded_url = params.get("encoded_url")
        else:  # We assume a v2 encoded URL, this is legacy behavior
            encoded_url = f"https://urldefense.proofpoint.com/v2/url?u={in_url}"

        decoder = URLDefenseDecoder()

        try:
            decoded_url = decoder.decode(encoded_url)
            self.logger.info('URL has been decoded')
            return {Output.DECODED_URL: decoded_url, Output.DECODE_SUCCESS: True}
        except (Exception, ValueError) as e:
            self.logger.error(f"Unexpected issue occurred decoding URL: {e}")
            return {Output.DECODED_URL: in_url, Output.DECODE_SUCCESS: False}

