import komand
from komand_cef.util import utils
from .schema import ParseSingleInput, ParseSingleOutput, Input, Output, Component


class ParseSingle(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='parse_single',
            description=Component.DESCRIPTION,
            input=ParseSingleInput(),
            output=ParseSingleOutput())

    def run(self, params={}):
        return {
            Output.CEF: utils.parse_cef(params.get(Input.CEF_STRING))
        }
