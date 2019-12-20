import komand
from .schema import DecodeInput, DecodeOutput, Input, Output
# Custom imports below
from komand_microsoft_atp_safe_links.util.utils import decode_url


class Decode(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='decode',
                description='Decodes a Microsoft Safe Link',
                input=DecodeInput(),
                output=DecodeOutput())

    def run(self, params={}):
        url = params.get(Input.URL)
        try:
            results = decode_url(url)
            if results:
                return {Output.RESULT: results}
            return {Output.RESULT: url}
        except Exception as e:
            return {Output.RESULT: url}
            self.logger.debug(e)
            raise PluginException(cause=f"Error: Unable to decode the Microsoft Safe Link.",
                                  assistance="Check that the input was a valid Safe Link URL. \
                                  If the problem persists, please contact support.")
