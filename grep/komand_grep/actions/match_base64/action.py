import komand
from .schema import MatchBase64Input, MatchBase64Output, Input, Output
# Custom imports below
from bs4 import UnicodeDammit
import base64
from komand_grep.util import utils


class MatchBase64(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='match_base64',
                description='Find pattern in base64 file',
                input=MatchBase64Input(),
                output=MatchBase64Output())

    def run(self, params={}):
        data = params.get(Input.DATA)
        try:
            decoded = base64.b64decode(data).decode('utf-8')
        except Exception as ex:
            self.logger.debug("Error decoding")
            self.logger.debug(ex)
            decoded = UnicodeDammit.detwingle(data).decode('utf-8', errors='ignore')

        output = utils.process_grep(
            utils.cat_lines(
                self.logger,
                decoded,
                params.get(Input.PATTERN),
                params.get(Input.BEHAVIOR)
            )
        )

        return {
            Output.FOUND: output.get(utils.FOUND),
            Output.HITS: output.get(utils.HITS),
            Output.MATCHES: output.get(utils.MATCHES)
        }
