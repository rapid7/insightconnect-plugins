import komand
import base64

from komand_cef.util import utils

from .schema import ParseMultipleInput, ParseMultipleOutput, Input, Output, Component


class ParseMultiple(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='parse_multiple',
                description=Component.DESCRIPTION,
                input=ParseMultipleInput(),
                output=ParseMultipleOutput())

    def run(self, params={}):
        decoded = base64.b64decode(params.get(Input.FILE)).decode('utf-8')
        lines = decoded.split('\n')

        return {
          Output.CEFS: [utils.parse_cef(line) for line in lines]
        }
