import komand
from .schema import DecodeInput, DecodeOutput, Input, Output, Component
from komand.exceptions import PluginException
import base64


class Decode(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='decode',
                description=Component.DESCRIPTION,
                input=DecodeInput(),
                output=DecodeOutput())

    def run(self, params={}):
        try:
            data = params.get(Input.BASE64)
            errors = params.get(Input.ERRORS)
            result = base64.standard_b64decode(data)
            if errors in ["replace", "ignore"]:
                return {Output.DATA: result.decode('utf-8', errors=errors)}
            else:
                return {Output.DATA: result.decode('utf-8')}
        except Exception as e:
            self.logger.error("An error has occurred while decoding ", e)
            raise PluginException(cause="Internal error",
                                  assistance='An error has occurred while decoding ',
                                  data=e)
